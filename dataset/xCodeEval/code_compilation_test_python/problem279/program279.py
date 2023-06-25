def program279():
    n=input()
    num=input()
    left=sorted(map(int,num[:n]))
    right=sorted(map(int,num[n:]))
    
    
    if left[0]<right[0]:
        i=1
        while i<n:
            if left[i]>=right[i]:
                print("NO")
                break
                i+=1
        else:
            print("YES")
    elif left[0]>right[0]:
        i=1
        while i<n:
            if left[i]<=right[i]:
                print("NO")
                break
                i+=1
    
        else:
            print("YES")
    
    else:
        print("NO")
       