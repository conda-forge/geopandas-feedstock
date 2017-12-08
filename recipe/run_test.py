import os
import geopandas

fname = os.path.join(os.environ['RECIPE_DIR'], 'test_data', 'test.shp')
geopandas.read_file(fname)


import fiona
div20m = geopandas.read_file('test_issue_31')
print(div20m.head())
