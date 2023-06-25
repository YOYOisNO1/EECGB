def program4593():
    n, k = map(int, input().split())
    doors = input()
    
    lo = [-1] * 26
    
    for i in range(len(doors)):
        cc = ord(doors[i]) - ord('A')
        lo[cc] = i
    
    opened = set()
    
    exceeded = False
    
    for i in range(len(doors)):
        cc = ord(doors[i]) - ord('A')
        opened.add(cc)
    
        if len(opened) > k:
            exceeded = True
            break
    
        if i == lo[cc]:
            opened.remove(cc)
    
    print("YES" if exceeded else "NO")