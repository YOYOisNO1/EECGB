    from sys import stdin
    lines = stdin.readlines()
    n = int(lines[0])
    liste = []
    for i in str(n):
        liste.append(i)
    flag = True
def bul(liste,num):
        k = 0
        for i in range(len(liste[k:])):
            if len(num) == 0:
                return True
            elif liste[i] == num[0]:
                num = num[1:]
                k = i+1
        if len(num) == 0:
            return True
        else:
            return False
    
    for i in range(int(n**0.5)+1,0,-1):
        if bul(liste,str(i**2)):
            print(len(liste)) - len(str(i**2))
            flag = False
            break
    if flag:
        print(-1)