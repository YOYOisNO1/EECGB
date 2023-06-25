def z(a):
        if a==0:return 1
        elif a<=9:return a
        else: return max(a%10 * z(a//10),9*z(a//10-1))
    print(z(int(input())))