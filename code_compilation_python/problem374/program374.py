    s = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        
def solve():
        n = int(input())
        a = input()
    	a = a.lower()
    	return all(i in a for i in s)
    	
    ans = solve()
    if ans:
        print("YES")
    else:
        print("NO")