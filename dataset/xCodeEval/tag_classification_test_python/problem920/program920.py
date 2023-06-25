def program920():
    n=int(input())
    s=input()
    arr=[]
    num=[]
    for i in range(n):
    	if s[i:i+2] in arr:
    		num[arr.index(s[i:i+2])]+=1
    	else:
    		arr.append(s[i:i+2])
    		num.append(1)
    #print(s[2:3])
    print(arr[num.index(max(num))])