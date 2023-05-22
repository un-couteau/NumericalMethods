from src.euler import Euler
from src.runge_kutty import RungeKutty


def main() -> None:
    a, b, c, d, l, m, n, p, q = 0, 8, 0, 6, 1, 9, 0, 3, 1
    # a, b, c, d, l, m, n, p, q = 0, 888, 0, 666, 111, 999, 0, 333, 111
    h = 0.2
    euler = Euler(a, b, c, d, l, m, n, p, q, h)
    # print(euler.get_result())
    runge_kutty = RungeKutty(a, b, c, d, l, m, n, p, q, h)

    euler_x_list, euler_y_list = euler.get_result()
    runge_kutty_x_list, runge_kutty_y_list = runge_kutty.get_result()

    def print_nice(x_list, y_list, message: str | None = None):
        if message is not None:
            print(message)
        for x, y in zip(x_list, y_list):
            print(f"x = {round(x, 1)}\ty = {round(y, 7)}")

    print_nice(euler_x_list, euler_y_list, "Метод Эйлера:")
    print_nice(runge_kutty_x_list, runge_kutty_y_list, "Метод Рунги-Кутти 4 порядка:")


if __name__ == '__main__':
    main()
