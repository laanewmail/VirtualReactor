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

    def calculate(self, k1: float = None, k2: float = None):
        self.numeric_solver.k1 = k1 if k1 is not None else self.numeric_solver.k1
        self.numeric_solver.k2 = k2 if k2 is not None else self.numeric_solver.k2

        self.numeric_solution = self.numeric_solver.nf_Solve()

        # TODO: в общем случае аналитическое решение для шума не используется,
        #  такая реализация временная для демоснтрации
        self.analit_solver.k1 = self.numeric_solver.k1
        self.analit_solver.k2 = self.numeric_solver.k2

        tmp_experiment_results = [self.analit_solver.rnd_points(our_function=func, norm=norm)
                                  for func, norm in [(self.analit_solver.SolveY1, 1.0),
                                                     (self.analit_solver.SolveY3, 2.5),
                                                     (self.analit_solver.SolveY5, 18.0)]
                                  ]
        # self.experiment_results = dict(zip(
        #     [t for t,_ in ], []
        # ))

