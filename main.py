from src.simple_iteration import SimpleIteration


def main() -> None:
    matrix_a: list[list[float]] = [[-0.1, 0.2, -0.1], [0.1, -0.2, -0.2], [-0.2, 0.1, -0.1]]
    matrix_b: list[float] = [1.6, -2.3, 1.5]
    simple_iteration = SimpleIteration(matrix_a, matrix_b, 0.01)
    print(simple_iteration.get_result())


if __name__ == '__main__':
    main()
