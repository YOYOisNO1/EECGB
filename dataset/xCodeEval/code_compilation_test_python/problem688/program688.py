def program688():
    n=int(input())
    w=input().split()
    w=list(w)
    if len(w)==1:
        if w[-1]=='15':
            print('DOWN')
        elif:w[-1]=='0':
            print('UP')
        else:
            print('-1')
    else:
         if w[-1]=='15':
             print('DOWN')
         else:
             if int(w[-1])<int(w[-2]):
                print('DOWN')
             elif int(w[-1])>int(w[-2]):
                print('UP')