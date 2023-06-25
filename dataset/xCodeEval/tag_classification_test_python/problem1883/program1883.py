def program1883():
    n,y=map(int, input().split())
    first_odd = 1
    last_odd = n if n%2 == 1 else n-1
    n_odd = (last_odd-first_odd)/2 + 1
    if y <= n_odd:
        print(first_odd) + 2*(y-1)
    else:
        y -= n_odd
        print(2+2*(y-1))