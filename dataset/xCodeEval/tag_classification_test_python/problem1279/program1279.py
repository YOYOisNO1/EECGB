def program1279():
    num_2,num_3,num_5,num_6 = map(int,input().split())
    count_32, count_256 = 0,0
    
    count_256 = min(num_2, num_5, num_6)
    num_2 -= count_256
    num_5 -= count_256
    num_6 -= count_256
    
    count_32 = min(num_2,num_3)
    
    print(256*count_256) + 32* count_32