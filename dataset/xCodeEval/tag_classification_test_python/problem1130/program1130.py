def solution(n,week):
        if n > sum(week):
            return solution(n%sum(week),week)
        elif n == 0:
            arr = []
            for k in range(len(week)):
                if week[k] > 0:
                    arr.append(k)
            return max(arr) + 1
        else:
            for i in range(len(week)):
                n -= week[i]
                if n <= 0:
                    return i+1
    print(solution(int(input()),list(map(int,input().split()))))