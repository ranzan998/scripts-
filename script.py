# impost the os library

import os

# call conda from the python script. It assumes that we've FERRET environment installed through conda.
# test.jnl is a ferret script that we want to run from python itself.
os.system('conda run -n FERRET ferret -script wavelet_cw_ccw.jnl')

# To run a fortran code
os.system('gfortran test.f -o test.o')

#to run a fortran code that has netcdf dependency, and needs to be linked with other subroutines inside the code
os.system('f77 -c -I/usr/include test.f; f77 -o test test.o -L/{path to netcdff} -lnetcdff; ./test')

# multiple codes like this can be stored in a shell script (e.g, test_multiple.sh) and can be called through python
os.system('bash test_multiple.sh')
