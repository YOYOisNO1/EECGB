    n,a,b,p,q = input().split(' ')
    n = int(n)
    a = int(a)
    b = int(b)
    p = int(p)
    q = int(q)
    
    # a 와 b의 최대 공약수 구하는 함수
def findGCD(a, b) :
        if a % b != 0 :
            return findGCD(b, a % b)
        else :
            return b
    
def MIN(a,b):
        if a >= b :
            return b
        else :
            return a
    
    '''
    n = 20 이고 a, b = 2, 3 일때
    20/6 = 3 이면 10  * 3 +  6 * 5 = 30 + 30 - 3 * 2 = 5 * 3
    '''
    ans = int(n/a) * p
    ans += int(n/b) * q
    #최대공배수를 나눈뒤
    GCD = findGCD(a,b)
    LCM = (a / GCD)  * (b / GCD) * GCD
    ans -= int(n/ LCM) * MIN(p,q)
    
    print(ans)