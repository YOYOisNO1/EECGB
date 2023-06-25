def program455():
    s = str(input())
    e = s.split(" ")
    ss = str(input())
    ee = ss.split(" ")
    count = 0
    answer = []
    for i in range(int(e[0])):
        answer.append(0)
    index = 0
    truth = False
    i=0
    while count < int(e[0]):
        while i < int(e[0]) and truth = False:
            if answer[i] < int(ee[i]):
                answer[i]+=int(e[1])
                if answer[i]>=int(ee[i]):
                    count+=1
                    index = i
                    if count == int(e[0]):
                        truth = True
            i+=1
    print(index)