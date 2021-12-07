from tkinter import *
import numpy as np
from Settings.utils.comparator import Comparator

comparator = Comparator()

pass
# comparator.generate_experiment_results()
k1_range = [comparator.numeric_solver.k1 * 0.001, comparator.numeric_solver.k1 * 1.999]

k2_range = [comparator.numeric_solver.k2 * 0.001, comparator.numeric_solver.k2 * 1.999]

k1_range_linspace = np.linspace(*k1_range, 50)
k2_range_linspace = np.linspace(*k2_range, 50)

# TODO: добавить рекурсивные разбиения
# TODO: привести параметры к одному виду
min_all_points = comparator.calculate_range_k(k1_range_linspace, k2_range_linspace)
min_hilbert_points = comparator.calculate_hilbert(k1_range, k2_range, 5)

min_all_points.pop('numeric_solution')
min_hilbert_points.pop('numeric_solution')

print(f"MIN_ALL_POINTS: {min_all_points}")
print(f"MIN_HILBERT_POINTS: {min_hilbert_points}")

## WINDOW ##
window = Tk()
window.title("Сравнение методов")

label_all = Label(window, text=f"ALL: {min_all_points.__str__()}", font='Times 16')
label_all.grid(row=0, column=0)

label_hilbert = Label(window, text=f"HILBERT: {min_hilbert_points.__str__()}", font='Times 16')
label_hilbert.grid(row=1, column=0)

window.mainloop()
