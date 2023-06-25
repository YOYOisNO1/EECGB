def answer():
        a = sum([int(x) for x in input().split()])
        b = sum([int(x) for x in input().split()])
        c = int(input())
        s_cups = int(a/5)
        if a%5:s_cups+=1
        
        s_medals = int(b/10)
        
        if b%10:s_medals+=1
    
        if c>=s_medals+s_cups:ans = "YES"
        else:ans="NO"
        return ans
    print(answer())