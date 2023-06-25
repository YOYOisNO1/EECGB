def loops(k):
        if(k>36):
            return -1
        else:
            two,one,number="8","9",""
            while(k>0):
                if(k>=2):
                    number += two
                    k = k - 2
                else:
                    number += one
                    k = k - 1
            return int(number)
            
    k = int(input())
    print(loops(k))