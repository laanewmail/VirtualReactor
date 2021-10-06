from pathlib import Path
from Settings.utils.readers import read_json
from random import randint as rnd
from random import random
import numpy as np
from os import environ


def rnd_points(our_function, points_number, norm=1.0):
    default_config = read_json(environ.get('CONFIG_PATH'))
    t = default_config['t'][0:2]
    # x = sorted([rnd(*t) for i in range(points_number)])
    x = []
    for i in range(points_number):
        curr_n = rnd(*t)
        while curr_n in x:
            curr_n = rnd(*t)
        x.append(curr_n)
    x.sort()
    return np.array(x), [(our_function(xi)+our_function(xi)*(random()-0.5)/norm)/norm for xi in x]




