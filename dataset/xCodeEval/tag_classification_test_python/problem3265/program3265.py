def play_off(n):
        h=2**n
        return h-1
    
    t=int(input())
    for i in range(t):
        n=int(input())
        print(play_off(n))