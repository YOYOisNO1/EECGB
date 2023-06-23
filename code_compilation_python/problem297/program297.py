    import sys
def wincases(arr):
        i=0
        while i<9:
            if arr[i]==arr[i+1]==arr[i+2] and arr[i]!='.':
                return arr[i]
            i=i+3
        for i in range (0,3):
            if arr[i]==arr[i+3]==arr[i+6] and arr[i]!='.':
                return arr[i]
        if arr[0]==arr[4]==arr[8] and arr[0]!='.':
            return arr[4]
        if arr[2]==arr[4]==arr[6] and arr[2]!='.':
            return arr[4]
        return '.'
    
def invalid(nX,n0):
        if nX-n0>1:
            return True
        return False
    
def counter(arr):
        nX=n0=0
        for i in range (0,9):
            if arr[i]=='X':
                nX=nX+1
            if arr[i]=='0':
                n0=n0+1
        return (nX,n0)
    
def main():
        arr=''
        for line in sys.stdin:
            arr=arr+line
            arr=arr.rstrip()
        nX,n0=counter(arr)
        #verficamos si es valido
        if invalid(nX,n0) == False:
            win=wincases(arr)
            #no se define ganador todavia
            if win == '.':
                #no hay empate
                if nX+n0!=9:
                    if nX==n0:
                        print('first')
                    else:
                        print('second')
                else:
                    print('draw')
            else:
                if win=='X':
                    print('the first player won')
                print('the second player won')
        else:
            print('illegal')
        print(n0,nX)
        a=input()
    
    if __name__ == '__main__':
        main()