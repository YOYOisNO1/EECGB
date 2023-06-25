def program77():
    n=int(input())
    st=input().split(" ")
    arr=[int(x) for x in st]
    dic={}
    for i in arr:
        dic[i]=dic.get(i,0)+1
    print(max(dic.values()))