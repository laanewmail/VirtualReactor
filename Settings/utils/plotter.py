from Solvers.analit_solve import AnalitSolution
from Solvers.numeric_solve import NumericSolution

import matplotlib.pyplot as plt
import pylab


def plot_all(**kwargs):
    A_Solver = AnalitSolution()

    N_Solver = NumericSolution(time=A_Solver.t)

    N_Solution = N_Solver.nf_Solve()

    # SOLVE 1
    pylab.subplot(3, 3, 1)
    pylab.title("Численное решение")
    pylab.plot(N_Solver.t, N_Solution[0])

    pylab.subplot(3, 3, 2)
    pylab.title("Аналитическое решение")
    a_solve_1 = A_Solver.SolveY1(A_Solver.t)
    pylab.plot(A_Solver.t, a_solve_1/max(a_solve_1))

    pylab.subplot(3, 3, 3)
    pylab.title("Экспериментальные данные")
    points = A_Solver.rnd_points(A_Solver.SolveY1)
    pylab.scatter(x=points[0], y=points[1], marker='o', c='r', edgecolor='b')

    # SOLVE 2
    pylab.subplot(3, 3, 4)
    pylab.plot(N_Solver.t, N_Solution[1])

    pylab.subplot(3, 3, 5)
    a_solve_3 = A_Solver.SolveY3(A_Solver.t)
    pylab.plot(A_Solver.t,  a_solve_3 / max(a_solve_3))

    pylab.subplot(3, 3, 6)
    points = A_Solver.rnd_points(A_Solver.SolveY3)
    pylab.scatter(x=points[0], y=points[1], marker='o', c='r', edgecolor='b')

    # SOLVE 3
    pylab.subplot(3, 3, 7)
    pylab.plot(N_Solver.t, N_Solution[2]/9)

    pylab.subplot(3, 3, 8)
    a_solve_5 = A_Solver.SolveY5(A_Solver.t)
    pylab.plot(A_Solver.t, a_solve_5 / max(a_solve_5))

    pylab.subplot(3, 3, 9)
    points = A_Solver.rnd_points(A_Solver.SolveY5)
    pylab.scatter(x=points[0], y=points[1], marker='o', c='r', edgecolor='b')

    pylab.show()


plot_all()