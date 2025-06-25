import wrf_domain_tool.domain_generator as WRF
wrf = WRF.WRFDomain([
    'https://geo.datav.aliyun.com/areas_v3/bound/100000.json',  # 中国
    'https://geo.datav.aliyun.com/areas_v3/bound/510000.json'   # 四川
],dx_base=27000,
    ratios=[1, 3])
wrf.load_shapefiles()
wrf.compute_domain_params()
wrf.write_namelist("namelist.wps")