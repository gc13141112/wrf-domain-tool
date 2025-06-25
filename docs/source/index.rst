.. wrf-domain-tool documentation master file, created by
   sphinx-quickstart on 2025-05-03.

Welcome to wrf-domain-tool's documentation!
===========================================
.. image:: https://img.shields.io/badge/GitHub-WRFDomain-blue?logo=github
   :target: https://github.com/gc13141112/wrf-domain-tool
   :alt: GitHub Repository
Geographic information systems use GeoTIFF and other formats to organize and
store gridded raster datasets such as satellite imagery and terrain models.
Rasterio reads and writes these formats and provides a Python API based on
Numpy N-dimensional arrays and GeoJSON.

Here's an example program that extracts the GeoJSON shapes of a raster's valid
data footprint.

.. code:: python

    import rasterio
    import rasterio.features
    import rasterio.warp

    with rasterio.open('example.tif') as dataset:

        # Read the dataset's valid data mask as a ndarray.
        mask = dataset.dataset_mask()

        # Extract feature shapes and values from the array.
        for geom, val in rasterio.features.shapes(
                mask, transform=dataset.transform):

            # Transform shapes from the dataset's own coordinate
            # reference system to CRS84 (EPSG:4326).
            geom = rasterio.warp.transform_geom(
                dataset.crs, 'EPSG:4326', geom, precision=6)

            # Print GeoJSON shapes to stdout.
            print(geom)

The output of the program:

.. code:: python

    {'type': 'Polygon', 'coordinates': [[(-77.730817, 25.282335), ...]]}

Rasterio supports Python versions 3.6 or higher.

.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   wrf-domain-tool

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
