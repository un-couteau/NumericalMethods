import numpy as np
import matplotlib.pyplot as plt
from math import log

def f(x):
    return (log(x))**(9/7)

x = [9, 12, 15]
y = [f(x[0]), f(x[1]), f(x[2])]

coefficients = np.polyfit(x, y, len(x) - 1)

lagrange_poly = np.poly1d(coefficients)

a = 11.5
lagrange_value = lagrange_poly(a)

x_values = np.linspace(x[0], x[2], 100)
f_values = [f(x) for x in x_values]

lagrange_values = lagrange_poly(x_values)

plt.plot(x_values, lagrange_values, label='Полином Лагранжа')
plt.plot(x_values, f_values, label='f(x)')
plt.scatter(x, y, color='red', label='Узлы интерполяции')
plt.scatter(a, lagrange_value, color='green', label='Значение полинома в точке a')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция полиномом Лагранжа')
plt.grid(True)
plt.show()

exact_value = f(a)

interpolation_error = abs(exact_value - lagrange_value)

print("Значение функции f(x) в точке a:", exact_value)
print("Значение полинома Лагранжа в точке a:", lagrange_value)
print("Погрешность интерполяции:", interpolation_error)
