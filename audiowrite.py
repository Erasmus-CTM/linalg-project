def audiowrite(filename, f, freq_s):
    ofile = wave.open(filename, 'w')
    ofile.setsampwidth(2)
    ofile.setframerate(freq_s)
    ofile.setnchannels(1)
    max_amplitude = 2**15-1
    f=max_amplitude*f
    f=f.astype(np.uint16)
    ofile.writeframesraw(f.astype(np.uint16).tobytes())
    ofile.close()