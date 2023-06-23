def program3674():
    import sys
    import re
    
    line1 = sys.stdin.readline()
    line2 = sys.stdin.readline()
    
    point1 = map(int, re.findall(r'\d+', line1))
    point2 = map(int, re.findall(r'\d+', line2))
    
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    
    
    diagonalSteps = min(abs(y2)-abs(y1), abs(x2)-abs(x1))
    remainingSteps = max(abs(y2)-abs(y1), abs(x2)-abs(x1)) - diagonalSteps
    
    print(diagonalSteps+remainingSteps)