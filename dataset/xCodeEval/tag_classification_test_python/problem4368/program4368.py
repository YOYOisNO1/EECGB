def func(n):
        distance = min((ord(n[0])-96) - (ord('a')-96) , 26 - abs((ord('a')-96)-(ord(n[0])-96)))
        for i in range(len(n)-1):
            right_distance = abs((ord(n[i])-96)-(ord(n[i+1])-96))
            left_distance = 26 - abs((ord(n[i])-96)-(ord(n[i+1])-96))
            distance += min(right_distance,left_distance)
        print(distance)
    n = input()
    func(n)