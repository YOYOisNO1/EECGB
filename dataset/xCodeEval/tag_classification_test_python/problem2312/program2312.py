    # enumerate range float sorted reversed
def print_ints(a):
        print(' ').join(map(str, a))
    
    read_ints = lambda: map(int, input().strip().split())
    read_floats= lambda: map(float, input().strip().split())
    n = int(input())
    c = 0
    c += n/100
    n %= 100
    c += n/20
    n %= 20
    c += n/10
    n %= 10
    c += n/5
    n %= 5
    c += n
    print(c)