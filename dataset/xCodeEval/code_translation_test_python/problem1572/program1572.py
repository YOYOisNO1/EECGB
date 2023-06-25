def program1572():
    h,m=map(int,input().split(":"));print(h%12*30+m/2.,m*6)