# impost the os library

import os

# call conda from the python script. It assumes that we've FERRET environment installed through conda.
# test.jnl is a ferret script that we want to run from python itself.
os.system('conda run -n FERRET ferret -script wavelet_cw_ccw.jnl')

#
os.system(' ')
