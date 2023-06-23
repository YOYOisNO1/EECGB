    import sys
    import collections
    
    
def int2base(dec, base):
        ans = []
        while(dec > 0):
            ans.insert(0,dec % base)
            dec //= base
    
        return ans
    
    
def xenodrome(num_list):
        most_common = collections.Counter(num_list).most_common(1)
        return most_common[0][1] == 1
    
    
    
    while(True):
    
        num,base = map(int, input().split())
        candidate = int2base(num,base)
        if(xenodrome(candidate)):
            print("YES")
        else:
            print("NO")