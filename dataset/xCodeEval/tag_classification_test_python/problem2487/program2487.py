def program2487():
    import math
    
    a,b = input().split()
    a = int(a)
    b = int(b)
    
    if b==a:
        print("1")
    else:
        ans=2
        start=3
        end=a
        while start<=end:
            mid=math.floor((start+end)>>1);
            #print(start,end,mid);
            if mid%2==0:
                gadha=math.ceil(math.log(math.ceil(b/2.0)+1,2))-1
                len_gadha=mid-2
                total_len=int(len_gadha*((1<<gadha)-1))
               # print(total_len,len_gadha,gadha,mid)
                if total_len+b+mid-1<=a:
                    start=mid+1
                    ans=mid
                else:
                   # print("here")
                    end=mid-1
            else:
                gadha=math.ceil(math.log(b+1,2))-1;
                len_gadha=mid-1
                total_len=int(len_gadha*((1<<gadha)-1))
               # print(total_len,len_gadha,gadha,mid)
                if total_len+b+mid-1<=a:
                    start=mid+1
                    ans=mid
                else:
                    tmp=mid+1
                    gadha=math.ceil(math.log(math.ceil(b/2.0)+1,2))-1
                    len_gadha=tmp-2
                    total_len=int(len_gadha*((1<<gadha)-1))
                   # print(total_len,len_gadha,gadha,tmp)
                    if total_len+b+tmp-1<=a:
                        start=tmp+1
                        ans=tmp
                    else:
                        end=mid-1
        print(ans)