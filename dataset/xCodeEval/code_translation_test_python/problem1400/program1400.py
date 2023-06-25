def program1400():
    n = int(input())
    s = input()
    summ = 0
    for i in range(len(s)):
        if s[i:i+3] == 'xxx':
            summ+=1
    print(summ)