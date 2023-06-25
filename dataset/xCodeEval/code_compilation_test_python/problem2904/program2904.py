def program2904():
    a=int(input())
    l=0,i=0,c=0
    while(a>0):
          i++
          c=l+i
          l=c
          a-=c
          if(a<0):
            i=i-1
    print(i)