    
    
    
def main():   
        inputline = input()
        spline = inputline.split(' ')
        adult = int(spline[0])
        child = int(spline[1])
        if adult == 0 :
            print "impossible"
        else:
            if adult < child :
                minimum = child
            else:
                minimum =  adult
            
            maximun = adult + child -1
            print str(minimum) + ' ' + str(maximum)
    
            
        
    
    
    
    
    if __name__ == "__main__":
        main()