def program1311():
    import sys
    facto = [1]*21
    for i in range(1, 21):
        facto[i] = facto[i-1]*i
    n = int(sys.stdin.readline())
    print((facto[n] // (facto[n//2] * facto[n//2])) * facto[n//2-1] * facto[n//2-1] //2)