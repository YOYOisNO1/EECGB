def program2931():
    line1 = input()
    line = line1.split()[0]
    numbers =[]
    n=[]
    for i in line:
        numbers.append(int(i))
    
    if(numbers[0]+numbers[1]+numbers[2] == numbers[3]+numbers[4]+numbers[5]):
        print "0"
    else:
        elif(numbers[0]+numbers[1]+numbers[2] > numbers[3]+numbers[4]+numbers[5]):
            n.append(numbers[0])
            n.append(numbers[1])
            n.append(numbers[2])
            n.append(9-numbers[3])
            n.append(9-numbers[4])
            n.append(9-numbers[5])
            diff = (numbers[0]+numbers[1]+numbers[2] - (numbers[3]+numbers[4]+numbers[5])) 
        else:
            n.append(numbers[3])
            n.append(numbers[4])
            n.append(numbers[5])
            n.append(9-numbers[0])
            n.append(9-numbers[1])
            n.append(9-numbers[2])
            diff = numbers[3]+numbers[4]+numbers[5] - (numbers[0]+numbers[1]+numbers[2])
        n1 = sorted(n)
        if(n1[5]>=diff):
            print "1"
        elif(n1[5]+n1[4]>=diff):
            print "2"
        else:
            print "3"
    