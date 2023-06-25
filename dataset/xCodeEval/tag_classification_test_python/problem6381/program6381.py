def program6381():
    '''import sys 
    sys.stdin = open('/home/srikar/Desktop/input.txt', 'r')  
    sys.stdout = open('/home/srikar/Desktop/output.txt', 'w') '''
    MOD = 1000000007
    MOD2 = 998244353
    ii = lambda : int(input())
    si = lambda : input()
    dgl = lambda : list(map(int, input()))
    f = lambda : map(int, input().split())
    il = lambda : list(map(int, input().split()))
    ls = lambda : list(input())
    k1,k2,k3=sorted(f())
    if k1==1 or k1==k2==2 or k1==k2==k3==3 or (k1,k2,k3)==(2,4,4):
    	print('YES')
    else:
    	print('NO')