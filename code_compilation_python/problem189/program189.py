def main():
        x,y=map(long,input().split())
        y-=1 
        if y!=0 and (x-y)%2==0 and x>=y:
            print "Yes"
        else:
            print "No"
        
    main()