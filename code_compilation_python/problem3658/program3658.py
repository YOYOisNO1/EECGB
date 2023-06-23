def program3658():
    n, a = [int(v) for v in input().split()]
    exp2 = -9 * n ** 2 + 45 * n - 57
    exp1 = (
        108 * a * n ** 3
        - 324 * a * n ** 2
        + (
            (
                108 * a * n ** 3
                - 324 * a * n ** 2
                + 216 * a * n
                - 54 * n ** 3
                - 81 * n ** 2
                + 783 * n
                - 810
            )
            ** 2
            + 4 * exp2 ** 3
        )
        ** 0.5
        + 216 * a * n
        - 54 * n ** 3
        - 81 * n ** 2
        + 783 * n
        - 810
    ) ** (1 / 3)
    p1 = round(
        abs(1 / (3 * 2 ** (1 / 3)) * exp1 - (2 ** (1 / 3) * exp2) / (3 * exp1) + 2 * n - 3)
    )
    p2 = round(
        abs(
            -1 / (6 * 2 ** (1 / 3)) * complex(1, 3 ** 0.5) * exp1
            + complex(1, -(3 ** 0.5)) * exp2 / (3 * 2 ** (2 / 3) * exp1)
            + 2 * n
            - 3
        )
    )
    p3 = round(
        abs(
            -1 / (6 * 2 ** (1 / 3)) * complex(1, -(3 ** 0.5)) * exp1
            + complex(1, (3 ** 0.5)) * exp2 / (3 * 2 ** (2 / 3) * exp1)
            + 2 * n
            - 3
        )
    )
    print(min(p1, p2, p3))