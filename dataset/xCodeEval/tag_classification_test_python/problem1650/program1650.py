def program1650():
    l = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',';','z','x','c','v','b','n','m',',','.','/']
    d = input()
    s = input()
    for i in s:
        print(l[l.index(i)-1] if d=='R' else l[l.index(i)+1], end='')