def program4001():
    n, m, l, r = map(int , input().split())
    a = list(map(int , input().split()))
    if max(x) > r or  min(a) < l:
        print("Incorrect")
    elif n - m >= 2 :
        print("Correct")
    elif:
        if l not in a and r not in a and l != r:
            print("Incorrect")
        else:
            print("Correct")