def fun():
        n,k=map(int,input().split())
        gates=0
        mp={}
        opened={}
        inp=input()
        for x in range(len(inp)):
            mp[inp[x]]=x
        for x in range(len(inp)):
            #print(inp[x],gates)
            if mp[inp[x]]!=x:
                if inp[x] not in opened:
                    opened[inp[x]]=1
                    gates+=1
                    if gates>k:
                        return "YES"
            else:
                if inp[x] not in opened:
                    if gates+1>k:
                        return "YES"
                else:
                    gates-=1
        return "NO"
def fun1():
        n,k=map(int,input().split())
        gates=0
        mp={}
        opened={}
        inp=input()
        for x in range(len(inp)):
            mp[inp[x]]=x
        for x in range(len(inp)):
            if mp[inp[x]]!=x:
                if inp[x] not in opened:
                    opened[inp[x]]=1
                    gates+=1
                    if gates>k:
                        return "YES"
            else:
                gates-=1
        return "NO"
    print(fun())
    #print(fun())
        
    