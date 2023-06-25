def maths(l,n,k,r):
        while l != r:
            x = middle = (l + r) // 2
            sum = 0
            while x != 0:
                sum += x
                x //= k
            if sum >= n:
                r = middle
            else:
                l = middle + 1
        return l
    
def main():
        n,k = map(int,input().split()) 
        l, r = 1, n
        print(maths(l,n,k,r))
    
    
    if __name__ == '__main__':
        main()