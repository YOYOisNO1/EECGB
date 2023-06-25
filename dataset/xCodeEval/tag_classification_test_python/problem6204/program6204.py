def rook_moves(r1, c1, r2, c2):
        if r1 == r2 and c1 == c2:
            return 0
        elif r1 == r2 or c1 == c2:
            return 1
        else:
            return 2
    
def king_moves(r1, c1, r2, c2):
        if r1 == r2 or c1 == c2:
            return max(abs(r1 - r2), abs(c1 - c2))
        elif abs(r1 - r2) == abs(c1 - c2):
            return abs(r1 - r2)
        else:
            return max(abs(r1 - r2), abs(c1 - c2))
    
def bishop_moves(r1, c1, r2, c2):
        if r1 == r2 and c1 == c2:
            return 0
        elif (r1 + c1) % 2 != (r2 + c2) % 2:
            return 0
        elif abs(r1 - r2) == abs(c1 - c2):
            return 1
        else:
            return 2
    
def main():
        r1, c1, r2, c2 = [int(x) for x in input().split()]
        king = king_moves(r1, c1, r2, c2)
        rook = rook_moves(r1, c1, r2, c2)
        bishop = bishop_moves(r1, c1, r2, c2)
        print(rook, bishop, king)
    
    if __name__ == '__main__':
        main()