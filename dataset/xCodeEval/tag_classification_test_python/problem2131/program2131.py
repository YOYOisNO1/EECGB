    from __future__ import print_function
    import sys
    from collections import *
    from heapq import *
    from functools import *
    INF=float("inf")
    NINF=float("-inf")
    
    try:
        input=input
    except:
        pass
    
def read_string():
        return input()
    
def read_int_line():
        return [int(x) for x in input().split(" ")]
    
def read_int():
        return int(input())
    
    class TreeNode(object):
    def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    def __str__(self):
            q=deque()
            ans=[]
            q.append(self)
            ans.append(self.val)
            while q:
                cur=q.popleft()
                ans.append(cur.left.val if cur.left else "null")
                ans.append(cur.right.val if cur.right else "null")
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            while ans and ans[-1] == "null":
                ans.pop()
            return str(ans).replace("'null'", 'null')
    
def toTreeNode(s):
        l = eval(s.replace("null", "None"))
        n=len(l)
        if not n:
            return None
        root=TreeNode(l[0])
        q=deque()
        q.append(root)
        i=1
        while q and i < n:
            cur=q.popleft()
            if l[i] != None:
                cur.left = TreeNode(l[i])
                q.append(cur.left)
            i+=1
            if i>=n:
                break
            if l[i] != None:
                cur.right=TreeNode(l[i])
                q.append(cur.right)
            i+=1
        return root
    
    class Djs:
    def __init__(self, n):
            self.w=[1]*n
            self.p=[-1]*n
    def find(self, x):
            p=self.p[x]
            if p==-1:
                return x
            else:
                self.p[x]=self.find(p)
                return self.p[x]
    def union(self, x, y):
            x,y=self.find(x),self.find(y)
            if x==y:
                return
            if self.w[x]>self.w[y]:
                x,y=y,x
            self.p[x]=y
            self.w[y]+=self.w[x]
    def roots(self):
            return [x for x, y in enumerate(self.p) if y==-1]
    
def mat3d(x, y, z, fill=0):
        return [[[fill]*z for _ in range(y)]  for _ in range(x)]
    
def mat2d(h, w, fill=0):
        return [[fill]*w for _ in range(h)] 
    
def matmul(m1, m2,P=0):
        h1,w1=len(m1),len(m1[0])
        h2,w2=len(m2),len(m2[0])
        assert w1==h2
        ans=mat2d(h1,w2)
    
        if P:
            for i in range(h1):
                for j in range(w2):
                    for k in range(w1):
                        ans[i][j]=(ans[i][j]+m1[i][k]*m2[k][j])%P
        else:
            for i in range(h1):
                for j in range(w2):
                    for k in range(w1):
                        ans[i][j]=ans[i][j]+m1[i][k]*m2[k][j]
        return ans
    
def mati(n):
        ans=mat2d(n,n)
        for i in range(n):
            ans[i][i]=1
        return ans
    
def matpow(m, p, P):
        # assert square matrix
        h,w=len(m),len(m[0])
        assert h==w
        ans=mati(h)
        base=m
        while p:
            if p%2==1:
                ans=matmul(ans, base,P)
            base=matmul(base, base,P)
            p//=2
        return ans
    
def doit():
        n,k,d=read_int_line()
        dp=mat2d(n+1,2, 0)
        dp[0][0]=1
        P=10**9+7
        for ni in range(1,n+1):
            for cur in range(1, min(k+1, ni+1)):
                if cur<d:
                    dp[ni][0]+=dp[ni-cur][0]
                    dp[ni][1]+=dp[ni-cur][1]
                else: dp[ni][1]+=dp[ni-cur][0]+dp[ni-cur][1]
            dp[ni][0]%=P
            dp[ni][1]%=P
        print("%d"%dp[n][1])
    
    
    
    
    
    if __name__ == "__main__":
        try:
            while True:
                doit()
        except EOFError:
            pass