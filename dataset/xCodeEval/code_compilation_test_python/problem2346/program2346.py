    str1, str2 = map(str, input().split())
    
    # 对每一个s2和s1不一样的字符，这个是字符是ans的一部分
    
def f(s1, s2):
        if s1 != s2:
            return s2
        else:
            return ' '
    
    
    ss = [f(str1[i], str2[i]) for i in range(len(str1))]
    
    # ss[i]不是空格证明是str2的一部分
    # 是空格就换成比str1[i]小的数
    
    # print(ss)
    
    for i in range(len(ss)):
        if(ss[i] == ' ' and str1[i] == 'a') or (abs(ord(ss[i]) - ord(str1[1])) == 1):
            ss = "-1"
            break
        elif(ss[i] == ' '):
            ss[i] = chr(ord(str1[i]) + 1)
    
    print(''.join(ss))