import datetime
import utm
from utm import *

# path relative to the root dir of this template. Leave as mesh/blah.msh in most cases
# added my file and data
mesh_file = 'celtic_sea.msh'
forcing_boundary = 666
utm_zone = 30
utm_band="U"
cent_lat = -592967
cent_lon = 6703824
spin_up = 172800  # 2 days in seconds
end_time = 2764800 # 32 days
output_dir = "output"
output_time = 900 #outputs generated every 15 mins
constituents = ['M2', 'S2', 'N2', 'K2', 'K1', 'O1', 'P1', 'Q1', 'M4']
# year, month, day, hour, min, sec
start_datetime = datetime.datetime(2000,1,1,0,0,0) 
time_diff = 0
