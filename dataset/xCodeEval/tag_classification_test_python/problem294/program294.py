def program294():
    __author__ = "Ryabchun Vladimir"
    
    
    n = int(input())
    sum_years = 0
    groups = list(map(int, input().split()))
    for elem in groups:
        sum_years += elem
    print(int(sum_years / n))