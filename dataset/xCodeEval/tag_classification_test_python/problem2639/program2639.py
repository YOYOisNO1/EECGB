def program2639():
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    print('0', end=' ')
    for i in range(1,n):
        student_fail = 0
        new_lst = s[:i+1]
        while sum(new_lst) > m:
            new_lst.remove(max(new_lst[:-1]))
            student_fail+=1
        print(student_fail, end=' ')