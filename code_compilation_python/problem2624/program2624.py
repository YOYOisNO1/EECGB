def program2624():
        n , a, b = map(int, input().split())
         
        if b >= 0:
            ans = (a + b % n) % n
            if ans == 0:
                print(n)
            else:
                print(ans)
        else:
             ans = (a + (n - abs(b) % n)) % n
             if ans == 0:
                 print(n)
             else:
                print(ans)