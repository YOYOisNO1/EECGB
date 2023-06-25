def program3163():
    m, n = map(int, input().split())
    
    if(m == 1):
        print(1)
    elif(n > m/2):
        print(n) - 1
    else:
      print(n) + 1