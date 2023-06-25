    year = input();
    
def isNext(y):
        if len(y) == 1: return True;
        if y[0] in y[1:len(y)]: return False;
        else: return isNext(y[1:len(y)]);
    
    for i in range(int(year)+1,9013):
        if isNext(str(i)):
            print(i;)
            break;