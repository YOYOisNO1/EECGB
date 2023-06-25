    #code
    #print("GfG")
def func(num):
        num=int(num)
        num=num*num*num*num*num
        num=str(num)
        l=len(num)
        s= num[l-5] + num[l-4] + num[l-3] + num[l-2] + num[l-1]
        print(s)
    
    a=input()
    n1=a[0]
    n2=a[1]
    n3=a[2]
    n4=a[3]
    n5=a[4]
    num=""+n1+n3+n5+n4+n2
    func(num)