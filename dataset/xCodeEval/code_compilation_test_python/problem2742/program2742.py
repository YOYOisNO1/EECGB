def program2742():
    n = input()
    
    ans = 0
    while n > 0:
        x = n % 16
        n /= 16
        if x == 0 or x == 4 || x == 6 || x == 9 || x == 10 || x == 13:
            ans += 1
        else:
          if x == 8 || x == 11:
              ans += 2
    
    print ans