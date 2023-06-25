    s = input()
    
def first(s, i): return s[:i]
def last(s, i): return s[-i:]
    
    for i in range(len(s)//2+1, len(s)):
        if first(s, i) == last(s, i):
            print("YES")
            print(first(s, i))
            break
    else: print("NO")