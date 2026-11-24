def plot_trig_approx(find_c, func, Nvals):
    for N in Nvals:
        M=2*N+1
        p = points_p(find_c, N)
        plt.plot(tp, p, label=f"p(t), M={M}.")
    plt.plot( tp, func(tp), '-k', label = 'f(t)')
    plt.legend()
    plt.show()