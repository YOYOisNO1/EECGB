def program1880():
    
    n = int(input())
    
    numbers = list(map(int, input().split()))
    
    if all(numbers[x] == 0 for x in range(n)):
        print("NO")
    else:
        print("YES")
        if sum(numbers):
            print("1\n1 {}".format(n))
        else:
            i = 0
            while sum(numbers[0:i+1]) == 0:
                ++i
            print("2\n{} {}\n{} {}".format(1, i+1, i+2, n))
    
    