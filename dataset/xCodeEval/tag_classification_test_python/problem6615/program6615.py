    from math import ceil
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    
def solve(n,k,a):
        one,two,four = 0, n*2, n
        for size in a:
            while size >= 4:
                if four > 0:
                    four -= 1
                else:
                    two -= 2
                size -= 4
    
            while size > 0:
                if four > 0:
                    four -= 1
                    if size == 2:
                        one += 1
                    elif size == 1:
                        two += 1
                    break
                elif two > 0:
                    two -= 1
                    size -= 2
                elif one > 0:
                    one -= 1
                    size -= 1
                else:
                    return "NO"
        return "YES"
    
    
    
    print(solve(n,k,sorted(a, reverse=True)))
    