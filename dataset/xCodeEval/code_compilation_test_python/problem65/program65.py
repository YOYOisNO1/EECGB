def main():
        if n // 7 == 0 and n%7==6: s1 = 1
        else: s1 = n // 7 * 2
        s2 = n // 7 * 2
        if n % 7 == 1: s2 += 1
        elif n % 7 >= 2: s2 += 2
    
        print(s1,s2)
    main()