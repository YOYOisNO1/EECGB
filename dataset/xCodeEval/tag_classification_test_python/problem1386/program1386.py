def program1386():
    month={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December',13:'January',14:'February',15:'March',16:'April',17:'May',18:'June',19:'July',20:'August',21:'September',22:'October',21:'November'}
    s=str(input())
    n=int(input())
    for key,item in month.items():
        if s in item:
            n=n%12
            print(month[n+key])
            break