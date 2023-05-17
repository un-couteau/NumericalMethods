from numpy import array
from simple_iteration import SimpleIteration
from copy import copy
class Zeidel(SimpleIteration):
    def __init__(self, matrix_a: list[list[float]], matrix_b: list[float]) -> None:
        super.__init__()
        super().__init__(matrix_a, matrix_b)

    def get_result(self):
        q: float = self._norm()

        m_x: list[float] = [0.0 for _ in range(self._matrix_size)]

        iterations: int = 0
        x_0: list[float] = copy(self._matrix_b)

        while True:
            for i in range(self._matrix_size):
                for j in range(self._matrix_size):
                    x_0[i] = x_0[]
                # for_append: float = 0

                # x_0[i] = x_0[0] * self._matrix_b[i][0] + x_0[]
                # for j in range(self._matrix_a_len):
                #     x_0[i] = x_0[i] * self._matrix_b[i]
                # ...

