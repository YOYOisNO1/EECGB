def program1515():
    n = int(input())
    s = str(input())
    
    if n == 1:
        print("YES")
        exit(0)
    if len(s) != len(set(s)):
        print("YES")
    else:
        print("NO")