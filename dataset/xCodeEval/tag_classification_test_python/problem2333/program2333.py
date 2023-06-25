def program2333():
    '''
    Created on Jan 1, 2013
    
    @author: Evan
    '''
    line0 = input()
    line1 = input()
    line2 = input()
    l0 = line0.split(" ")
    l1 = line1.split(" ")
    l2 = line2.split(" ")
    l0[0] = int(l0[0])
    l0[1] = int(l0[1])
    l0[2] = int(l0[2])
    l1[0] = int(l1[0])
    l1[1] = int(l1[1])
    l1[2] = int(l1[2])
    l2[0] = int(l2[0])
    l2[1] = int(l2[1])
    l2[2] = int(l2[2])
    
    num = (l0[1] + l0[2] + l1[2] + l1[0] + l2[0] + l2[1])/2
    
    l0[0] = num - l0[1] - l0[2]
    l1[1] = num - l1[0] - l1[2]
    l2[2] = num - l2[0] - l2[1]
    
    print(l0[0],) l0[1], l0[2]
    print(l1[0],) l1[1], l1[2]
    print(l2[0],) l2[1], l2[2]