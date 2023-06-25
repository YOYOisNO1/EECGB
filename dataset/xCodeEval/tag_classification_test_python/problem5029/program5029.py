    w,b=map(float,input().split())
    dic={}
    
def fun(w,b):
        if dic.get((w,b)):
            return dic[(w,b)]
        if w>0 and b>1:
            temp=b/(b+w)*(b-1)/(w+b-1)
            res=w/(w+b)+temp*(w/(w+b-2)*fun(w-1,b-2)+(b-2)/(w+b-2)*fun(w,b-3))
            dic[(w,b)]=res
            return res
        elif w>0 and b==1:
            return w/(w+b)
        elif w>0 and b==0:
            return 1.0
        else:
            return 0.0
    
    pro=fun(w,b)
    print(pro)