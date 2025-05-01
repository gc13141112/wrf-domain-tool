# wrf-domain-tool

自动从多个 Shapefile 文件生成 WRF 模拟的多层嵌套 domain，并自动输出 `namelist.wps`。

## 安装

```bash
conda create -n wrfdom python=3.10 geopandas shapely -c conda-forge
git clone https://github.com/yourusername/wrf-domain-tool.git
cd wrf-domain-tool
pip install .
