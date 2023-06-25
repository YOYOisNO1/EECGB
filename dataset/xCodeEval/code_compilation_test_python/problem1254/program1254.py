    # -*- coding: utf-8 -*-
    """
    @Project : CodeForces
    @File    : 994C - Two Squares.py
    @Time    : 2018/6/17 2:33
    @Author  : Koushiro
    
    http://codeforces.com/contest/994/problem/C
    """
    
    # 二维向量的外积
def two_dimen_cross_product(vectors_A,vectors_B):
        return vectors_A[0]*vectors_B[1]-vectors_A[1]*vectors_B[0]
    
    # 矩阵的点可以顺时针或逆时针按A、B、C、D依次存储
def point_in_rectangle(point,rect):
        AB=[rect[1][0]-rect[0][0],rect[1][1]-rect[0][1]]
        DC=[rect[2][0]-rect[3][0],rect[2][1]-rect[3][1]]
        AP=[point[0]-rect[0][0],point[1]-rect[0][1]]
        DP=[point[0]-rect[3][0],point[1]-rect[3][1]]
    
        BC=[rect[2][0]-rect[1][0],rect[2][1]-rect[1][1]]
        AD=[rect[3][0]-rect[0][0],rect[3][1]-rect[0][1]]
        BP=[point[0]-rect[1][0],point[1]-rect[1][1]]
    
        if two_dimen_cross_product(AB,AP)*two_dimen_cross_product(DC,DP)>0:
            return False
        elif two_dimen_cross_product(BC,BP)*two_dimen_cross_product(AD,AP)>0:
            return False
        else:
            return True
    
    if __name__ == "__main__":
        a = [[0, 0] for i in range(4)]
        b = [[0, 0] for i in range(4)]
        a_tmp = list(map(int, input().split()))
        b_tmp = list(map(int, input().split()))
        for i in range(4):
            for j in range(2):
                a[i][j] = a_tmp[i * 2 + j]
        for i in range(4):
            for j in range(2):
                b[i][j] = b_tmp[i * 2 + j]
    
        result = "NO"
        for i in range(4):
            if point_in_rectangle(a[i],b):
                result="YES"
                break
        for i in range(4):
            if point_in_rectangle(b[i],a):
                result="YES"
                break
        # b_x = b[1][0]
        # for i in range(4):
        #     if abs(a[i][0] - b_x) * abs(abs[i][1] - b_y) <= 0.5 * ((b[0][1] - b[1][1]) * (b[1][0] - b[0][0])):
        #         result = "YES"
    
        print(result)