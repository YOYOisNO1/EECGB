def program1436():
    import functools
    
    (n, m) = [int(x) for x in input().split(" ")]
    arr = [int(x) for x in input().split(" ")]
    last = 0
    
    while True:
        end = False
        was = False
        for i in range(len(arr)):
            if arr[i] > 0:
                if arr[i] - m <= 0:
                    last = i + 1
                    arr[i] -= m
                else:
                    arr[i] -= m
                was = True
    
        if not was:
            print(last)
            break