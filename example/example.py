import wrf_domain_tool.domain_generator as WRF
wrf = WRF.WRFDomain(
    shapefiles=[
        "https://geo.datav.aliyun.com/areas_v3/bound/100000.json",  # 全国
        "https://geo.datav.aliyun.com/areas_v3/bound/510000.json",  # 四川
        "https://geo.datav.aliyun.com/areas_v3/bound/410000.json",   # 河南
        "https://geo.datav.aliyun.com/areas_v3/bound/440000.json"   # D04 - 广东
    ],
    ratios=[1, 3, 3,3]
)

wrf.load_shapefiles()
wrf.compute_domain_params()
wrf.write_namelist("namelist.wps")
wrf.plot_domains()