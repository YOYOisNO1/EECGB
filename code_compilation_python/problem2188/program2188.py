def program2188():
    pages = int(input().strip())
    weeks = input().strip().split()
    weeks[0] = int(weeks[0])
    for i in range(1,len(weeks)):
        weeks[i] = weeks[i - 1] + int(weeks[i])
    pages %= weeks[6]
    if pages == 0:
        print 7
        return
    #print pages, weeks[6]
    for i in range(len(weeks)):
        if pages <= weeks[i]:
            print str(i+1)
            break