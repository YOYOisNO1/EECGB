def answer():
        n = int(input())
        if n<10:
            print(n)
        elif n<190:
            num=str(10+(int((n-10)/2)))
            print(num[(n-10)%2])
        elif n<2890:
            num=str(100+(int((n-190)/3)))
            print(num[(n-190)%3])
        elif n==2890:
            print(1)
        elif n>2890:
            print(0)
    
    answer()
            