def program2992():
    bug, beaver, both, students = map(int, input().split())
    
    if ((bug - both) + (beaver - both) + both) < students and students > 0 and bug <= both and beaver <= both and both < students:
        print(str(students - ((bug - both) + (beaver - both) + both)))
    else:
        print(-1