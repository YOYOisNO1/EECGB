def program6928():
    from sys import stdin
    
    rstrs = lambda: [str(x) for x in stdin.readline().split()]
    strs_inp = lambda n: [rstrs() for _ in range(n)]
    n = int(input())
    qur, sol = strs_inp(n), []
    
    for i in range(123, 9877):
        num = '0' * (4 - len(str(i))) + str(i)
        if len(set(num)) != 4:
            continue
    
        q = 0
        for a, b, c in qur:
            same, diff = 0, 0
            for j in range(4):
                if num[j] == a[j]:
                    same += 1
                if a[j] in num:
                    diff += 1
    
            diff -= same
            if diff == int(c) and same == int(b):
                q += 1
    
        if q == n:
            sol.append(num)
    
    if len(sol) > 1:
        print('Need more data')
    elif not len(sol):
        print('Incorrect data')
    else:
        print(sol[0])