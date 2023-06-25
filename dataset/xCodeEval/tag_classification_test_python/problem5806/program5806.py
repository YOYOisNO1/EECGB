def program5806():
    i=input
    i()
    s=list(map(int,i().split()))
    print("Bob"if s.count(min(s))>len(s)/2 else"Alice")