def program2119():
    if __name__ == "__main__":
        n, d = map(int,input().split())
        costs = map(int, input().split())
        m = int(input())
        ans = 0
        if m < n:
            ans = sum(costs[:m])
        else:
            ans = sum(costs)
            ans -= (m-n)*d
        print ans