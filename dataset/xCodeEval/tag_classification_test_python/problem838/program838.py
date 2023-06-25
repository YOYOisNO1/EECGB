def main():
        v1, v2 = (int(i) for i in input().split())
        t, d = (int(i) for i in input().split())
    
        res = 0
        for i in range(t):
            res += min(v1 + d*i, v2 + d*(t - i - 1))
        print(res)
    
    if __name__ == '__main__':
        main()