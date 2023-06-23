def main():
        a =[]
        for i in range(3):
            a.append(map(int,input().split())))
        a[0][0] = int((a[1][2] + a[2][1])/2)
        a[2][2] = int((a[0][1] + a[1][0])/2)
        a[1][1] = int((a[0][1] + a[2][1])/2)
        for i in range(3):
            print(' '.join([str(x) for x in a[i]]))
    
    main()