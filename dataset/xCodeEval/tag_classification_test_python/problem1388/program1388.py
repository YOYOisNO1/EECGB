def program1388():
    str='January, February, March, April, May, June, July, August, September, October, November, December'
    list=str.split(', ')
    #print(list[1])
    m=input()
    n=0
    for i in range(len(list)):
        if m==list[i]:
            n=i
            break
    n2=int(input())
    n2=(n2+n)%12
    print(list[n2])