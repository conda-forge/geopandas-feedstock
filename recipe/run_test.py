import os
import geopandas

import os
import geopandas


# Read ESRI shapefile.
fname = os.path.join(os.environ['RECIPE_DIR'], 'test_data', 'test.shp')
gdf = geopandas.read_file(fname)


# Save geopackage.
gdf.to_file(
    driver='GPKG',
    filename='geopackage.gpkg',
    layer='geodata'
)

# Read geopackage.
gpkg = geopandas.read_file('geopackage.gpkg')


# Compare.
from pandas.testing import assert_frame_equal

assert_frame_equal(gdf, gpkg)

# Test issue #31.
import fiona
div20m = geopandas.read_file('test_issue_31')
print(div20m.head())
