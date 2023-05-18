from copy import copy
from numpy import array
from .simple_iteration import SimpleIteration


class Zeidel(SimpleIteration):
    def __init__(self, matrix_a: list[list[float]], matrix_b: list[float], eps: float = 0.0001) -> None:
        super().__init__(matrix_a, matrix_b)

    def get_result(self):
        q: float = self._norm()

        m_x: list[float] = [0.0 for _ in range(self._matrix_size)]

        x_0: list[float] = copy(self._matrix_b)

        flag: bool = True
        while flag:
            for i in range(self._matrix_size):
                temp: float = 0
                for j in range(self._matrix_size):
                    temp += x_0[j] * self._matrix_a[i][j]
                x_0[i] = temp + self._matrix_b[i]

            delta_x = array(x_0) - array(m_x)
            delta = self._max(delta_x)

            if (delta * q / (1 - q)) < self._eps:
                flag = False

            m_x = copy(x_0)
            self._iterations += 1

            if not flag: return x_0
