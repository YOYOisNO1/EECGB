def main():
            l=map(long,input().split())
            n=map(long,input().split())
            y=(n[0]*2)+n[1]
            b=n[1]+(3*n[2])
            if y<l[0]:
                y=l[0]
            if b<l[1]:
                b=l[1]
            print(((y-l[0])+(b-l[1])))
        
    main() 