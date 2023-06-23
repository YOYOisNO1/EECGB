def program321():
    from collections import Counter as count
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    dic = count(a)
    arr = []
    for i in dic:
        arr.append(dic[i])
    print(max(arr))