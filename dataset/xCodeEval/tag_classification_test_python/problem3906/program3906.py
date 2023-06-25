def get_product(n):
        product = 1
        while n > 0 and product > 0:
            product *= (n % 10)
            n //= 10
        return product
    
    
    n = input()
    l = len(n)
    n = int(n)
    maximum_product = get_product(n)
    for i in range(0, l):
        base = 10 ** (l - i - 1)
        v = (n // base - 1) * base + (base - 1)
        maximum_product = max(maximum_product, get_product(v))
    print(maximum_product)