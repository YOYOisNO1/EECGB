def program2939():
    digit = ['zero' , 'one' , 'two' , 'three' , 'four ', 'five' ,'six' , 'seven', 'eight', 'nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens = ['zero', 'ten', 'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    n = input()
    if n%10==0:
        print(tens[n/10])
    elif n <20:
        print(digit[n])
    else:
        print(tens[n/10]+'-'+digit[n%10])