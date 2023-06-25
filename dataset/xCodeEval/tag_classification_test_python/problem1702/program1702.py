def count(k):
        answer = [100]
        if 100 % k == 0:
            answer.append(100 // k)
        if k % 25 == 0:
            answer.append(4)
        if k % 20 == 0:
            answer.append(5)
        if k % 50 == 0:
            answer.append(2)
        if k % 10 == 0:
            answer.append(10)
        if k % 2 == 0:
            answer.append(50)
        if k % 4 == 0:
            answer.append(25)
        if k % 5 == 0:
            answer.append(20)
        return round(min(answer))
    
    
    t = int(input())
    for i in range(t):
        k = int(input())
        print(count(k))