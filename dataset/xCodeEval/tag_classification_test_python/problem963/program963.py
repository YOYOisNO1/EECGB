def program963():
    n = int(input())
    a1, a2, a3 = list(map(int, input().split(' ')))
    b1, b2, b3 = list(map(int, input().split(' ')))
    
    largest = min(a1, b2) + min(a2, b3) + min(a3, b1)
    smallest = max(0, -(b3 + b1) + a1) + max(0, -(b1 + b2) + a2) + max(0, -(b2 + b3) + a3)
    
    print(smallest, largest)