def stack(days,count):
      x=count//days
      y=count%days
      return days*(x)*(x-1)//2+y*x
    
def main():
      arr=input().split()
      n=int(arr[0])
      pages=int(arr[1])
      arr=input().split()
      for x in range(n):
        arr[x]=int(arr[x])
      arr.sort(reverse=True)
      
      position=0
      total=0
      while total<pages:
        if position==n:
          return -1
        total+=arr[position]
        position+=1
      #print(position,total)
    
      days=position
      count=position
      
      #print(arr)
      #print(days,count)
      while True:
        if position==n:
            return days
        if arr[position]<=count//(days-1):
          return days
        total+=stack(days,count)
        total-=stack(days-1,count)
        #print(total,days-1)
        while total<pages:
          if position==n:
            return days
          if arr[position]<=count//(days-1):
            return days
          total+=arr[position]-count//(days-1)
          #print(total)
          position+=1
          count+=1
        days-=1
        if days==0:
          return 1
    
    
    
    
    
    print(main())