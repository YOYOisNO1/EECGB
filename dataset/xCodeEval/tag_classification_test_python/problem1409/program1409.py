    x,y=map(int,input().split())
    
def sa(x,y):
        div=x//y
        if(x==(div)*y):
            return div
        elif(x>y):
            output=0
            output+=div
            x=x%y
            if x==1:
                output=output+y
                return output
            if x !=1:
                output=output+sa(y,x)
                return output
        else:
            return sa(y, x)
    
    print(sa(x,y))