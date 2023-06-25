def program286():
    n,k = map(int, input().split())
    scores = list(map(int, input().split()))
    for i,s in enumerate(scores):
        scores[i] = (s,i)
    scores.sort()
    p = [scores[0][1]]
    for i in range(1, len(scores)):
        if scores[i][0] != scores[i-1][0]:
            p.append(scores[i][1])
    if len(p) >= k:
        print("YES")
        print(" ".join(map(lambda x: str(x+1), p[:k])))
    else:
        print("NO")
         