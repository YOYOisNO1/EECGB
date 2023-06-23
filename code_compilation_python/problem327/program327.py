    from sys import maxsize, stdout, stdin,stderr
    mod = int(1e9 + 7)
def tup():return map(int,stdin.readline().split())
def I(): return int(stdin.readline())
def lint(): return [int(x) for x in stdin.readline().split()]
def S(): return input().strip()
def grid(r, c): return [lint() for i in range(r)]
def debug(*args, c=6): print('\033[3{}m'.format(c), *args, '\033[0m', file=stderr)
    from  math import  log2,sqrt
    from collections import Counter,defaultdict
    from itertools import permutations
    import re
    
# def bark():
    #     n = I();    s =S()
    #     a = re.split('[A-Z]+',s)
    #     p = max(map(lambda x: len(set(x)),a))
    #     return p
    from math import floor,sqrt,ceil
    #
# def bark():
    #     n = I()
    #     s = int(sqrt(n))
    #     for i in range(s,n+1):
    #         if i*s >=n:
    #             print(2*(i+s))
    #             #find some area greater than or equal to n and then find it's perimeter since it's a rectange use 2*(l+b)
    #             break
    # if __name__ == '__main__':
    #     bark()
    #print(375.80 , 30000.30000)
    #print(1234567890000000/123456789)
    
    
def kround():
    
        n , k =tup()
        if n% pow(10,k) ==0:
            print(n)
        else:
            a = pow(10,k)
            for i in range(1,10000000000000000):
                if i%n==0 and i%a==0:
                    print(i)
                    break
            # else:
            #     num =0
            #     f=  str(n); i =0
            #     c = len(f) + k
            #     while True:
            #         num += int(f[i]) * pow(10,c)
            #         if num%n==0:
            #             #print(num)
            #             break
            #         c-=1
            #         i+=1
            #     p = str(num)
            #     j =0
            #     flag = 1
            #     for i in range(len(p)):
            #         for j in range(i+1):
            #             if len(p[:j]) >0:
            #                 #print(int(p[:j]))
            #                 if int(p[:j]) % pow(10,k)==0:
            #                     print(p[:j])
            #                     flag = 0
            #                     break
            #         if flag==0:break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if __name__ == '__main__':
        kround()