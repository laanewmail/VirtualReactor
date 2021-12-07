import pylab

from Solvers.numeric_solve import NumericSolution


def plot_all(**kwargs):
    N_Solver = NumericSolution()

    N_Solution = N_Solver.nf_Solve()
    N_Solver.generate_rnd_time()
    rnd_N_Solution = N_Solver.rnd_points(N_Solution)

    # SOLVE 1
    pylab.subplot(3, 3, 1)
    pylab.title("Численное решение")
    pylab.plot(N_Solver.t, N_Solution[0] / max(N_Solution[0]))

    pylab.subplot(3, 3, 3)
    pylab.title("Численное решение + Шум")
    pylab.plot(N_Solver.t, N_Solution[0] / max(N_Solution[0]))
    pylab.scatter(x=rnd_N_Solution[0], y=rnd_N_Solution[1][0], marker='o', c='r', edgecolor='b')

    pylab.subplot(3, 3, 2)
    pylab.title("Экспериментальные данные")
    pylab.scatter(x=rnd_N_Solution[0], y=rnd_N_Solution[1][0], marker='o', c='r', edgecolor='b')

    # SOLVE 2
    pylab.subplot(3, 3, 4)
    pylab.plot(N_Solver.t, N_Solution[1] / max(N_Solution[1]))

    pylab.subplot(3, 3, 6)
    pylab.plot(N_Solver.t, N_Solution[1] / max(N_Solution[1]))
    pylab.scatter(x=rnd_N_Solution[0], y=rnd_N_Solution[1][1], marker='o', c='r', edgecolor='b')

    pylab.subplot(3, 3, 5)
    pylab.scatter(x=rnd_N_Solution[0], y=rnd_N_Solution[1][1], marker='o', c='r', edgecolor='b')

    # SOLVE 3
    pylab.subplot(3, 3, 7)
    pylab.plot(N_Solver.t, N_Solution[2] / max(N_Solution[2]))

    pylab.subplot(3, 3, 9)
    pylab.plot(N_Solver.t, N_Solution[2] / max(N_Solution[2]))
    pylab.scatter(x=rnd_N_Solution[0], y=rnd_N_Solution[1][2], marker='o', c='r', edgecolor='b')

    pylab.subplot(3, 3, 8)
    pylab.scatter(x=rnd_N_Solution[0], y=rnd_N_Solution[1][2], marker='o', c='r', edgecolor='b')

    pylab.show()


plot_all()
