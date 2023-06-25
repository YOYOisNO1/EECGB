def mp():  return map(int,input().split())
def lt():  return list(map(int,input().split()))
def pt(x):  print(x)
def ip():  return input()
def it():  return int(input())
def sl(x):  return [t for t in x]
def spl(x): return x.split()
def aj(liste, item): liste.append(item)
def bin(x):  return "{0:b}".format(x)
def listring(l): return ' '.join([str(x) for x in l])
def ptlist(l): print(' '.join([str(x) for x in l]))
    
    c,b,h,w,n = mp() 
    a = lt()
    
    dict = {}
def cal(x,y,i):
        global dict
        if (x,y,i) in dict:
            return dict[(x,y,i)]
        elif i == -1:
            if max(x,y) > 1:
                dict[(x,y,-1)] = float("inf")
                return dict[(x,y,-1)]
            else:
                dict[(x,y,-1)] = 0
                return dict[(x,y,-1)]
        else:
            if max(x,y) <= 1:
                dict[(x,y,i)] = 0
                return 0
            else:
                w1,w2,u1,u2 = cal(x,y/a[i],i-1)+1,cal(x,y,i-1),cal(x/a[i],y,i-1)+1,cal(x,y,i-1)
                dict[(x,y,i)] = min(w1,w2,u1,u2)
                return dict[(x,y,i)]
    v = cal(c/h,b/w,n-1)
    dict = {}
    u = cal(b/h,c/w,n-1)
    r = min(v,u)
    if r == float("inf"):
        pt(-1)
    else:
        pt(r)
        
        
        