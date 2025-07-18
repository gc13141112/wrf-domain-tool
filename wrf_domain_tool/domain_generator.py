import geopandas as gpd
from pathlib import Path
from typing import List
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.feature import COASTLINE, BORDERS
from matplotlib.patches import Rectangle
import pyproj
class WRFDomain:
    """
    A class for calculating WRF nested domains from shapefiles and generating namelist.wps.

    Attributes:
        shapefiles (List[str]): Paths to shapefiles representing domain boundaries.
        dx_base (float): Base resolution for the outermost domain (meters).
        ratios (List[int]): Nesting ratios for each domain.
        domains (List[dict]): Computed domain parameters.
    """

    def __init__(self, shapefiles: List[str], dx_base: float = None, ratios: List[int] = None):
        self.shapefiles = shapefiles

        if dx_base is None:
            self.dx_base = 27000
        else:
            self.dx_base = dx_base

        if ratios is None:
            self.ratios = [1] + [3] * (len(shapefiles) - 1)
        else:
            assert len(ratios) == len(shapefiles), "Each shapefile must have a corresponding nesting ratio."
            self.ratios = ratios

        self.domains = []

    def load_shapefiles(self):
        """Load shapefiles and calculate geographic centers and extents."""
        for shp in self.shapefiles:
            gdf = gpd.read_file(shp)
            if gdf.crs is None or not gdf.crs.is_projected:
                gdf = gdf.to_crs("EPSG:4326")
            bounds = gdf.total_bounds  # (minx, miny, maxx, maxy)
            minx, miny, maxx, maxy = bounds
            center_lon = (minx + maxx) / 2
            center_lat = (miny + maxy) / 2
            width_km = (maxx - minx) * 111  # rough conversion
            height_km = (maxy - miny) * 111
            self.domains.append({
                "center_lat": center_lat,
                "center_lon": center_lon,
                "width_km": width_km,
                "height_km": height_km
            })

    def compute_domain_params(self):
        """Compute dx/dy and domain size in grid points for each nest."""
        for i, dom in enumerate(self.domains):
            dx = self.dx_base / self.ratios[i]
            dom["dx"] = dx
            dom["dy"] = dx
            dom["e_we"] = int(dom["width_km"] * 1000 / dx) + 1
            dom["e_sn"] = int(dom["height_km"] * 1000 / dx) + 1

    def auto_start_indices(self):
        """Automatically compute i_parent_start and j_parent_start between nested domains."""
        i_starts = [1]
        j_starts = [1]
        geoms = []
        centers = []

        for shp in self.shapefiles:
            gdf = gpd.read_file(shp)
            gdf = gdf.to_crs("EPSG:3857")
            bounds = gdf.total_bounds
            minx, miny, maxx, maxy = bounds
            centerx = (minx + maxx) / 2
            centery = (miny + maxy) / 2
            centers.append((centerx, centery))
            geoms.append((minx, miny, maxx, maxy))

        for i in range(1, len(self.shapefiles)):
            parent_minx, parent_miny, _, _ = geoms[i - 1]
            parent_dx = self.dx_base / self.ratios[i - 1]
            dx = parent_dx
            i_start = int((centers[i][0] - parent_minx) / dx)
            j_start = int((centers[i][1] - parent_miny) / dx)
            i_starts.append(i_start)
            j_starts.append(j_start)

        return i_starts, j_starts

    def write_namelist(self, output_path="namelist.wps"):
        """Write WRF namelist.wps based on domain parameters."""
        i_starts, j_starts = self.auto_start_indices()

        with open(output_path, "w") as f:
            f.write("&share\n")
            f.write(f" max_dom = {len(self.domains)},\n")
            f.write(" start_date = " + ", ".join(["'2024-06-01_00:00:00'"] * len(self.domains)) + ",\n")
            f.write(" end_date   = " + ", ".join(["'2024-06-02_00:00:00'"] * len(self.domains)) + ",\n")
            f.write(" interval_seconds = 21600,\n io_form_geogrid = 2,\n/\n\n")

            f.write("&geogrid\n")
            f.write(" parent_id = " + ", ".join(["1" if i == 0 else str(i) for i in range(1, len(self.domains) + 1)]) + ",\n")
            f.write(" parent_grid_ratio = " + ", ".join(map(str, self.ratios)) + ",\n")
            f.write(" i_parent_start = " + ", ".join(map(str, i_starts)) + ",\n")
            f.write(" j_parent_start = " + ", ".join(map(str, j_starts)) + ",\n")
            f.write(" e_we = " + ", ".join(str(d["e_we"]) for d in self.domains) + ",\n")
            f.write(" e_sn = " + ", ".join(str(d["e_sn"]) for d in self.domains) + ",\n")
            f.write(" dx = " + str(self.domains[0]["dx"]) + ",\n dy = " + str(self.domains[0]["dy"]) + ",\n")
            f.write(" map_proj = 'lambert',\n")
            f.write(f" ref_lat = {self.domains[0]['center_lat']},\n ref_lon = {self.domains[0]['center_lon']},\n")
            f.write(" truelat1 = 30.0,\n truelat2 = 60.0,\n stand_lon = " + str(self.domains[0]['center_lon']) + ",\n")
            f.write(" geog_data_res = " + ", ".join(["'default'"] * len(self.domains)) + ",\n")
            f.write(" geog_data_path = '/your/WPS_GEOG',\n/\n")
    def plot_domains(self):
        """Plot domains in projected Lambert Conformal coordinates (meters)."""
        """Plot WRF nested domains with Lambert projection, national and provincial boundaries."""
        
        center_lat = self.domains[0]['center_lat']
        center_lon = self.domains[0]['center_lon']

        # Lambert投影 (和WRF配置保持一致)
        lcc_proj = ccrs.LambertConformal(
            central_longitude=center_lon,
            central_latitude=center_lat,
            standard_parallels=(30, 60)
        )

        fig, ax = plt.subplots(figsize=(12, 10), subplot_kw={"projection": lcc_proj})
        ax.set_title("WRF Nested Domains with China Borders")

        # 添加 cartopy 自带国界 & 海岸线
        # ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.8)
        # ax.add_feature(cfeature.BORDERS.with_scale('50m'), linewidth=0.8, linestyle="--", edgecolor='gray')
        # ax.add_feature(cfeature.LAND, facecolor="#f5f5f5")
        # ax.add_feature(cfeature.OCEAN, facecolor="#cceeff")

        # 加载中国省界数据（Aliyun GeoJSON）
        try:
            gdf = gpd.read_file('https://geo.datav.aliyun.com/areas_v3/bound/100000.json')
            gdf = gdf.to_crs(lcc_proj.proj4_init)
            gdf.plot(ax=ax, facecolor='none', edgecolor='gray', linewidth=0.6)

            gdf = gpd.read_file('https://geo.datav.aliyun.com/areas_v3/bound/510000.json')
            gdf = gdf.to_crs(lcc_proj.proj4_init)
            gdf.plot(ax=ax, facecolor='none', edgecolor='gray', linewidth=0.6)

            gdf = gpd.read_file('https://geo.datav.aliyun.com/areas_v3/bound/410000.json')
            gdf = gdf.to_crs(lcc_proj.proj4_init)
            gdf.plot(ax=ax, facecolor='none', edgecolor='gray', linewidth=0.6)

            gdf = gpd.read_file('https://geo.datav.aliyun.com/areas_v3/bound/440000.json')
            gdf = gdf.to_crs(lcc_proj.proj4_init)
            gdf.plot(ax=ax, facecolor='none', edgecolor='gray', linewidth=0.6)
        except Exception as e:
            print(f"❌ 无法加载省界数据: {e}")

        # 绘制嵌套域框
        transformer = pyproj.Transformer.from_crs("EPSG:4326", lcc_proj.proj4_init, always_xy=True)
        for i, dom in enumerate(self.domains):
            width_m = dom["width_km"] * 1000
            height_m = dom["height_km"] * 1000
            x_center, y_center = transformer.transform(dom["center_lon"], dom["center_lat"])
            lower_left_x = x_center - width_m / 2
            lower_left_y = y_center - height_m / 2

            rect = Rectangle((lower_left_x, lower_left_y), width_m, height_m,
                            transform=lcc_proj,
                            edgecolor=f"C{i}", facecolor='none', linewidth=2, label=f"Domain {i+1}")
            ax.add_patch(rect)

            ax.plot(dom["center_lon"], dom["center_lat"], marker="x", color=f"C{i}", transform=ccrs.PlateCarree())
            ax.text(dom["center_lon"], dom["center_lat"], f"D{i+1}", transform=ccrs.PlateCarree(),
                    fontsize=11, ha="center", va="center")

        ax.legend()
        ax.gridlines(draw_labels=True)
        plt.savefig('test.jpg',dpi = 200, bbox_inches ='tight')
