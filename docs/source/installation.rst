Installation
============

To install ``wrf-domain-tool``, you can either use the source code directly or install it as a Python package.

Requirements
------------

- Python 3.8+
- `geopandas <https://geopandas.org/>`_
- `matplotlib <https://matplotlib.org/>`_
- `cartopy <https://scitools.org.uk/cartopy/>`_
- `shapely`, `pyproj`, `numpy`

You can install dependencies via pip:

.. code-block:: bash

    pip install geopandas matplotlib cartopy shapely pyproj numpy

Install from GitHub
-------------------

If you're using the development version or cloning the repository manually:

.. code-block:: bash

    git clone https://github.com/your-username/wrf-domain-tool.git
    cd wrf-domain-tool
    pip install -e .

This will install the package in editable mode, allowing you to make local changes and test them directly.

Install via pip (future support)
--------------------------------

Once published to PyPI, you will be able to install it via:

.. code-block:: bash

    pip install wrf-domain-tool

Note: This feature will be available after PyPI release.

Testing Installation
--------------------

To verify the installation:

.. code-block:: bash

    python -c "from wrf_domain_tool import WRFDomain; print('Installed successfully')"
