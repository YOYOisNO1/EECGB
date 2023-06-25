    line = input().split(' ')
    n = int(line[0])
    a = int(line[1])
    b = int(line[2])
    p = int(line[3])
    q = int(line[4])
    
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
    
    ans = int(n/a) * p
    ans += int(n/b) * q
    # 최대공배수를 나눈뒤
    GCD = findGCD(a,b)
    LCM = (a / GCD)  * (b / GCD) * GCD
    ans -= int(n/ LCM) * MIN(p,q)
    
    print(ans)