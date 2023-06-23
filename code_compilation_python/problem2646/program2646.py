    import sys
    
    l1,l2=[a.strip() for a in sys.stdin.readlines()]
    
def pos(astr):
     x=ord(astr[0])-ord("a")
     y=int(astr[1])
     return [x,y]
    pos1=pos(l1)
    pos2=pos(l2)
    as=[]
    l=0
    while pos1!=pos2:
      a=""
      if pos1[0]<pos2[0]:
        pos1=[pos1[0]+1,pos1[1]]
        a+="R"
      elif pos1[0]>pos2[0]:
        pos1=[pos1[0]-1,pos1[1]]
        a+="L"
      if pos1[1]<pos2[1]:
        pos1=[pos1[0],pos1[1]+1]
        a+="U"
      elif pos1[1]>pos2[1]:
        pos1=[pos1[0],pos1[1]-1]
        a+="D"
      l+=1
      as.append(a)
      
    print l
    for a in as:print a