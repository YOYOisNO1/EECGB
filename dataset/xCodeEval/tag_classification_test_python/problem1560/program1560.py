def program1560():
    #Vitaly and strings: http://codeforces.com/problemset/problem/518/A
    import copy
    
    
    if __name__ == '__main__':
        input1 = list(input())
        input2 = list(input())
        flag = False 
        for i in range(len(input1)-1,-1,-1):
            if input1[i] == 'z':
                input1[i] = 'a'
            else:
                input1[i] = chr(ord(input1[i]) + 1)
                break 
        
        for j in range(len(input1)):
            if input1[j] < input2[j]:
                flag = True 
                break  
    
        if flag:
            print(''.join(input1))
        else:
            print('No such string')
        
        
       