def program1101():
    import bisect 
    bits = []
    for i in range(1, 513):
      bits.append(int(format(i, "b")))
    n = int(input())
    print(bisect.bisect_right(bits, n))