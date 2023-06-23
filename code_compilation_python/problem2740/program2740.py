def program2740():
    #n = int(input()) 
    #n, m = map(int, input().split())
    s = input()
    #c = list(map(int, input().split()))
    a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    b = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0]
    s = hex(s)
    l = 0
    for i in range(2, len(s)):
        l += b[a.index(s[i])]
    print(l)