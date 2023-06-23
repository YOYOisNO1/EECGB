def program569():
    sa=input()
    count=0
    count1=0
    for i in range(len(sa)):
     if sa[i].isupper():
       count+=1 
      if sa[i].islower():
       count1+=1 
    if count > count1:
        print(sa.upper())
    else :
        print(sa.lower())