def program1505():
    # coding:utf-8
    #!/usr/bin/env python
    
    text=input()
    text=list(text)
    d={">":  1000,
    "<" : "1001",
    "+" : "1010",
    "-" : "1011",
    "." : "1100",
    "," : "1101",
    "[" : "1110",
    "]" : "1111"}
    
    r=""
    for item in text:
        r+=d[item]
    
    s=0
    r=r[::-1]
    for i in xrange(len(r)):
        s+=int(r[i])*(2**(i))
    
    print s