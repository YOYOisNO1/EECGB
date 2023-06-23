def program1261():
    from fnmatch import fnmatch, fnmatchcase
    pat = "CODE*FORCES"
    pat2 ="*CODEFORCES"
    pat3 ="CODEFORCES*"
    pat4 "*CODEFOCES*"
    name = input()
    if fnmatch(name, pat) or fnmatch(name, pat3) or fnmatch(name, pat2) or fnmatch(name, pat4):
        print("YES")
    else:
        print("NO")