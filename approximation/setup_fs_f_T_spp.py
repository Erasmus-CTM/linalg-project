freq_s = 44100
freq = 440
T= 1/freq
samples_per_period = int(freq_s/freq)
tp = np.linspace(0,T,samples_per_period).reshape((-1,1))