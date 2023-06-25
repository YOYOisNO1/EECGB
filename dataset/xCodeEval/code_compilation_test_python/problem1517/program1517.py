def get():
        return int(input())
        
def count():
        c = []
        for i in range(2):
            c.extend(map(int,input().split()))
        return len(c)
        
    for i in range(get()):
        c = count()
        match c:
            case 0: print(0)
            case 1|2|3: print(1)
            case 4: print(2)