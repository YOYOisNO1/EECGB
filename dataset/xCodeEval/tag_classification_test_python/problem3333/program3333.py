def findnumber(num):
      final=-1
      
      for check in range(int(num[0]),int(num[1])+1):
        arr = list(map(int,str(check))) 
        if len(arr) == len(set(arr)):
          final=check
          break
      return final
    print(findnumber(input().split()))