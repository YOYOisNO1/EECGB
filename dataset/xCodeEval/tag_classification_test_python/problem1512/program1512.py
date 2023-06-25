def program1512():
    a=lambda:input();a();a=a();print(["NO","YES"][len(a)-len(set(a))>=1 or len(a)==1 ])
    