set GEOS_HEADERS=%PREFIX%\include
set GEOS_LIB=%PREFIX%\lib

:: VS2008 doesn't have stdbool.h
if "%VS_MAJOR%" == "9" (
    copy %RECIPE_DIR%\stdbool.h %CONDA_PREFIX%\\include
)

python setup.py install --single-version-externally-managed --record record.txt --with-cython
