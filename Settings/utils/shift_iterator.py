from Settings.utils.readers import read_json
from random import randint as rnd
from random import random
import numpy as np
from os import environ


class ShiftIterator:
    points_range = None
    points = []

    def __init__(self, func):
        self.points_range = read_json(environ.get('CONFIG_PATH'))['t'][0:2]

    def _generate_points(self, n):
        for i in range(n):
            curr_point = rnd(*self.points_range)
            while curr_point in self.points:
                curr_point = rnd(*self.points_range)
            self.points.append(curr_point)
        self.points.sort()

    def calculate_shift_single(self, our_function, points_number, norm):
        self._generate_points(points_number)
        function_values = [our_function(x) for x in self.points]
        shifted_function_values = [(our_function(x)+our_function(xi)*(random()-0.5)/norm)/norm for xi in x]
