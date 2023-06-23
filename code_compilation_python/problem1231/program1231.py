def program1231():
    #coding: utf-8
    
    n = int(input())
    seq = input()
    
    new_seq = ""
    while len(seq) > 1:
        temp = seq[i] + seq[i+1]
        if temp in ["RU", "UR"]:
            new_seq += "D"
            seq = seq[2::]
        else:
            new_seq += seq[i]
            seq = seq[1::]
    
    if n % 2 != 0:
        new_seq += seq[-1]
    
    print len(new_seq)