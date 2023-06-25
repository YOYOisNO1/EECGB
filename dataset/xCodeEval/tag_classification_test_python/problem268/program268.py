def program268():
    first, last = input().split()
    l = []
    l.append(first[0])
    for i in range(1,len(first)):
        if first[i]<last[0]:
            l.append(first[i])
        else:
            break
    l.append(last[0])
    print(''.join(l))