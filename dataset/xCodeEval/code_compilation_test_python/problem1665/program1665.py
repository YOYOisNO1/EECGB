def main():
        s = input()
        x, y, z = map(int, input().split())
        p1, p2, p3 = map(int, input().split())
        a = s.count('B')
        b = s.count('S')
        c = s.count('C')
        r = int(input())
        if a != 0 and b != 0 and c != 0:
            d = min(x // a, y // b, z // c)
            cost = a * p1 + b * p2 + c * p3
            total = (x - a * d) * p1 + (y - b * d) * p2 + (z - c * d) * p3 + r
            ans = d + total // cost
        elif a == 0:
            if b != 0 and c != 0:
                d = min(y // b, z // c)
                cost = b * p2 + c * p3
                total = (y - b * d) * p2 + (z - c * d) * p3 + r
                ans = d + total // cost
            elif b == 0:
                d = min(z // c)
                cost = c * p3
                total = (z - c * d) * p3 + r
                ans = d + total // cost
            elif c == 0:
                d = min(y // b)
                cost = b * p2
                total = (y - b * d) * p2 + r
                ans = d + total // cost
        elif b == 0:
            if a != 0 and c != 0:
                d = min(x // a, z // c)
                cost = a * p1 + c * p3
                total = (x - a * d) * p1 + (z - c * d) * p3 + r
                ans = d + total // cost
            elif a == 0:
                d = min(z // c)
                cost = c * p3
                total = (z - c * d) * p3 + r
                ans = d + total // cost
            elif c == 0:
                d = min(x // a)
                cost = a * p1
                total = (x - a * d) * p1 + r
                ans = d + total // cost
        else:
            if a != 0 and b != 0:
                d = min(x // a, y // b)
                cost = a * p1 + b * p2
                total = (x - a * d) * p1 + (y - b * d) * p2 + r
                ans = d + total // cost
            elif a == 0:
                d = min(y // b)
                cost = b * p2
                total = (y - b * d) * p2 + r
                ans = d + total // cost
            elif b == 0:
                d = min(x // a)
                cost = a * p1
                total = (x - a * d) * p1 + r
                ans = d + total // cost
        print(ans)
    
    
    if __name__ == '__main__':
        main()