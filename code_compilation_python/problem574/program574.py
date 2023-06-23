def program574():
    r,g,b=input().split(" ")
    r,g,b=int(r),int(g),int(b)
    if r<1000 and g<1000 and b<1000 and r>=2 and g>=2 and b>=2 and (r%3==2 or g%3==2 or b%3==2):
        print(2+(r-2)/3+(g-2)/3+(b-2)/3)
    else:
        minm=min(r,min(g,b))
        ans1=minm+(r-minm)/3+(g-minm)/3+(b-minm)/3
        ans2=r/3+g/3+b/3
    	print(max(ans1,ans2))