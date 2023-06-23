def program3972():
    text = input()
    n, k = map(int ,text.split(" "))
    d = n//(2*(k+1))
    c = k*d
    nw = n - c - d
    print("%d %d %d"%(d, c , nw))