def program1454():
    for i in range(int(input())):
          cnt = 0
          n = int(input())
          a = list(map(int, input().split()))
          a1 = [0,1,2]
          n-=1
          a[0]-=1
          a[1]-=1
          a[2]-=1
          while True:
                if n in a1:
                      cnt+=1
                      x = a[n]
                      n = x
                else:
                      break
          print("YES" if cnt == 3 else "NO")