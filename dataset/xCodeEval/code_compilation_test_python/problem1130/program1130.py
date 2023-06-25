    import math
def get_dividers(n):
        dividers = {1}
        i = 2
        while n > 1:
            while n % i == 0:
                dividers.add(i)
                n /= i
            i += 1
        return dividers
    
    n = int(input())
    
    dividers = get_dividers(n)
    possible_solutions = {1} 
    for mul in dividers:
        new_solutions = set()
        for curr in possible_solutions:
            if curr * mul <= n:
                new_solutions.add(curr * mul)
        possible_solutions.update(new_solutions)
    print(max(possible_solutions)