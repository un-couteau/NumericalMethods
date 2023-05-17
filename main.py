import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.log(x) ** (9 / 5)


x = np.array([9, 12, 15])
a = 11.5


def divided_differences(x, y):
    n = len(x)
    F = np.zeros((n, n))
    F[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            F[i, j] = (F[i + 1, j - 1] - F[i, j - 1]) / (x[i + j] - x[i])

    return F[0, :]


y = f(x)
coefficients = divided_differences(x, y)


def newton_polynomial(x, coefficients, nodes):
    n = len(nodes)
    result = coefficients[0]

    for i in range(1, n):
        term = coefficients[i]
        for j in range(i):
            term *= (x - nodes[j])
        result += term

    return result


p_a = newton_polynomial(a, coefficients, x)

x_values = np.linspace(x[0], x[2], 100)
y_values_f = f(x_values)
y_values_p = newton_polynomial(x_values, coefficients, x)

plt.plot(x_values, y_values_f, label='f(x)')
plt.plot(x_values, y_values_p, label='Полином Ньютона')
plt.scatter(x, y, color='red', label='Узлы интерполяции')
plt.scatter(a, p_a, color='green', label='Значение полинома в точке a')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция полиномом Ньютона')
plt.show()

exact_error = f(a) - p_a

print('Значение функции f(x) в точке a:', f(a))
print('Значение полинома Ньютона в точке a:', p_a)
print('Погрешность интерполяции:', exact_error)
