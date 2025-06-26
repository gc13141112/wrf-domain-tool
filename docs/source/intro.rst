Introduction
============

Philosophy
----------

The philosophy behind ``wrf-domain-tool`` is centered on usability, reproducibility, and scientific rigor in WRF domain configuration.

1. Shapefile-Centric Configuration
----------------------------------
*“Let the domain speak for itself.”*

- Uses shapefiles as the primary input for defining nested domains.
- Domain boundaries are determined directly from real geographic data.
- Avoids manual input of center coordinates and grid dimensions.

2. Automation over Manual Effort
--------------------------------
*“Repeatable science requires reproducible setup.”*

- Automatically calculates `ref_lat`, `ref_lon`, `e_we`, `e_sn`, `dx`, and `dy`.
- Produces a fully structured ``namelist.wps`` file with minimal configuration.
- Designed for automated workflows and high-throughput simulations.

3. Projection-Aware and Domain-Focused
--------------------------------------
*“Good domains start with good projections.”*

- Detects and adapts to shapefile coordinate reference systems (CRS).
- Supports WRF-compatible projections such as Lambert Conformal and Mercator.
- Emphasizes the importance of correct map projections in regional climate modeling.

4. Transparent and Inspectable
------------------------------
*“You should always see what your domain looks like.”*

- Includes built-in visualization for nested domains using Matplotlib and Cartopy.
- Supports overlaying administrative boundaries for intuitive inspection.
- Exposes internal parameters (e.g., bounding boxes, domain centers) to the user.

5. Composable and Extensible
----------------------------
*“No domain is an island.”*

- Modular and object-oriented design enables easy extension.
- Independent components for shapefile parsing, grid calculation, and namelist generation.
- Easily integrates with larger WRF preprocessing or experiment automation systems.