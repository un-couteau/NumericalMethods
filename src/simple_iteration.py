import numpy as np


class SimpleIteration:
    def __init__(self, matrix_a: list[list[float]], matrix_b: list[float], eps: float = 0.0001) -> None:
        self.__matrix_a = matrix_a
        self.__matrix_a_len: int = len(matrix_a)
        self.__matrix_b = matrix_b if len(matrix_b) == self.__matrix_a_len else matrix_b.append(0)
        self.__abs_sum_list: list[float] = []
        self.__eps = eps

    def __norm(self) -> float:
        for row in range(self.__matrix_a_len):
            abs_sum: float = 0
            for col in range(self.__matrix_a_len):
                abs_sum += abs(self.__matrix_a_len[row][col])
            self.__abs_sum_list.append(abs_sum)

        max_sum: float = 0
        for i in range(self.__matrix_a_len):
            max_sum = self.__abs_sum_list[i] if self.__abs_sum_list[i] > max_sum else max_sum
        return max_sum

    def __max(self, delta_x):
        max_value: float = 0

        for i in range(self.__matrix_a_len):
            max_value = abs(delta_x)[i] if max_value < abs(delta_x)[i] else max_value
        return max_value

    def get_result(self):
        q: float = self.__norm()
        x_0: list[float] = self.__matrix_b

        while True:
            m_x = np.dot(self.__matrix_a, self.__matrix_b) + self.__matrix_b
            delta_x = m_x - x_0
            delta = self.__max(delta_x)
            if (delta * q / (1 - q)) < self.__eps:
                return x_0
