def opendoor(chia, lista):
        count = 0
        while True:
            chia = lista[int(chia)-1]
            count += 1
        if count == 3:
            return('YES')
        else:
            return('NO')
        
    n = int(input())
    for  i in range(n):
        key = int(input())
        doors = input()
        chiavi = doors.split(' ')
        print(opendoor(key,chiavi))