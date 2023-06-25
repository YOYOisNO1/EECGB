def program687():
    import itertools
    
    n = int(input())
    cube = [0]*n
    for i in range(n):
        cube[i] = map(int,input().split())
    
    nums = []
    
    for j in range(n):
        for i in cube[j]:
            nums.append(i)
    
    if n == 2:
        for j in itertools.permutations('01',2):
            for i in itertools.product(cube[int(j[0])],cube[int(j[1])]):
                if not i[0] == "0":
                    nums.append(int(str(i[0]) + str(i[1])))
    elif n == 3:
        for j in itertools.permutations('012',2):
            for i in itertools.product(cube[int(j[0])],cube[int(j[1])]):
                if not i[0] == "0":
                    nums.append(int(str(i[0]) + str(i[1])))
    
    if n == 3:
        for j in itertools.permutations('012',3):
            for i in itertools.product(cube[int(j[0])],cube[int(j[1])],cube[int(j[2])]):
                if not i[0] == "0":
                    nums.append(int(str(i[0]) + str(i[1]) + str(i[2])))
    
    check = True
    i = 1
    while check:
        if i not in nums:
            print(i-1)
            check = False
        i += 1