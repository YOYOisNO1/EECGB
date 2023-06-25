    """This script is a solution for A problem Codeforces round 374"""
    
def main():
        """Main function"""
        size = int(input())
        cw = input()
        black = False
        cnt = 0
        size = 0 
        result = []
        for w in cw:
            if black and w == "B":
                size += 1
            elif black and w == "W":
                result.append(size)
                size = 0
                black = False
            elif (not black) and w == "B":
                cnt += 1
                size += 1
                black = True
            elif (not black) and w == "W":
                pass
        if black:
                result.append(size)
    
        print(cnt)
        print(' ').join(str(x) for x in result)
    
    if __name__ == '__main__':
        main()