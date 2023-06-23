    s,t=input(),input()
    ss,tx=str(sorted(s)),str(sorted(t))
def subset(s,t):
        i=0
        for c in s:
            if c==t[i]:i+=1
            elif i==len(t):break
        return i==len(t)
    if ss==tx:
        print("array")
    elif subset(s,t):
        print("automaton")
    elif subset(ss,tt):
        print("both")
    else: 
        print("need tree)