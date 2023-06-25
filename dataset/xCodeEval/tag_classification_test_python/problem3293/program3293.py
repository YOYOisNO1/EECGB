def program3293():
    w1 , h1 , w2 , h2=map(int,input().split())
    if w2==w1:
        h=(h1+h2)
        ANS=(w2+2)*(h+2)-(w2*h)
        print(ANS)
    else:
        ANS = (h1 + 2)*(w1 + 2)-(h1 * w1)-w2-2
        ANS += ((h2 + 2) * (w2 + 2))-(h2 * w2 )-(w2+2)
        print(ANS)