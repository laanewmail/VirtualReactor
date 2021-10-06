from Solvers.base_class import *


class AnalitSolution(Base_Class_For_all):

    # def __init__(self):
    #     self.k1 = default_config['k1']
    #     self.k2 = default_config['k2']
    #     self.C1 = default_config['C1']
    #     self.C2 = default_config['C2']
    #     self.C3 = default_config['C3']
    #     self.t = np.linspace(*default_config['t'])

    def SolveY1(self, param_t):
        return 1 / (self.k1 * param_t + self.C1)

    def SolveY2(self, param_t):
        return 1 / (self.k1 * param_t + self.C1)

    def SolveY3(self, param_t):
        r1 = self.k1 / self.k2 + (self.k1 * (self.k2 + self.k1) ** (0.5)) / self.k2
        r2 = (self.k1 * (self.k2 + self.k1)) ** (0.5) / self.k2 - self.k1 / self.k2
        r3 = (self.C2 * (1 / (self.k1 * (param_t + self.C1)))) ** ((self.k1 + self.k2) ** (0.5) / self.k1 ** (0.5))
        return ((r1 + r2 * r3) * (1 / (self.k1 * (param_t + self.C1)))) / (1 - r3)

    def SolveY4(self, param_t):
        return self.SolveY3(param_t)
    
    def SolveY5(self, param_t):
        r1 = self.k1 / self.k2 + (self.k1 * (self.k2 + self.k1) ** (0.5)) / self.k2
        r2 = (self.k1 * (self.k2 + self.k1)) ** (0.5) / self.k2 - self.k1 / self.k2
        r3 = (self.C2 * (1 / (self.k1 * (param_t + self.C1)))) ** ((self.k1 + self.k2) ** (0.5) / self.k1 ** (0.5))
        return (self.C3 - 2 * (((r1 + r2 * r3) * (1 / (self.k1 * (param_t + self.C1)))) / (1 - r3)) - 1 / (self.k1 * param_t + self.C1)) * 3

    def plot_Yi_t(self, solver, i=1, norm=1.0):
        pylab.figure(i)
        pylab.plot(self.t, solver(self.t)/norm, label=f"Y{i}")

    def plot_Yi_with_rnd_points(self, solver, points_number, norm):
        points = rnd_points(solver, points_number, norm)

        fig, ax = plt.subplots(
            nrows=1, ncols=1,
            figsize=(8, 4)
        )
        ax.scatter(x=points[0], y=points[1], marker='o', c='r', edgecolor='b')
        ax.set_title(solver.__name__)
        ax.set_xlabel('$t$')
        ax.set_ylabel('$Yi(t) + rnd$')


# Solution = AnalitSolution()
#
# Solution.plot_Yi_t(solver=Solution.SolveY1, i=1, norm=1.0)
# Solution.plot_Yi_t(solver=Solution.SolveY3, i=3, norm=2.5)
# Solution.plot_Yi_t(solver=Solution.SolveY5, i=5, norm=18.0)
#
# Solution.plot_Yi_with_rnd_points(solver=Solution.SolveY1, points_number=50, norm=1.0)
# Solution.plot_Yi_with_rnd_points(solver=Solution.SolveY3, points_number=50, norm=2.5)
# Solution.plot_Yi_with_rnd_points(solver=Solution.SolveY5, points_number=50, norm=18.0)
#
# plt.show()