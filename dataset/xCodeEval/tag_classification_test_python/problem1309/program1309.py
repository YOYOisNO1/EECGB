def program1309():
    n= int(input())
    ans=1
    for i in range(1, n):
      ans*= i
    print(int(ans*2/n))