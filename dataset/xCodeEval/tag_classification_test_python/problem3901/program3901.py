def get_natural_sum(n):
        return n * (n+1) // 2
    
    a = int(input())
    b = int(input())
    
    n1, n2 = max(a, b), min(a, b)
    
    dist_a = (n1 - n2) // 2
    dist_b = (n1 - n2) - dist_a
    
    print(get_natural_sum(dist_a) + get_natural_sum(dist_b))