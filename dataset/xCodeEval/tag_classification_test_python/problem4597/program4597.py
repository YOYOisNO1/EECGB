    guests, guards = map(int, input().split())
    
    gates_opened = {}
    count = {}
    
    seq = input()
    
    for g in seq:
        c = count.setdefault(g, 0)
        count[g] = c+1
    
    
    # print(count)
def main():
        gates = 0
        for g in seq:
            count[g] -= 1
            # print(g, gates_opened)
            if not gates_opened.has_key(g):
                gates += 1
                gates_opened[g] = True
            if gates > guards:
                print('YES')
                return
            if gates_opened.has_key(g):
                if count[g] == 0:
                    gates_opened.pop(g)
                    gates -= 1
    
        print('NO')
    
    if __name__ == '__main__':
        main()