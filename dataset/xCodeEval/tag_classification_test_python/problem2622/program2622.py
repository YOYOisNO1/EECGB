def program2622():
    '__author__'=='deepak Singh Mehta(learning to code :) ) '
    
    
    
    if __name__=='__main__':
        date,of,param = map(str,input().split())
        date = int(date)
        if param[0]=='w':
          if date==5 or date==6:
            print(53)
          else:
            print(52)
        else:
          if date<=29:
            print(12)
          elif date<= 30:
            print(11)
          else:
            print(7)