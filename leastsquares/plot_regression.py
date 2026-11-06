def plot_regression(x, f, nvals):
    for n in nvals:
        p = np.arange(0,n+1).reshape((1,-1))
        A = x**p
        sol = np.linalg.solve(A.T@A,A.T@f)
        t = np.linspace(0,3.5,100).reshape((-1,1))
        plt.plot( t, t**p@sol, label = f"n={n}" )
    plt.scatter(x,f)
    plt.legend()
    plt.show()