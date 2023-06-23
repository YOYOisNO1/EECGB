def program2287():
    x,y,z,tuno,tdos,ttres=map(int,input().split())
    var1=abs(x-y)  
    stair=var1*tuno
    var2=abs(x-z)
    eleva=((3*ttres)+((var2)*tdos)+((var1)*tdos)
    if stair>=eleva:
          print("YES")
    else:
          print("NO")