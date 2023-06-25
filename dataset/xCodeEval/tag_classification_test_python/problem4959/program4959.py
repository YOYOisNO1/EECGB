def program4959():
    n1=input()
    nn1=[]
    nn2=[]
    nn3=[]
    if n1[1] == '<':
        nn1=[n1[2],n1[0]]
    else:
        nn1=[n1[0],n1[2]]
        
    n2=input()
    if n2[1] == '<':
        nn2=[n2[2],n2[0]]
    else:
        nn2=[n2[0],n2[2]]
        
    n3=input()
    if n3[1] == '<':
        nn3=[n3[2],n3[0]]
    else:
        nn3=[n3[0],n3[2]]
    
    str1=[]
    
    #print(nn1)
    #print(nn2)
    #print(nn3)
    
    if nn1[0] == nn2[0]:
        if nn3[0] == nn1[1]:
            str1=[nn1[0],nn1[1],nn3[1]]
            t=str1[2]+str1[1]+str1[0]
            print(t)
        elif nn3[0] == nn2[1]:
            str1=[nn2[0],nn2[1],nn3[1]]
            t=str1[2]+str1[1]+str1[0]
            print(t)
    elif nn2[0] == nn3[0]:
        if nn1[0] == nn2[1]:
            str1=[nn2[0],nn2[1],nn1[1]]
            t=str1[2]+str1[1]+str1[0]
            print(t)
        elif nn1[0] == nn3[1]:
            str1=[nn3[0],nn3[1],nn1[1]]
            t=str1[2]+str1[1]+str1[0]
            print(t)
    elif nn3[0] == nn1[0]:
        if nn2[0] == nn3[1]:
            str1=[nn3[0],nn3[1],nn2[1]]
            t=str1[2]+str1[1]+str1[0]
            print(t)
        elif nn2[0] == nn1[1]:
            str1=[nn1[0],nn1[1],nn2[1]]
            t=str1[2]+str1[1]+str1[0]
            print(t)
    #elif nn1[0] != nn2[0] & nn1[0] != nn3[0] & nn2[0] != nn3[0]:
    else:
        print("Impossible")