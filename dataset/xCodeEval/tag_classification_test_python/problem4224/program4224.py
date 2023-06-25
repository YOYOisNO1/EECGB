def program4224():
    n=int(input())
    s=input()
    if(s.find("000")!=-1 or s.find("11")!=-1 or s.find("001")==0 or s[::-1].find("001")==0 or s.find("1")==-1):
        print("No")
    else:
        print("Yes")