def program2536():
    #puzzle
    
    students,puzzles = map(int,input().split(" "))
    p = map(int,input().split(" "))
    p.sort()
    i = 0
    s = 1000000000000000
    while i+students <= puzzles:
            if abs(p[i]-p[i+students-1]) < s:
                    s=abs(p[i]-p[i+students-1])
            i+=1
    print(s)