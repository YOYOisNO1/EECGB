def program1900():
    line = input()
    a1,b1 = [int(x) for x in line.split()]
    line = input()
    a2,b2 = [int(x) for x in line.split()]
    line = input()
    a2,b2 = [int(x) for x in line.split()]
    if a2+a3<=a1 and b2+b3<=b1 or a2+a3<=b1 and b2+b3<=a1 or a2+b3<=a1 and b2+a3<=b1 or a2+b3<=b1 and b2+a3<=a1:
        print 'YES'
    else:
        print 'NO'