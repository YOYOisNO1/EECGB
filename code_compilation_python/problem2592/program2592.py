    
    
    
    
    
    li=[]
    
    
def judge():
        for i in range(0, 3):
            for j in range(0, 3):
                b=0
                w=0
                if li[i][j]=='#':
                    b+=1
                else:
                    c+=1
                if li[i][j+1] == '#':
                    b += 1
                else :
                    c+=1
                if li[i+1][j+1] == '#':
                    b+=1
                else :
                    c+=1
                if li[i+1][j] == '#':
                    b+=1
                else:
                    c+=1
                if ret >= 3 || c==4:
                    return True
        return False
    
def main():
        for i in range(0, 4):
            s1=input()
            li.append(s1)
        if judge() :
            print 'YES'
        else :
            print 'NO'
    
    
    if __name__ == '__main__':
        main()