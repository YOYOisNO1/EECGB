def program497():
    
    if __name__=="__main__":
        a=input()
        l=len(a)
        cnt=0
        for i in range(l):
            if a[i]=='1':
                for j in range(i+1,l):
                    if a[j]=='0':
                        cnt+=1
                break
    
        if cnt>5:
            print("yes")
        else:
            print("no")