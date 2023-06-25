    n = int(input())
    l = []
    res = []
def foo(k):
        global l
        global res
        if k == 0:
            if len(l) > len(res):
                res = l
            l = list()
            return
        for i in range(k // 2 + 1, k + 1):
            l.append(i)
            foo(k - i)
    foo(n)
    print(len(res))
    for i in res:
        print(i, end=" ")