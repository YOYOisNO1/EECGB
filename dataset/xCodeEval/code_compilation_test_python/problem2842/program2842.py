def program2842():
    n=int(input())
    t=list(input())
    if(n==1):
          print("t")
    else:
          s=''
          i=1
          summ=1
          while(i<n):
                s+=t[i-1]
                i+=summ
                summ+=1
          print(s)`