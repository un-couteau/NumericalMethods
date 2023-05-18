import math


class Euler:
    def __init__(self, a: int, b: int, c: int, d: int, l: int, m: int, n: int, p: int, q: int, h: float) -> None:
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._l = l
        self._m = m
        self._n = n
        self._p = p
        self._q = q

        self._h = h

        self._y = 1.0
        self._x = 0.0
        self._y_list: list[float | int] = []
        self._x_list: list[float | int] = []

    def y(self) -> float:
        return math.pow(-1, self._n + self._p + self._q) * float(f"{self._a}.{self._b}") * self._y + float(
            f"{self._c}.{self._d}") * math.pow(self._x, 2) + float(f"{self._l}.{self._m}")

    def get_result(self):
        while self._x <= 2:
            self._y_list.append(self._y)
            self._x_list.append(self._x)

            value: float = self.y()

            self._y += self._h * value
            self._x += self._h

        return self._x_list, self._y_list
