def program404():
    arr = sorted([(len(input())-2,i) for i in 'ABCD'])
    p=0
    if 2 * arr[0][0] <= arr[1][0]:
        p+=1
    if 2 * arr[-2][0] <= arr[-1][0]:
        p+=2
    print(['C',arr[0][1],arr[-1][1],'C'][p])