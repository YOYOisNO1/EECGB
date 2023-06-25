def program4228():
    n=int(input())
    s=input()
    f=0
    if len(s)==1:
        if s[0]=="0":
            
            print("NO")
        else:
            print("YES")
    else:
        s1=""
        s1="0"+s+"0"
        if "11" in s1:
            print("NO")
        elif "000" in s1:
            print("NO")
        else:
            print("yeS")