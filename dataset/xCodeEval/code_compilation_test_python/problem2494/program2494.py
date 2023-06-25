def program2494():
    n=int(input())
    
    code_crack=[0,5,3,2,4,1]
    new=''
    for i in range(6):
        new+=str(bit[code_crack[i]])
    print(int(new,2)