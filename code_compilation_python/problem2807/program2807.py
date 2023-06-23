     Getting Chess Board from Codeforces.
    chessBoard = []
    for i in range (8):
        chessBoard.append(list(input()))
    # Counting Number of Black Tiles.
    blackTileCount = 0
    for i in range(8):
        blackTileCount+=chessBoard[i].count('B')
    # Function to extract Column "j" from chessBoard.
def extractColumn(j):
        colString = ""
        for x in range(8):
            colString+=chessBoard[x][j]
        return colString
    # Painting Rows.
    paintedCount = 0
    for i in range(8):
        rowString = "".join(chessBoard[i])
        if rowString == "BBBBBBBB":
            paintedCount+=1
    # Exiting Program if all black Tiles painted.
    if 8*paintedCount == blackTileCount:
        exit()
    # Painting Columns.
    for i in range(8):
        colString = extractColumn(i)
        if colString == "BBBBBBBB":
            paintedCount+=1
    # Verdict.
    print(paintedCount)