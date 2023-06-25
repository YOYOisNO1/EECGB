    minimo=-1
def find_min(a_s,a_f,a_c,b_s,b_f,b_c,ordine,prossimo,antenato):
        global minimo
        #print("Vengo da::: "+antenato)
        if(prossimo==3):
            #print("---")
            #print("%d %d %d" % (a_s,a_f,a_c))
            #print("%d %d %d" % (b_s,b_f,b_c))
            #print("---")
            valore=max(a_s,a_f,a_c)
            if(minimo<0):
                minimo=valore
            else:
                if(valore<minimo):
                    minimo=valore
    
        else:
            elem=ordine[prossimo]
            if(elem=="s"):
                c_a_s,c_b_s,c_b_c=a_s,b_s,b_c
    
                tmin=min(c_a_s,c_b_s)
                c_a_s-=tmin
                c_b_s-=tmin
                if(c_a_s>0):
                    tmin=min(c_a_s,c_b_c)
                    c_a_s-=tmin
                    c_b_c-=tmin
                
                #print(elem)
                #print("%d %d %d" % (c_a_s,a_f,a_c))
                #print("%d %d %d" % (c_b_s,b_f,c_b_c))
                find_min(c_a_s,a_f,a_c,c_b_s,b_f,c_b_c,ordine,prossimo+1,elem)
                
                tmin=min(a_s,b_c)
                a_s-=tmin
                b_c-=tmin
                if(a_s>0):
                    tmin=min(a_s,b_s)
                    a_s-=tmin
                    b_s-=tmin
    
                #print(elem)
                #print("%d %d %d" % (a_s,a_f,a_c))
                #print("%d %d %d" % (b_s,b_f,b_c))
                find_min(a_s,a_f,a_c,b_s,b_f,b_c,ordine,prossimo+1,elem)
    
            if(elem=="f"): 
                c_a_f,c_b_f,c_b_s=a_f,b_f,b_s
                
                tmin=min(c_a_f,c_b_f)
                c_a_f-=tmin
                c_b_f-=tmin
                if(c_a_f>0):
                    tmin=min(c_a_f,c_b_s)
                    c_a_f-=tmin
                    c_b_s-=tmin
    
                #print(elem)
                #print("%d %d %d" % (a_s,c_a_f,a_c))
                #print("%d %d %d" % (c_b_s,c_b_f,b_c))
                find_min(a_s,c_a_f,a_c,c_b_s,c_b_f,b_c,ordine,prossimo+1,elem)
                
                tmin=min(a_f,b_s)
                a_f-=tmin
                b_s-=tmin
                if(a_f>0):
                    tmin=min(a_f,b_f)
                    a_f-=tmin
                    b_f-=tmin
    
                #print(elem)
                #print("%d %d %d" % (a_s,a_f,a_c))
                #print("%d %d %d" % (b_s,b_f,b_c))
                find_min(a_s,a_f,a_c,b_s,b_f,b_c,ordine,prossimo+1,elem)
            
            if(elem=="c"):
                c_a_c,c_b_c,c_b_f=a_c,b_c,b_f
    
                tmin=min(c_a_c,c_b_c)
                c_a_c-=tmin
                c_b_c-=tmin
                if(c_a_c>0):
                    tmin=min(c_a_c,c_b_f)
                    c_a_c-=tmin
                    c_b_f-=tmin
    
                #print(elem)
                #print("%d %d %d" % (a_s,a_f,c_a_c))
                #print("%d %d %d" % (b_s,c_b_f,c_b_c))
                find_min(a_s,a_f,c_a_c,b_s,c_b_f,c_b_c,ordine,prossimo+1,elem)
                
                tmin=min(a_c,b_f)
                a_c-=tmin
                b_f-=tmin
                
                if(a_c>0):
                    tmin=min(a_c,b_c)
                    a_c-=tmin
                    b_c-=tmin
    
                #print(elem)
                #print("%d %d %d" % (a_s,a_f,a_c))
                #print("%d %d %d" % (b_s,b_f,b_c))
                find_min(a_s,a_f,a_c,b_s,b_f,b_c,ordine,prossimo+1,elem)
    
    
    
    n=int(input())
    
    la=input().strip().split(" ")
    lb=input().strip().split(" ")
    
    
    a_s,a_f,a_c = int(la[0]), int(la[1]), int(la[2])
    b_s,b_f,b_c = int(lb[0]), int(lb[1]), int(lb[2])
    
    #print("%d %d %d" % (a_s,a_f,a_c) )
    #print("%d %d %d" % (b_s,b_f,b_c) )
    
    diz={}
    diz["s"]=[a_s,b_s]
    diz["f"]=[a_f,b_f]
    diz["c"]=[a_c,b_c]
    
    ll=[ "sfc","scf","fsc","csf","fcs","cfs" ]
    
    for ordine in ll:
        #print(ordine)
        find_min(a_s,a_f,a_c,b_s,b_f,b_c,list(ordine),0,"ORI")
    
    
    massimo=0
    if(a_s>b_f):
        massimo+=b_f
    else:
        massimo+=a_s
    if(a_f>b_c):
        massimo+=b_c
    else:
        massimo+=a_f
    if(a_c>b_s):
        massimo+=b_s
    else:
        massimo+=a_c
    
    
    #massimo=max(a_s,b_f)+max(a_f,b_c)+max(a_c,b_s)
    print("%d %d" % (minimo,massimo))