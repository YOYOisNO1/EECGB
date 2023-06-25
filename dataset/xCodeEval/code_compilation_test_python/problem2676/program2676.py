def program2676():
    Links_and_Pearls(array)
        array = input()
        a = 0
        b = 0
        i = 0
        while(i<len(array)):
            if(array[i] == 'o'):
                a = a + 1
            else:
                b = b + 1
            i = i + 1
        if(a == 0):
            print("YES")
        else:
            if(b%a==0):
                print("YES")
            else:
                print("NO")