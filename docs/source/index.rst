.. wrf-domain-tool documentation master file, created by
   sphinx-quickstart on 2025-05-03.

Welcome to wrf-domain-tool's documentation!
===========================================
.. image:: https://img.shields.io/badge/GitHub-WRFDomain-blue?logo=github
   :target: https://github.com/gc13141112/wrf-domain-tool
   :alt: GitHub Repository

Useful Links
------------
- `WRF public site <https://www2.mmm.ucar.edu/wrf/users/>`_
- `Wetland example <https://forum.mmm.ucar.edu/threads/temporal-changing-surface-fields-tidal-wetlands.10595/>`_
- `landcover process <https://github.com/gc13141112/coupledreview/tree/master/landcover/>`_


The WRF Domain Tool, together with a shapefile, allows us to plot the WRF domain.

Here's an example program that plots the nest domain.

.. code:: python

      import wrf_domain_tool.domain_generator as WRF
      wrf = WRF.WRFDomain([
         'https://geo.datav.aliyun.com/areas_v3/bound/100000.json',  # 中国
         'https://geo.datav.aliyun.com/areas_v3/bound/510000.json'   # 四川
      ],dx_base=27000,
         ratios=[1, 3])
      wrf.load_shapefiles()
      wrf.compute_domain_params()
      wrf.write_namelist("namelist.wps")
      wrf.plot_domains()
.. code-block:: fortran
   &share
   max_dom = 7,
   start_date = '2024-06-01_00:00:00', '2024-06-01_00:00:00', '2024-06-01_00:00:00', '2024-06-01_00:00:00',
   end_date   = '2024-06-02_00:00:00', '2024-06-02_00:00:00', '2024-06-02_00:00:00', '2024-06-02_00:00:00',
   interval_seconds = 21600,
   io_form_geogrid = 2,
   /

   &geogrid
   parent_id            = 1, 1, 2, 1, 3, 1, 4
   parent_grid_ratio    = 1, 3, 3, 3, 3, 3, 3
   i_parent_start       = 1, 91, 61, 136, 28, 138, 33
   j_parent_start       = 1, 36, 47, 61, 31, 18, 14
   e_we                 = 235, 124, 88, 73, 64, 103, 73
   e_sn                 = 160, 121, 91, 70, 64, 67, 64
   dx = 27000.0,
   dy = 27000.0,
   map_proj = 'lambert',
   ref_lat = 28.480215434999998,
   ref_lon = 104.2990125,
   truelat1 = 30.0,
   truelat2 = 60.0,
   stand_lon = 104.2990125,
   geog_data_res = 'default', 'default', 'default', 'default',
   geog_data_path ='/home/gaochao/model/software/geog/geog/'
   /


.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   wrf-domain-tool

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
