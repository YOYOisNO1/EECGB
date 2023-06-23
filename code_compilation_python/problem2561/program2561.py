def program2561():
    n,k=map(int,input().split(' '));
    two=2**(n-1);
    value=n;
    while two != k:
        if(two<k):
            k = k-two;
        value--;
        two = two //2;
    print(n);