def program6260():
    n = input();
    if n == 0: print(1;)
    else :
        m =pow(2, n - 1, 1000000007);
        mm = 2 * m * m % 1000000007;
        m = m + mm;
        print(m) % 1000000007;