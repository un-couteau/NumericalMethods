from .euler import Euler


class RungeKutty(Euler):
    def get_result(self):
        while self._x <= 2:
            self._y_list.append(self._y)
            self._x_list.append(self._x)

            k1 = self._h * self.f()
            k2 = self._h * self.f(self._x + 0.5 * self._h, self._y + 0.5 * k1)
            k3 = self._h * self.f(self._x + 0.5 * self._h, self._y + 0.5 * k2)
            k4 = self._h * self.f(self._x + self._h, self._y + k3)

            self._y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
            self._x += self._h
        return self._x_list, self._y_list
