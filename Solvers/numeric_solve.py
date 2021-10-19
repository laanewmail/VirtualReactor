import pylab

from Solvers.base_class import *


class NumericSolution(Base_Class_For_all):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.y0 = [1, 1, 0]

    def odesystem(self, y,  t):  # , params
        y1, y3, y5 = y
        # y   z    x
        return [
            -self.k1 * y1 * y1,
            (self.k1 * y1 * y1 - self.k2 * y3 * y3) / 2,
            3 * self.k2 * y3 * y3
        ]

    #def nf_Solve(self, y0=None, t=None, max_step=2):  # y0 - начальные условия
    #   return solve_ivp(self.odesystem, t if t else self.t, y0 if y0 else self.y0 , max_step=max_step)

    def nf_Solve(self,  y0=None, t=None):  # y0 - начальные условия
        return odeint(self.odesystem, y0 if y0 else self.y0, t if t else self.t).T

    def arrenius(self, k0):
            return k0 * (math.e) ** (-self.E / (self.R * self.T))

    # #TODO: дорисовать про константу аррениуса
    # k0 = 1
    # T = np.linspace(300, 500, 100, dtype=int)
    # R = 8.314
    # E = 50
    #
    # def arrenius(T, k0, E):
    #     return k0 * (math.e) ** (-E / (R * T))
    #
    # plt.plot(T, arrenius(T, k0, E))
    # plt.show()

    def plot_Yi_t(self, t, yi):
        pylab.plot(t, yi)


# solution = NumericSolution()
# res = solution.nf_Solve()
# solution.plot_Yi_t(res.t, res.y[0])
# solution.plot_Yi_t(res.t, res.y[1])
# solution.plot_Yi_t(res.t, res.y[2]/9)
#
# pylab.show()

