import numpy as np
import math
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from pathlib import Path
from Settings.utils.readers import read_json

config_path = Path('..') / "Settings" / "config.json"
default_config = read_json(config_path)


class NumericSolution:
    k1 = default_config['k1']
    k2 = default_config['k2']
    C1 = default_config['C1']
    C2 = default_config['C2']
    C3 = default_config['C3']
    t = np.linspace(*default_config['t'])


print(NumericSolution)