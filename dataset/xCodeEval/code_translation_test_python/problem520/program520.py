def program520():
    import math
    s1, s2, s3=map(int,input().split())
    a = math.sqrt(s1 * s2 / s3)
    b = math.sqrt(s3 * s1 / s2)
    c = math.sqrt(s3 * s2 / s1)
    sum = a + b + c
    print(int(4 * sum))