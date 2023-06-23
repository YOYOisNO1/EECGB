def program3785():
    import re;
    s=input();
    s=re.sub(r"at","@",s,1);
    for i in range(100):
      s=re.sub(r"([a-z]|\.|\@)dot([a-z]|\.|\@)",r"\1.\2",s);
    print(str(s));