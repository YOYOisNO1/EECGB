def program2136():
    a=(input()+"0")[1:]
    print(9*len(a)-sum(map(int,a))+(len(a)>1))