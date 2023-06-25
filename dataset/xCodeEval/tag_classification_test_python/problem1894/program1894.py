def program1894():
    n=int(input())
    st1=input()
    l=0
    r=0
    for i in range (n):
       if(st1[i]=="L"):
             l+=1
       if(st1[i]=="R"):
             r+=1
    print(l+r+1)