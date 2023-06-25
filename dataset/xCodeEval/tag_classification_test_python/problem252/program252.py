    x=input()
    y=x.strip(" ?")
    
def a1():
        p = y[len(y)-1]
        if p=='a' or p=='e' or p=='i' or p=='o' or p=='u' or p=='A' or p=='O' or p=='I' or p=='E' or p=='U' or p=="y" or p=='Y' :
            print("YES")
    
        else:
            print("NO")
    
    a1()