from Solvers.base_class import *
from random import randint as rnd
from random import random


class AnalitSolution(Base_Class_For_all):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.generate_rnd_time()

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

    def plot_Yi_with_rnd_points(self, solver, norm):
        points = self.rnd_points(solver)

        fig, ax = plt.subplots(
            nrows=1, ncols=1,
            figsize=(8, 4)
        )
        ax.scatter(x=points[0], y=points[1], marker='o', c='r', edgecolor='b')
        ax.set_title(solver.__name__)
        ax.set_xlabel('$t$')
        ax.set_ylabel('$Yi(t) + rnd$')

    def generate_rnd_time(self):
        x = []
        for i in range(default_config.get("rnd_points_number", 50)):
            curr_n = self.t[rnd(0, len(self.t) - 1)]
            while curr_n in x:
                curr_n = self.t[rnd(0, len(self.t) - 1)]
            x.append(curr_n)
        x.sort()
        self.rnd_time = x

    def rnd_points(self, our_function):
        max_val = max([our_function(x) for x in self.t])
        return np.array(self.rnd_time), [(our_function(xi)+our_function(xi)*(random()-0.5)/max_val)/max_val for xi in self.rnd_time]

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