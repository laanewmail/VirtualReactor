from Solvers.analit_solve import AnalitSolution
from Solvers.numeric_solve import NumericSolution
from Settings.utils.rnd_points import rnd_points

import matplotlib.pyplot as plt
import pylab


def plot_all(**kwargs):
    A_Solver = AnalitSolution()

    N_Solver = NumericSolution()
    N_Solution = N_Solver.nf_Solve()

    n_points = 50

    pylab.subplot(3, 3, 1)
    pylab.plot(N_Solution.t, N_Solution.y[0])
    # pylab.title("Численное решение Y1")

    pylab.subplot(3, 3, 2)
    pylab.plot(A_Solver.t, A_Solver.SolveY1(A_Solver.t)/1.0)
    # pylab.title("Аналитическое решение Y1")

    pylab.subplot(3, 3, 3)
    points = rnd_points(A_Solver.SolveY1, n_points, norm=1.0)
    pylab.scatter(x=points[0], y=points[1], marker='o', c='r', edgecolor='b')
    # pylab.plot(A_Solver.t, A_Solver.SolveY1(A_Solver.t) / 1.0)

    pylab.subplot(3, 3, 4)
    pylab.plot(N_Solution.t, N_Solution.y[1])
    # pylab.title("Численное решение Y3")

    pylab.subplot(3, 3, 5)
    pylab.plot(A_Solver.t, A_Solver.SolveY3(A_Solver.t) / 2.5)

    pylab.subplot(3, 3, 6)
    points = rnd_points(A_Solver.SolveY3, n_points, norm=2.5)
    pylab.scatter(x=points[0], y=points[1], marker='o', c='r', edgecolor='b')
    # pylab.plot(A_Solver.t, A_Solver.SolveY1(A_Solver.t) / 1.0)

    pylab.subplot(3, 3, 7)
    pylab.plot(N_Solution.t, N_Solution.y[2]/9)
    # pylab.title("Численное решение Y3")

    pylab.subplot(3, 3, 8)
    pylab.plot(A_Solver.t, A_Solver.SolveY5(A_Solver.t) / 18.0)

    pylab.subplot(3, 3, 9)
    points = rnd_points(A_Solver.SolveY5, n_points, norm=18)
    pylab.scatter(x=points[0], y=points[1], marker='o', c='r', edgecolor='b')
    # pylab.plot(A_Solver.t, A_Solver.SolveY1(A_Solver.t) / 1.0)

    pylab.show()


plot_all()