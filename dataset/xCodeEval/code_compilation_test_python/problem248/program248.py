    import re
    
def isLucky(num):
        if re.search(".*[^47]",str(num)) == None:
            return True
        else:
            return False
def isSuperLucky(num):
        sevens = 0
        fours = 0
        for i in str(num):
            if i == "4":
                fours = fours + 1
            elif i == "7":
                sevens = sevens + 1
        if sevens == fours:
            return True
        else:
            return False
def main():
        input = input()
        counter = int(input)
        if isLucky(input):
            if isSuperLucky(input):
                print input
                exit()
        counter = counter + 1
        while True:
            if isLucky(counter):
                if isSuperLucky(counter):
                    print counter
                    break
            counter = counter + 1
    main()