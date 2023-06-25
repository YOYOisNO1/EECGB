def program476():
    n = int(input())
    students = [int(s) for s in input().split()]
    students.sort()
    c = 0
    for i in range(len(students)):
        if i%2==0:
            c -= students[i]
        else:
            c += students[i]
            
    print(c)