from adc import DCA1000
import numpy as np

dca = DCA1000()
dca.send_start_command()
adc_data = dca.read(timeout=.1)
np.save('framedata',adc_data)
frame = dca.organize(adc_data,num_chirps=16,num_rx=4,num_samples=256)
dca.send_stop_command()
#print(frame[0][0][0])