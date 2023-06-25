def program1348():
    from collections import deque
    
    if __name__ == '__main__':
        n = int(input())
        K1 = [int(num) for num in input().split()]
        K2 = [int(num) for num in input().split()]
    
        K1, K2 = K1[1:], K2[1:]
        Q1, Q2 = deque(reversed(K1)), deque(reversed(K2))
        nb_fight = 0
        E = set()
        E.add((tuple(Q1), tuple(Q2)))
        while True:
            k1, k2 = Q1.pop(), Q2.pop()
    
            if k1 > k2:
                Q1.appendleft(k2)
                Q1.appendleft(k1)
            else:
                Q2.appendleft(k1)
                Q2.appendleft(k2)
    
            nb_fight += 1
            if (tuple(Q1), tuple(Q2)) in E:
                print(-1)
                break
            elif not Q1:
                print(nb_fight,) 2
                break
            elif not Q2:
                print(nb_fight,) 1
                break
    
            E.add((tuple(Q1), tuple(Q2)))