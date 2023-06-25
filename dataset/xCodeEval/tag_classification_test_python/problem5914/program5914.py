    n = input()
    crush = [0] + map(int, input().split())
    
    t = 1
    
    flag = [0] * (n + 1)
    
    
def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    
def lcm(a, b):
        return a * b / gcd(a, b)
    
    
def search(start, end, count):
        flag[start] = 1
        next_crush = crush[start]
    
        if next_crush == end:
            return 1 + count
    
        if start == next_crush or flag[next_crush] == 1:
            return -1
    
        return search(next_crush, end, count + 1)
    
    
    for i in range(1, n + 1):
        if flag[i] == 1:
            continue
        step = search(i, i, 0)
        if step == -1:
            t = -1
            break
        else:
            if step % 2 == 0:
                t = lcm(t, step / 2)
            else:
                t = lcm(t, step)
    
    print(t)