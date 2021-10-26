import numpy as np

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

    def calculate_single_k(self, k1: float = None, k2: float = None):
        self.numeric_solver.k1 = k1 if k1 is not None else self.numeric_solver.k1
        self.numeric_solver.k2 = k2 if k2 is not None else self.numeric_solver.k2

        self.numeric_solution = self.numeric_solver.nf_Solve()

        # TODO: в общем случае аналитическое решение для шума не используется,
        #  такая реализация временная для демоснтрации
        self.analit_solver.k1 = self.numeric_solver.k1
        self.analit_solver.k2 = self.numeric_solver.k2

        self.experiment_results = [self.analit_solver.rnd_points(our_function=func, norm=norm)
                                  for func, norm in [(self.analit_solver.SolveY1, 1.0),
                                                     (self.analit_solver.SolveY3, 2.5),
                                                     (self.analit_solver.SolveY5, 18.0)]
                                  ]

        tmp_numeric_solution = []
        rnd_time_indexes = self._get_time_indexes()
        for y in self.numeric_solution:
            tmp_numeric_solution.append([y[i] for i in rnd_time_indexes])

        shift = []
        for i, n_solution in enumerate(tmp_numeric_solution):
            shift.append(abs(np.array(n_solution) - np.array(self.experiment_results[i][1])))

        return sum(sum(shift))

    def calculate_range_k(self, k1_range, k2_range):
        min_shift = {'k1': self.numeric_solver.k1,
                     'k2': self.numeric_solver.k2,
                     'shift': self.calculate_single_k(self.numeric_solver.k1, self.numeric_solver.k2)}
        print(f"K:({min_shift['k1']}, {min_shift['k2']}) ;  SHIFT: {min_shift['shift']}")

        matching_shifts = []

        for k1 in k1_range:
            for k2 in k2_range:
                curr_shift = {'k1': k1,
                              'k2': k2,
                              'shift': self.calculate_single_k(k1, k2)}
                print(f"K:({curr_shift['k1']}, {curr_shift['k2']}) ;  SHIFT: {curr_shift['shift']}")

                if curr_shift['shift'] < min_shift['shift']:
                    min_shift = curr_shift
                    matching_shifts = []
                elif curr_shift['shift'] == min_shift['shift']:
                    matching_shifts.append(curr_shift)

        print(f"MIN SHIFT: {min_shift}")
        print(f"MATCHING_SHIFTS: {matching_shifts}")


comparator = Comparator()

k1_range = np.linspace(comparator.numeric_solver.k1 - comparator.numeric_solver.k1 * 0.999,
                       comparator.numeric_solver.k1 + comparator.numeric_solver.k1 * 0.999,
                       100)
k2_range = np.linspace(comparator.numeric_solver.k2 - comparator.numeric_solver.k2 * 0.999,
                       comparator.numeric_solver.k2 + comparator.numeric_solver.k2 * 0.999,
                       100)

comparator.calculate_range_k(k1_range, k2_range)