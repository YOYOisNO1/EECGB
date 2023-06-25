def program6923():
    s=input()
    print((int(s,2)*1<<len(s)-1)%1000000007)