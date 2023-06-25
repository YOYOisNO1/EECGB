def program282():
    import sys
    import string
    
    
    if __name__ == '__main__':
    
        num1 = map(int,sys.stdin.readline().split())
    
        temp = 0
        for i in range(35):
    
            if num1[0] > temp:
                temp+=i
    
            elif num1[0] == temp:
                print("YES")
                break
            else:
                print("NO")
                break
    
    
    
    