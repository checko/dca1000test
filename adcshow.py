from adc import DCA1000
import numpy as np
import matplotlib.pyplot as plt

dca = DCA1000()
dca.connect_command()


for bigi in range(40):
    dca.send_start_command()
    adc_data = dca.read(timeout=.1)
    dca.send_stop_command()
    frame = np.zeros(len(adc_data)//2,dtype = complex)
    frame[0::2] = adc_data[0::4] + 1j * adc_data[2::4]
    frame[1::2] = adc_data[1::4] + 1j * adc_data[3::4]
    frame = frame.reshape(32*4,256)
    '''
    plt.clf()
    plt.plot(np.abs(np.fft.fft(frame[0])))
    plt.show(block=False)
    plt.pause(0.01)
    '''
    range_plot = np.fft.fft(frame,axis=1)
    #plt.imshow(np.abs(range_plot))
    #plt.pause(0.1)

    range_doppler = np.fft.fft(range_plot,axis=0)
    plt.imshow(np.abs(range_doppler))
    plt.pause(0.05)