def program1469():
    a = input().split()
    
    c1 = a[0] == a[1] == a[2] == a[3]
    c2 = a[8] == a[9] == a[10] == a[11]
    c3 = a[12] == a[13] == a[6] == a[7]
    c4 = a[4] == a[5] == a[18] == a[19]
    c5 = a[16] == a[17] == a[22] == a[23]
    c6 = a[20] == a[21] == a[14] == a[15]
    
    c1 = c1
    c2 = c2
    c7 = a[4] == a[5] == a[14] == a[15]
    c8 = a[12] == a[13] == a[22] == a[23]
    c9 = a[20] == a[21] == a[18] == a[19]
    c10 = a[16] == a[17] == a[6] == a[7]
    
    c11 = a[4] == a[5] == a[6] == a[7]
    c12 = a[20] == a[21] == a[22] == a[23]
    c13 = a[8] == a[9] == a[17] == a[19]
    c14 = a[16] == a[18] == a[0] == a[1]
    c15 = a[2] == a[3] == a[12] == a[14]
    c16 = a[13] == a[15] == a[10] == a[11]
    
    c11 = c11
    c12 = c12
    c17 = a[8] == a[9] == a[12] == a[14]
    c18 = a[13] == a[15] == a[0] == a[1]
    c19 = a[2] == a[3] == a[17] == a[19]
    c20 = a[16] == a[18] == a[10] == a[11]
    
    c21 = a[12] == a[13] == a[14] == a[15]
    c22 = a[16] == a[17] == a[18] == a[19]
    c23 = a[8] == a[10] == a[5] == a[7]
    c24 = a[4] == a[6] == a[1] == a[3]
    c25 = a[0] == a[2] == a[20] == a[22]
    c26 = a[21] == a[23] == a[9] == a[11]
    
    c21 = c21
    c22 = c22
    c27 = a[8] == a[10] == a[20] == a[22]
    c28 = a[21] == a[23] == a[1] == a[3]
    c29 = a[0] == a[2] == a[5] == a[7]
    c30 = a[4] == a[6] == a[9] == a[11]
    
    case1 = c1 and c2 and c3 and c4 and c5 and c6
    case2 = c1 and c2 and c7 and c8 and c9 and c10
    case3 = c11 and c12 and c13 and c14 and c15 and c16
    case4 = c11 and c12 and c17 and c18 and c19 and c20
    case5 = c21 and c22 and c23 and c24 and c25 and c26
    case6 = c21 and c22 and c27 and c28 and c29 and c30
    
    if case1 or case2 or case3 or case4 or case5 or case6:
        print('YES')
    else:
        print('NO')