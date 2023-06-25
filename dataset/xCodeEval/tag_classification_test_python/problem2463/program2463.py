    import logging
    import copy
    import sys
    import math
    
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    
#def solve(firstLine):
def solve(lines):
        wordsSet = set()
    
        wordMax = 0
        
    
        inWords = 0
        inParent = False
        noParent = 0
        inSidx = 0
        sidx = 0
        for idx, ch in  enumerate(lines):
            if ch == '(':
                if inParent == False:
                    inSidx=idx
                    for word in lines[sidx:idx].replace("_", " ").replace("(", " ").replace(")", " ").split():
                        wordMax = max([wordMax, len(word)])
                    
                inParent=True
                noParent+=1
            elif ch ==')':
                noParent-=1
                if noParent == 0:
                    inParent = False
                    sidx=idx
                    inWords += len(lines[inSidx:idx].replace("_", " ").replace("(", " ").replace(")", " ").split())
    
        if inParent == False:
            for word in lines[sidx:].replace("_", " ").replace("(", " ").replace(")", " ").split():
                wordMax = max([wordMax, len(word)])
                        
        print("%d %d" % (wordMax, inWords))
        
def main():
        firstLine = input()
        solve(input())
        
    
def log(*message):
        logging.debug(message)
        
    if __name__ == "__main__":
        main()
     