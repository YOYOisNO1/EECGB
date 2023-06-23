def program2878():
    enc=input()
    nums=[]
    for i in range(10):
        nums.append(input())
    code=[nums.index(enc[x*10:x*10+10]) for x in range(int(len(enc)/10))]
    for x in code:
        print(x,end='')