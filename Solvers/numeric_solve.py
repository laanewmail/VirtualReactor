import pylab

from base_class import *


class NumericSolution(Base_Class_For_all):

    def __init__(self):
        super().__init__()
        self.y0 = [1, 1, 0]
        self.t = default_config['t'][0:2]

    def odesystem(self, t,  y):  # , params
        y1, y3, y5 = y
        # y   z    x
        return [
            -self.k1 * y1 * y1,
            (self.k1 * y1 * y1 - self.k2 * y3 * y3) / 2,
            3 * self.k2 * y3 * y3
        ]

    def nf_Solve(self, y0=None, t=None, max_step=0.1):  # y0 - начальные условия
        return solve_ivp(self.odesystem, t if t else self.t, y0 if y0 else self.y0 , max_step=max_step)

    def plot_Yi_t(self, t, yi):
        pylab.plot(t, yi)


solution = NumericSolution()
res = solution.nf_Solve()
solution.plot_Yi_t(res.t, res.y[0])
solution.plot_Yi_t(res.t, res.y[1])
solution.plot_Yi_t(res.t, res.y[2]/9)

pylab.show()

