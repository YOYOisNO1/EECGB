def find(x,y,z,a,b,c):
       
        a_dis = x-a
        if a_dis <= 0:
         d_dis = y - b - a_dis
            if d_dis <= 0:
               m_dis = z - c - d_dis
               if m_dis <= 0:
                  return("YES")
    return("NO") 
    
    x,y,z = map(int(input.split()))
    a,b,c = map(int(input.split()))
    
    print(find(x,y,z,a,b,c))