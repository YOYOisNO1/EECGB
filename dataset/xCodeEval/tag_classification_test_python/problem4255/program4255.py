def inp():
        return map(int, input().split())
    
    
def arr_inp(n):
        return [int(x) for x in input().split()]
    
    
def print_arr(arr):
        print(*arr, sep=' ')
    
    
    n, m = inp()
    b = arr_inp(m)
    out = [0 for i in range(n)]
    
    for i in range(m):
        if (out[b[i] - 1] == 0):
            out[b[i] - 1] = b[i]
            for j in range(b[i], n):
                if (out[j] == 0):
                    out[j] = b[i]
                else:
                    break
    print_arr(out)