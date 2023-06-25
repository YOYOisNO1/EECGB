def main():
        d, k, a, b, t = map(int, input().split())
        ans = 0
        dc = d//k
        dr = d % k
        if not dc:
            print(a*dr)
        else:
            way1 = dc*(k*a + t) + dr*a
            way2 = dc*(k*a + t) - t + dr*b
            way3 = k*a + (d-k)*b
            print(min(
                way1,
                way2,
                way3
            ))
    
    
    if __name__ == '__main__':
        main()