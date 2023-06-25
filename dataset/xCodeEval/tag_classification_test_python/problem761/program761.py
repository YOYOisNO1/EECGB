def program761():
    a1,a2,a3=map(int,input().split())
    
    print(int(4*((a1*a3/a2)**(0.5)+(a1*a2/a3)**(0.5)+(a2*a3/a1)**(0.5))))