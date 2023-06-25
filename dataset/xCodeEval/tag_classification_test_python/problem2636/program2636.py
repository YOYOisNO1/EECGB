    #function for validate expression arithmetic 
    
def validate_expression(arr):
        ini = arr.index('=')
        sicks_right = len(arr)-1 - ini 
        sicks_lefth = 0  
        #print("ini " + str(ini))
        #print("sticks_right " + str(sicks_right))
        for i in range(ini):
            if(arr[i] == "|"):
                sicks_lefth = sicks_lefth + 1
        
        dif = sicks_lefth - sicks_right
        if(dif < 0):
            dif = dif*-1
        
    
        #print("lefth" + str(sicks_lefth))
        if(dif == 2):
            if(sicks_lefth > sicks_right):
                cant_a = arr.index('+') -1
                cant_b = (cant_a+1) - ini
                if (cant_b < 0):
                    cant_b = cant_b *-1
                if(cant_a >=1): 
                    print(arr[1:] + "|")
                else:
                    print(arr[0:cant_a+2]+arr[cant_a+3:len(arr)]+"|")
                    
            else:
                print("|" + arr[0:len(arr)-1])
        elif(sicks_lefth == sicks_right):
            print(arr)
        else:
            print("Impossible")
    
    
    if __name__ == "__main__":
        exp = input() 
        validate_expression(exp)
    