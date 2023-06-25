def program2294():
    is_prime = lambda x: all(x%d for d in range(2, int(x**.5)+1))
     
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print('YES' if a==b+1 and is_prime(a+b) else 'NO'