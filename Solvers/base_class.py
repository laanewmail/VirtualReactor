from pathlib import Path

import numpy as np
import math
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from Settings.utils.readers import read_json
from Settings.utils.rnd_points import rnd_points
import pylab
from os import environ

default_config = read_json(environ.get('CONFIG_PATH'))


class Base_Class_For_all:

    def __init__(self):
        self.k1 = default_config['k1']
        self.k2 = default_config['k2']
        self.C1 = default_config['C1']
        self.C2 = default_config['C2']
        self.C3 = default_config['C3']
        self.t = np.linspace(*default_config['t'])