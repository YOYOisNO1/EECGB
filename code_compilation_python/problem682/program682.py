def program682():
    n = int(input())
    s = input()
    print("Yes" if (((s.count("1")-s.count("0"))==0)or((s.count("1")-s.count("0"))==1))) else "No")