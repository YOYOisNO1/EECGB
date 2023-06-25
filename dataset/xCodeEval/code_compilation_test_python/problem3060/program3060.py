def function(n, nums):
        odd_pair_count=0
        odd_count1=0
        odd_count2=0
        for j in range(n):
            condition=True
            if nums[j][0]%2!=0 and nums[j][-1]%2!=0:
                odd_pair_count+=1
            if nums[j][0]%2!=0:
                odd_count1+=1
            if nums[j][-1] % 2 != 0
                odd_count2+=1
        if (odd_count1 + odd_count2) % 2 != 0:
            return -1
        if (odd_count1+odd_count2)%2==0:
            if odd_pair_count*2-(odd_count1+odd_count2)==0:
                return -1
            if odd_count1%2==0 and odd_count1==odd_count2:
                return 0
            return 1
    
    if __name__=="__main__":
        n=int(input())
        nums=[]
        for i in range(n):
            nums.append(list(map(int, input().rstrip().split())))
        print(function(n, nums))