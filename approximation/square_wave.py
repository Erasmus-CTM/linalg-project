def square_wave(t):
    return 2*(t < T/2).astype(int) -1