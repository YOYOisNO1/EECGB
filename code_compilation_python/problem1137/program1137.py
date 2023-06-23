def program1137():
    # Python 2.7.10
    # Time   : 2017-7-19 10:30
    # Auther : Anjone
    # URL : http://codeforces.com/contest/831/problem/A
    
    flag = 1
    n = int(input())
    array = list(map(int,input().split()))
    for i in range(1,n):
    	if(flag == 1 and array[i] > array[i-1] or flag == 2 and array[i] == array[i-1] or flag == 3 and array[i] < array[i-1]):
    	 	continue;
    	elif(++flag > 3):
    		print 'NO'
    		exit(0)
    	i--
    print 'YES'
    