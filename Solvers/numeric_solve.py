from os import environ as env
from random import randint as rnd
from random import random

import numpy as np
from scipy.integrate import odeint

from Settings.utils.readers import read_json


class NumericSolution:
    default_config = read_json(env.get('CONFIG_PATH'))

    def __init__(self, time=None):
        self.k1 = self.default_config['k1']
        self.k2 = self.default_config['k2']
        self.t = np.linspace(*self.default_config['t']) if time is None else time
        self.y0 = [1, 1, 0]
        self.generate_rnd_time()

    def odesystem(self, y, t):  # , params
        y1, y3, y5 = y
        # y   z    x
        return [
            -self.k1 * y1 * y1,
            (self.k1 * y1 * y1 - self.k2 * y3 * y3) / 2,
            3 * self.k2 * y3 * y3
        ]

    def nf_Solve(self, y0=None, t=None):  # y0 - начальные условия
        return odeint(self.odesystem, y0 if y0 else self.y0, t if t else self.t).T

    def generate_rnd_time(self):
        x = []
        for i in range(self.default_config.get("rnd_points_number", 50)):
            curr_n = self.t[rnd(0, len(self.t) - 1)]
            while curr_n in x:
                curr_n = self.t[rnd(0, len(self.t) - 1)]
            x.append(curr_n)
        x.sort()
        self.rnd_time = x

    def get_time_indexes(self):
        return [tuple(self.t).index(time) for time in self.rnd_time]

    def rnd_points(self, num_solution):

        rnd_indexes = self.get_time_indexes()
        result = []
        for solution in num_solution:
            solution_delta = []
            for index in rnd_indexes:
                delta = solution[index] * (random() - 0.5) / max(solution)
                val = solution[index] + delta
                solution_delta.append(val)
            max_val = max(solution)
            solution_delta = [obj / max_val for obj in solution_delta]
            result.append(solution_delta)
        return np.array(self.rnd_time), result

        # max_val = max([our_function(x) for x in self.t])
        # return np.array(self.rnd_time), [(our_function(xi) + our_function(xi) * (random() - 0.5) / max_val) / max_val
        #                                  for xi in self.rnd_time]
