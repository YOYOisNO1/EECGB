def program2950():
    from math import *;print(lambda(x,y):(lambda r:['black','white'][r!=int(r) and(1-int(r)%2)^(y/x>0)])(sqrt(x**2+y**2)))(map(float,input().split()))