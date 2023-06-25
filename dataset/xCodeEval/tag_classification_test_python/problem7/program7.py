def program7():
    import sys
    #import math
    toks = (token for token in sys.stdin.read().split())
    # toks2=sys.stdin.read().split()
    # print(toks2)
    
    
    # N=int(next(toks))
    # M=int(next(toks))
    # X=int(next(toks))
    # T=int(next(toks))
    # D=int(next(toks))
    
    # age=0
    # height=T
    
    # if M<X:
    #   height=height-D*(X-M)
    
    # print(height)
    
    
    # arr=[]
    # for i in range(5):
    #   n=int(next(toks))
    #   if n not in arr:
    #     arr.append(n)
    
    # print(len(arr))
    
    # N=int(next(toks))
    # X=int(next(toks))
    
    # sum=0
    # for i in range(N):
    #   sum+=int(next(toks))
    
    # sum=abs(sum)
    
    # print(math.ceil(sum/X))
    
    N=int(next(toks))
    M=int(next(toks))
    if(M==1):
      print(N-1)
    else:
      print((M-1)*N)
     				    	  				   			 	 	  			