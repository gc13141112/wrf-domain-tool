import geopandas as gpd
from pathlib import Path
from typing import List

class WRFDomain:
    """
    A class for calculating WRF nested domains from shapefiles and generating namelist.wps.

    Attributes:
        shapefiles (List[str]): Paths to shapefiles representing domain boundaries.
        dx_base (float): Base resolution for the outermost domain (meters).
        ratios (List[int]): Nesting ratios for each domain.
        domains (List[dict]): Computed domain parameters.
    """

    def __init__(self, shapefiles: List[str], dx_base=27000, ratios=[1, 3, 3]):
        self.shapefiles = shapefiles
        self.dx_base = dx_base
        self.ratios = ratios
        self.domains = []

    def load_shapefiles(self):
        """Load shapefiles and calculate geographic centers and extents."""
        for shp in self.shapefiles:
            gdf = gpd.read_file(shp)
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

    def write_namelist(self, i_starts: List[int], j_starts: List[int], output_path="namelist.wps"):
        """Write WRF namelist.wps based on domain parameters."""
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
