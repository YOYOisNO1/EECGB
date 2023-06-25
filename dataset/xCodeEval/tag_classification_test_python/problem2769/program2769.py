def program2769():
    s=input()
    print(0 if len(set(s))==1 else (len(s) if s!=s[len(s)-1::-1] else len(s)-1))