def program744():
    
     from sys import stdin, stdout
    n = stdin.readline()
    s1 = "Danil"
    s2 = "Olya"
    s3 = "Slava"
    s4 = "Ann"
    s5 = "Nikita"
    
    count1 = n.count(s1)
    count2 = n.count(s2)
    count3 = n.count(s3)
    count4 = n.count(s4)
    count5 = n.count(s5)
    
    if (count1+count2+count3+count4+count5) == 1:
        stdout.write("YES")
    else:
        stdout.write("NO")