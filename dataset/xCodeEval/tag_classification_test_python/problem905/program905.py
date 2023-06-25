def solve(n):
    
        height = boxesUsed = prevStepBoxes = 0
    
        while n > boxesUsed:
    
            height += 1
            thisStepBoxes = prevStepBoxes + height
            boxesUsed += thisStepBoxes
            prevStepBoxes = thisStepBoxes
    
            #if this layer is not possible, we over-estimated the height. Reduce it by 1
            if n < boxesUsed:
                height -= 1
    
        return height
    
    
    if __name__ == "__main__":
        n = int(input())
        print(solve(n))