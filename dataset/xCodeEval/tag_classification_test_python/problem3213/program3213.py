def program3213():
    from fractions import Fraction
    a = int(input())
    ans = 0
    for i in range(2,a):
        b = a
        while b != 0:
            ans += b % i
            b //= i
    ans = Fraction(ans, a-2)
    print(ans if ans.denominator != 1 else str(ans.numerator) + "/1")