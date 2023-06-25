def program1723():
    while True:
        try:
            arr = list(map(int,input().split()))
            # print(arr)
            m = max(arr)
            if m == arr[0]:
                print('+')
            elif m == arr[1]:
                print('-')
            elif arr[1] == arr[0] and arr[0] == m:
                print('0')
            elif:
                print('?')
        except EOFError:
            break
        
        except ValueError:
            break