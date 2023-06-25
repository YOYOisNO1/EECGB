def solution():
        a = int(input())
        b = int(input())
        b, a = max(a, b), min(a, b)
        cost = 1
        res = 0
        while b - a - 2 >= 0:
            res += 2 * cost
            cost += 1
            a += 1
            b -= 1
        if b > a:
            res += cost
        return res
    
    
    if __name__ == '__main__':
        print(solution())