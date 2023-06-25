def program2560():
        n,k=map(int,input().split())
        biggest_n=2
        seq1=[1]
        for i in range(0,n-1):
            seq1.append(biggest_n)
            seq1.extend(seq1[:-1])
            biggest_n+=1
            
        mid_n=biggest_n
    
        seq1ind=range(0,(len(seq1))-1)
        seq2ind=range(len(seq1)+1,(len(seq1)*2))
        mid_nind=len(seq1)
    
        if k in seq1ind or k in seq2ind:
            res=seq1ind[k]
        else:
            res=mid_n
        print(res)