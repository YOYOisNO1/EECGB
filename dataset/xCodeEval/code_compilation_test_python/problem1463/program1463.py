def program1463():
     a,b=map(int, input().split())
     print(max((a-min(a,b))/2,(b-min(a,b))/2))