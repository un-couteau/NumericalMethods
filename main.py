from src.simple_iteration import SimpleIteration
from src.zeidel import Zeidel


def main() -> None:
    matrix_a: list[list[float]] = [[-0.1, 0.2, -0.1], [0.1, -0.2, -0.2], [-0.2, 0.1, -0.1]]
    matrix_b: list[float] = [1.6, -2.3, 1.5]

    simple_iteration = SimpleIteration(matrix_a, matrix_b)
    zeidel = Zeidel(matrix_a, matrix_b)
    # print(simple_iteration.get_result())
    # print(zeidel.get_result())

    for smpl_itr, zeid in zip(simple_iteration.get_result(), zeidel.get_result()):
        print(f"Simple= {round(smpl_itr, 10)}\tZeidel= {round(zeid, 10)}")

    # print(f"{simple_iteration.get_iterations()=}\t{zeidel.get_iterations()=}")


if __name__ == '__main__':
    main()
