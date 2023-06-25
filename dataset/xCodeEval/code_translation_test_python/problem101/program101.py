def program101():
    y, b, r = map(int, input().split())
    m=1;n=2; o=3
    mix = 6
    while m<y and n<b and o<r:
        m+=1; n+=1; o+=1
        mix = (m+n+o)
    print(mix)