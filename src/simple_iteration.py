import numpy as np

class SimpleIteration:
    def __init__(self, matrix_a: list[list[float]], matrix_b: list[float], eps: float = 0.0001) -> None:
        self._matrix_a = matrix_a
        self._matrix_size: int = len(matrix_a) - 1 # Потому что в range идет счёт с 0
        self._matrix_b = matrix_b
        self._abs_sum_list: list[float] = []
        self._eps = eps

    def _norm(self) -> float:
        for row in range(self._matrix_size):
            abs_sum: float = 0
            for col in range(self._matrix_size):
                abs_sum += abs(self._matrix_a[row][col])
            self._abs_sum_list.append(abs_sum)

        max_sum: float = 0
        for i in range(self._matrix_size):
            max_sum = self._abs_sum_list[i] if self._abs_sum_list[i] > max_sum else max_sum
        print(f"{max_sum=}")
        return max_sum

    def _max(self, delta_x) -> float:
        max_value: float = 0

        for i in range(self._matrix_size):
            max_value = abs(delta_x)[i] if max_value < abs(delta_x)[i] else max_value
        print(f"{max_value=}")
        return max_value

    def get_result(self):
        norm = self._norm()
        q: float = norm
        x_0: list[float] = self._matrix_b

        while True:
            m_x = np.dot(self._matrix_a, x_0) + self._matrix_b
            delta_x = m_x - x_0
            delta = self._max(delta_x)
            if (delta * q / (1 - q)) < self._eps:
                return x_0

    def __str__(self):
        return f"Result: {self._result}"