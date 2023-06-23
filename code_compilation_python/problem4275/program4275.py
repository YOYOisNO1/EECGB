def program4275():
    data = []
    for i in range(int(input())):
        data.append(int(input()))
    if len(data) == 1:
        print(0)
    else:
        data = list(sorted(data))
        result = data[0] + data[1]
        print(result)
        for i in range(2,len(data)):
            print(result + data[i])
            result += data[i]