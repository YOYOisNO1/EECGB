def program2353():
    input()
    a=set(map(int,input().split())
    print(sum(all(x%y for y in a-{x})for x in a))