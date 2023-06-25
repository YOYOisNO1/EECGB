def program1165():
    """codeforces.com/problemset/problem/848/A"""
    import math
    
    k = int(input())
    if k == 0:
        print("a")
        exit()
    l = []
    while k != 0:
        n = math.floor((1 + math.sqrt(1+8*k))/2)
        l.append(n)
        k -= n*(n-1)/2
    word = ""
    letter = 'a'
    for chc in l:
        word += letter * chc
        letter = chr(ord(letter) + 1)
    print(word)