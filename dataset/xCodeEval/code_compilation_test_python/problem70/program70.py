def program70():
    n=int(input("testcase?"))
    keyinhand=[]
    doors=[]
    answer=[]
    if (1<=n<=18):
        for i in range (n):
            key=input("key in hand?")
            key=int(key)
            if (0<=key<=3):    
                keyinhand.append(key)
                a,b,c = input("keys behind doors?").split()
                a=int(a)
                b=int(b)
                c=int(c)
                if ((0<=a<=3) and (0<=c<=3) and (0<=b<=3)):
                    doors[1].append(a)
                    doors[2].append(b)
                    doors[3].append(c)
                if (doors[key]==0):
                    answer[i].append("NO")
                elif(doors[doors[key]]==0):
                    answer[i].append("NO")
                else:
                    answer[i].append("YES")               
        for i in range (n):
            print(doors[i])
            
    print("end")
    end=input()