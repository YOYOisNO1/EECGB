    w,b=map(float,input().split())
    
def fun(w,b):
        if w>0 and b>0:
            #case,这里的递归有问题，级数和的问题
            temp=b/(b+w)*(b-1)/(w+b-1)
            return w/(w+b)+temp*(w/(w+b-2)*fun(w-1,b-2)+(b-2)/(w+b-2)*fun(w,b-3))
        elif w>0 and b==0:
            return 1
        else:
            return 0
    pro=fun(w,b)
    print(pro)