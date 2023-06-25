def program3294():
    data = input().split() 
    w1, h1, w2, h2 = int(data[0]), int(data[1]), int(data[2]), int(data[3])
    print(w2+h2+w1-w2+h1+w1+h2+h1+4)