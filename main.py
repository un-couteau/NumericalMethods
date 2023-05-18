from src.euler import Euler


def main() -> None:
    a, b, c, d, l, m, n, p, q = 0, 8, 0, 6, 1, 9, 0, 3, 1
    h = 0.2
    euler = Euler(a, b, c, d, l, m, n, p, q, h)
    # print(euler.get_result())

    x_list, y_list = euler.get_result()
    for x, y in zip(x_list, y_list):
        print(f"x= {round(x, 1)}\t\ty= {round(y, 1)}")


if __name__ == '__main__':
    main()
