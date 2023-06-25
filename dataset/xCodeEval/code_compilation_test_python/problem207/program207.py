def program207():
    s = str(input())
    test= 'abcdefghijklmnopqrstuvwxyz'
    current_pos=0
    minimum_dis = 0
    for i in s:
        x =test.find(i)+1
        y=test[::-1].find(i)+1
        minimum_dis = minimum_dis + min(x,y)
        index= test.find(i)
        test = test[index:] + test[:index]
    print(minimum_dis-1)