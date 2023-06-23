def program256():
    first = [int(x) for x in input().split(' ')]
    string = input()
    q = [x for x in string]
    time = 0
    while time < first[1]:
        ctr = 0
        while ctr < first[0]-1:
            if q[ctr] == 'B' and q[ctr+1] == 'G':
                q[ctr],q[ctr+1] == q[ctr+1],q[ctr]
                ctr +=1
        time +=1 
    print(q.join(''))