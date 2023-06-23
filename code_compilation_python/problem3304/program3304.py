def program3304():
    k,g = list(map,input().split(" ")
    h = input()
    v = input()
    if(
       (h[0]  =='<' and v[0]  =='^') or
       (h[0]  =='>' and v[0]  =='v') or
       (h[-1] =='<' and v[-1] =='^') or
       (h[-1] =='>' and v[-1] =='v') or
       (h[-1] =='>' and v[0]  =='^') or
       (h[-1] =='<' and v[0]  =='v') or
       (h[0]  =='>' and v[-1] =='^') or
       (h[0]  =='<' and v[-1] =='v')
    ): 
        print("NO")
    else: 
        print("YES")