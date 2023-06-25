def program2526():
    mass = list(map(int, input().split()))
    count = 0
    for i in range(0, 3):
        if i == 0:
            if mass[i] == mass[i+1]:
                count += 1
                mass[i+1] = -1
            if mass[i] == mass[i+2]:
                count += 1
                mass[i+2] = -10
            if mass[i] == mass[i+3]:
                count += 1
                mass[i+3] = -100
        if i == 1:
            if mass[i] == mass[i+1]:
                count += 1
                mass[i+1] = -15
            if mass[i] == mass[i+2]:
                count += 1
                mass[i+2] = -16
        if i == 2:
            if mass[i] == mass[i+1]:
                count += 1
                mass[i+1] = -11
    
    print(count)