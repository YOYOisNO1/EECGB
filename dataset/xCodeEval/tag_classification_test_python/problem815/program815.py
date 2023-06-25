def program815():
    n = int(input())
    List = [0,9,90,900,9000,90000,900000,9000000,90000000,900000000,9000000000]
    i = 1
    count = 0
    while n>List[i]:
        count += List[i]*i
        n -= List[i]
        i+=1
    count += n*i
    print(count)