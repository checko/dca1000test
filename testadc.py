from adc import *

dca = DCA1000()
dca.send_start_command()
adc_data = dca.read(timeout=.1)
frame = dca.organize(adc_data,num_chirps=16,num_rx=4,num_samples=256)