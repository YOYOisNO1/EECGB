def program1342():
    #br = open('d.in')
    n = int(input())
    print(["white\n%d) %d" % (1, 2), "black"][n % 2]