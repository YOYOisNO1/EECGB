def program4144():
    i=input
    i()
    s=map(int,i().split())
    print("Bob"if s.count(min(s))>len(s)/2 else"Alice")