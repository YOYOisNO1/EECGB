def program3844():
    s = input()
    x = [4, 5, 6, 3, 2, 1][ord(s[-1]) - ord('a')]
    y = int(s[:-1]) - 1
    
    print (y // 4) * 16 + x + (y % 2) * 7