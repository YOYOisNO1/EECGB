    import math
    import time
    
    D = False
    
def b_search(lst, num,  row, col, ab):
        H = len(lst) - 1
        L = 0
    
        while L <= H:
            M = (L + H)//2
    
            if D: print(lst[M], row, ab/lst[M], col)
    
            if D: print("cond:", lst[M] <= row, num/lst[M] <= col)
    
            if lst[M] <= row and num/lst[M] <= col:
                return True
    
            if lst[M] > row:
                H = M - 1
    
            else:
                L = M + 1
    
        return False
    
def binary_search(lst1, a, lst2, b, row, col, ab):
        # we need to know if any rect in lst1 or lst2
        # can fix inside the dimensions of row, col
    
        # in this case, row <= col, and
        # item in lst are <= their pair
    
        if b_search(lst1, a, row, col, ab):
            return True
    
        return b_search(lst2, b, row, col, ab)
    
def divisors(num):
        rtn = []
        for i in range(1, math.ceil(math.sqrt(num)) + 1):
            if num % i == 0:
                rtn.append(i)
        return rtn
    
def sol():
        a, b = [int(x) for x in input().split(" ")]
        ab = a + b
        if D: print("")
        if D: print("a, b, ab:", a, b, ab)
    
        div_a  = divisors(a)
        div_b  = divisors(b)
        div_ab = divisors(ab)
    
        if D:
            print("div_a: " + ", ".join([str(x) for x in div_a]))
            print("div_b: " + ", ".join([str(x) for x in div_b]))
            print("div_ab: " + ", ".join([str(x) for x in div_ab]))
    
        for i in range(len(div_ab) - 1, -1, -1):
            row = div_ab[i]
            col = int(ab/row)
            if D: print("\n* Trying")
            if D: print("row, col:", row, col)
    
            ans = binary_search(div_a, a, div_b, b, row, col, ab)
    
            if ans:
                return 2 * (row + col)
    
    if D: start = time.time()
    
    # main
    #for t in range(int(input())):
    ans = int(sol())
    print(ans)
    
    if D:
        end = time.time()
        print(end - start)