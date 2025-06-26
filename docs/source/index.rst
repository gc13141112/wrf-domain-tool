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

.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   wrf-domain-tool

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
