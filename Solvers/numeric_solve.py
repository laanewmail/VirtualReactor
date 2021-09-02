from pathlib import Path

import numpy as np
import math
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from Settings.utils.readers import read_json
import pylab

config_path = Path('..') / "Settings" / "config.json"
default_config = read_json(config_path)


class NumericSolution:

    def __init__(self):
        self.k1 = default_config['k1']
        self.k2 = default_config['k2']
        self.C1 = default_config['C1']
        self.C2 = default_config['C2']
        self.C3 = default_config['C3']
        self.t = np.linspace(*default_config['t'])

    def SolveY1(self):
        return 1 / (self.k1 * self.t + self.C1)

    def SolveY2(self):
        return 1 / (self.k1 * self.t + self.C1)

    def SolveY3(self):
        r1 = self.k1 / self.k2 + (self.k1 * (self.k2 + self.k1) ** (0.5)) / self.k2
        r2 = (self.k1 * (self.k2 + self.k1)) ** (0.5) / self.k2 - self.k1 / self.k2
        r3 = (self.C2 * (1 / (self.k1 * (self.t + self.C1)))) ** ((self.k1 + self.k2) ** (0.5) / self.k1 ** (0.5))
        return ((r1 + r2 * r3) * (1 / (self.k1 * (self.t + self.C1)))) / (1 - r3)

    def SolveY4(self):
        return self.SolveY3()
    
    def SolveY5(self):
        r1 = self.k1 / self.k2 + (self.k1 * (self.k2 + self.k1) ** (0.5)) / self.k2
        r2 = (self.k1 * (self.k2 + self.k1)) ** (0.5) / self.k2 - self.k1 / self.k2
        r3 = (self.C2 * (1 / (self.k1 * (self.t + self.C1)))) ** ((self.k1 + self.k2) ** (0.5) / self.k1 ** (0.5))
        return (self.C3 - 2 * (((r1 + r2 * r3) * (1 / (self.k1 * (self.t + self.C1)))) / (1 - r3)) - 1 / (self.k1 * self.t + self.C1)) * 3

    def plot_Yi_t(self, solver, i=1, norm=1.0):
        pylab.figure(i)
        pylab.plot(self.t, solver()/norm, label=f"Y{i}")


NumericSolution().plot_Yi_t(solver=NumericSolution().SolveY1, i=1, norm=1.0)
NumericSolution().plot_Yi_t(solver=NumericSolution().SolveY3, i=3, norm=2.5)
NumericSolution().plot_Yi_t(solver=NumericSolution().SolveY5, i=5, norm=17.5)
pylab.show()