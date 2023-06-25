def program349():
    n = int (input ())
    m = n // 10000 * 10000 + n // 100 % 10 * 1000 + n % 10 * 100 + n % 100 // 10 * 10 + n // 1000 % 10
    m = m ** 5
    first = m // 10000 % 10
    second = m // 1000 % 10
    third = m // 100 % 10
    fourth = m // 10 % 10
    fifth = m % 10
    print((str) (first) + str (second) + str (third) + str (fourth) + str (fifth))