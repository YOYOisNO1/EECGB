def program3657():
    from math import ceil
    
    n, a = [float(v) for v in input().split()]
    exp2 = -9 * n ** 2 + 27 * n - 21
    exp1 = (
        -54 * a * n ** 3
        + 162 * a * n ** 2
        + (
            (
                -54 * a * n ** 3
                + 162 * a * n ** 2
                - 108 * a * n
                + 81 * n ** 2
                - 243 * n
                + 162
            )
            ** 2
            + 4 * exp2 ** 3
        )
        ** 0.5
        - 108 * a * n
        + 81 * n ** 2
        - 243 * n
        + 162
    ) ** (1 / 3)
    p1 = -((2 ** (1 / 3) * exp2) / (3 * exp1)) + 1 / (3 * 2 ** (1 / 3)) * exp1 + 1
    p2 = (
        (complex(1, 3 ** 0.5) * exp2) / (3 * 2 ** (2 / 3) * exp1)
        - 1 / (6 * 2 ** (1 / 3)) * complex(1, -(3 ** (0.5))) * exp1
        + 1
    )
    p3 = (
        (complex(1, -(3 ** 0.5)) * exp2) / (3 * 2 ** (2 / 3) * exp1)
        - 1 / (6 * 2 ** (1 / 3)) * complex(1, 3 ** (0.5)) * exp1
        + 1
    )
    # print(min(round(abs(p1)), round(abs(p2)), round(abs(p3))))
    p1 = round(abs(p1)) if abs(p1) - int(abs(p1)) < 0.01 else ceil(abs(p1))
    p2 = round(abs(p2)) if abs(p2) - int(abs(p2)) < 0.01 else ceil(abs(p2))
    p3 = round(abs(p3)) if abs(p3) - int(abs(p3)) < 0.01 else ceil(abs(p3))
    
    print(min(p1, p2, p3))