def program3427():
    r, c = map(int, input().split())
    row = input()
    col = input()
    if((row[0]==">" and col[-1]=="^") or (row[-1]==">" and col[-1]=="v") or (row[0]=="<" and col[0]=="^") or (row[-1]=="<" and col[0]=="v")):
        print("NO")
    else:
        print("YES")