def program7840():
    # test code from internet
    a = int( input() )
    k = (45 * 18 * 10**17) % a;
    t = a - k;
    print(t, t + 10**18 - 1)