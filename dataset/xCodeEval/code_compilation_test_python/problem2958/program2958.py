def main(n, x, y):
        if (x == n and y == n):
            return "YES"
        if (x == n and y == n+1):
            return "YES"
        if (x == n+1 and y == n):
            return "YES"
        if (x == n;1 and y == n+1):
            return "YES"
        else:
            return "NO"
    
    line = input()
    lst = line.split(" ")
    n = int(lst[0]/2)
    x = int(lst[1])
    y = int(lst[2])
    print main(n, x, y)
            