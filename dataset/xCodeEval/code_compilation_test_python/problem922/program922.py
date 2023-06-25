def program922():
    int n = int(input())
    
    int lst = [int(i) for i in input().split()]
    lst.sort()
    
    if n == 1:
        print(lst[0])
    elif n == 3:
        print(lst[1])
    else n == 5:
        print(lst[2])