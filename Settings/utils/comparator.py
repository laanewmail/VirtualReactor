from copy import deepcopy

import numpy as np
import pylab

from Solvers.analit_solve import AnalitSolution
from Solvers.numeric_solve import NumericSolution


class Comparator:
    # TODO: аналитическое решение для результатов эксперимента это временная мера
    analit_solver = None
    experiment_results = None  # это должно быть зафиксировано для всех вычислений numeric_solution

    numeric_solver = None  # система численного решения, где будем менять k1, k2
    numeric_solution = None  # здесь будут лежать результаты вычислений численой системы для фикс. к1, к2

    def __init__(self):
        self.analit_solver = AnalitSolution()
        self.numeric_solver = NumericSolution(time=self.analit_solver.t)

    def _get_time_indexes(self):
        return [tuple(self.numeric_solver.t).index(t) for t in self.analit_solver.rnd_time]

    def generate_experiment_results(self):
        self.experiment_results = [self.analit_solver.rnd_points(our_function=func)
                                   for func in [self.analit_solver.SolveY1,
                                                self.analit_solver.SolveY3,
                                                self.analit_solver.SolveY5]
                                   ]

    def calculate_single_k(self, k1: float = None, k2: float = None):
        self.numeric_solver.k1 = k1 if k1 is not None else self.numeric_solver.k1
        self.numeric_solver.k2 = k2 if k2 is not None else self.numeric_solver.k2

        self.numeric_solution = self.numeric_solver.nf_Solve()

        tmp_numeric_solution = []
        rnd_time_indexes = self._get_time_indexes()
        for y in self.numeric_solution:
            tmp_numeric_solution.append([y[i] / max(y) for i in rnd_time_indexes])

        shift = []
        for i, n_solution in enumerate(tmp_numeric_solution):
            shift.append(abs(np.array(n_solution) - np.array(self.experiment_results[i][1])))

        return {'shift': sum(sum(shift)), 'numeric_solution': deepcopy(self.numeric_solution)}

    def calculate_range_k(self, k1_range, k2_range):
        operation_id = 0
        min_shift = {'k1': self.numeric_solver.k1,
                     'k2': self.numeric_solver.k2,
                     **self.calculate_single_k(self.numeric_solver.k1, self.numeric_solver.k2)}
        print(f"{operation_id}) K:({min_shift['k1']}, {min_shift['k2']}) ;  SHIFT: {min_shift['shift']}")

        matching_shifts = []

        for k1 in k1_range:
            for k2 in k2_range:
                operation_id += 1
                curr_shift = {'k1': k1,
                              'k2': k2,
                              **self.calculate_single_k(k1, k2)}
                print(f"{operation_id}) K:({curr_shift['k1']}, {curr_shift['k2']}) ;  SHIFT: {curr_shift['shift']}")

                if curr_shift['shift'] < min_shift['shift']:
                    min_shift = curr_shift
                    matching_shifts = []
                elif curr_shift['shift'] == min_shift['shift']:
                    matching_shifts.append(curr_shift)

        print(f"(all) MIN SHIFT: {min_shift}")
        print(f"(all) MATCHING_SHIFTS: {matching_shifts}")
        print(operation_id)
        self._plot_numeric_solution_with_rnd_points(min_shift, f'All points ({operation_id} points)')
        return min_shift

    def calculate_hilbert(self, k1_range, k2_range, x_power=5):
        operation_id = 0
        min_shift = {'k1': self.numeric_solver.k1,
                     'k2': self.numeric_solver.k2,
                     **self.calculate_single_k(self.numeric_solver.k1, self.numeric_solver.k2)}
        print(f"{operation_id}) K:({min_shift['k1']}, {min_shift['k2']}) ;  SHIFT: {min_shift['shift']}")

        matching_shifts = []

        k1_i_range = [k for i, k in enumerate(np.linspace(*k1_range, pow(2, x_power + 1) + 1)) if i % 2 != 0]
        k2_i_range = [k for i, k in enumerate(np.linspace(*k2_range, pow(2, x_power + 1) + 1)) if i % 2 != 0]

        for k1 in k1_i_range:
            for k2 in k2_i_range:
                operation_id += 1
                curr_shift = {'k1': k1,
                              'k2': k2,
                              **self.calculate_single_k(k1, k2)}
                print(f"{operation_id}) K:({curr_shift['k1']}, {curr_shift['k2']}) ;  SHIFT: {curr_shift['shift']}")

                if curr_shift['shift'] < min_shift['shift']:
                    min_shift = curr_shift
                    matching_shifts = []
                elif curr_shift['shift'] == min_shift['shift']:
                    matching_shifts.append(curr_shift)

        print(f"(hilbert) MIN SHIFT: {min_shift}")
        print(f"(hilbert) MATCHING_SHIFTS: {matching_shifts}")
        print(operation_id)
        self._plot_numeric_solution_with_rnd_points(min_shift, f'Hilbert ({operation_id} points, X_power = {x_power})')
        return min_shift

    def _plot_numeric_solution_with_rnd_points(self, shift_obj, window_name='Window'):
        # pylab.ion()
        fig = pylab.gcf()
        fig.canvas.set_window_title(window_name)
        pylab.subplot(1, 3, 1)
        pylab.plot(self.numeric_solver.t, shift_obj['numeric_solution'][0] / max(shift_obj['numeric_solution'][0]))
        pylab.scatter(x=self.experiment_results[0][0], y=self.experiment_results[0][1], marker='o', c='r',
                      edgecolor='b')

        pylab.subplot(1, 3, 2)
        pylab.title(f"K1: {shift_obj['k1']}, K2: {shift_obj['k2']}, SHIFT: {shift_obj['shift']}")
        pylab.plot(self.numeric_solver.t, shift_obj['numeric_solution'][1] / max(shift_obj['numeric_solution'][1]))
        pylab.scatter(x=self.experiment_results[1][0], y=self.experiment_results[1][1], marker='o', c='r',
                      edgecolor='b')

        pylab.subplot(1, 3, 3)
        pylab.plot(self.numeric_solver.t, shift_obj['numeric_solution'][2] / max(shift_obj['numeric_solution'][2]))
        pylab.scatter(x=self.experiment_results[2][0], y=self.experiment_results[2][1], marker='o', c='r',
                      edgecolor='b')
        pylab.show()
        # pylab.pause(1)
        # pylab.close()


comparator = Comparator()

comparator.generate_experiment_results()
k1_range = [comparator.numeric_solver.k1 * 0.001, comparator.numeric_solver.k1 * 4.999]

k2_range = [comparator.numeric_solver.k2 * 0.001, comparator.numeric_solver.k2 * 4.999]

k1_range_linspace = np.linspace(*k1_range, 20)
k2_range_linspace = np.linspace(*k2_range, 20)

# TODO: добавить рекурсивные разбиения
# TODO: привести параметры к одному виду
min_all_points = comparator.calculate_range_k(k1_range_linspace, k2_range_linspace)
min_hilbert_points = comparator.calculate_hilbert(k1_range, k2_range, 3)

min_all_points.pop('numeric_solution')
min_hilbert_points.pop('numeric_solution')

print(f"MIN_ALL_POINTS: {min_all_points}")
print(f"MIN_HILBERT_POINTS: {min_hilbert_points}")
