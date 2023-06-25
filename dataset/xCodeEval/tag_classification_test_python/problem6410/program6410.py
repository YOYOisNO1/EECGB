    # python 3
    """
    Read tutorial, graph the moves
    """
    
    
def inna_and_pink_pony(n_int, m_int, i_int, j_int, a_int, b_int) -> str:
        corner_1 = (1, 1)
        corner_2 = (1, m_int)
        corner_3 = (n_int, 1)
        corner_4 = (n_int, m_int)
        corners = [corner_1, corner_2, corner_3, corner_4]
        c = max(n_int, m_int)
        for each in corners:
            if abs(each[0] - i_int) % a_int != 0 or abs(each[1] - j_int) % b_int != 0:
                continue
            horizontal_moves = abs(each[0] - i_int) // a_int
            vertical_moves = abs(each[1] - j_int) // b_int
            if horizontal_moves % 2 != vertical_moves % 2:
                continue
            each_move = max(horizontal_moves, vertical_moves)
            if (a_int > max(i_int - 1, n_int - i) and abs(each[1] - j_int) > 0) or (
                    b_int > max(j - 1, m - j) and abs(each[0] - i_int) > 0):
                break
            c = min(c, each_move)
    
        if c < max(n_int, m_int):
            return c
        else:
            return "Poor Inna and pony!"
        
    
    if __name__ == "__main__":
        """
        Inside of this is the test. 
        Outside is the API
        """
    
        n, m, i, j, a, b = list(map(int, input().split()))
    
        print(inna_and_pink_pony(n, m, i, j, a, b))
    
        # print(inna_and_pink_pony(n, m, i, j, a, b))