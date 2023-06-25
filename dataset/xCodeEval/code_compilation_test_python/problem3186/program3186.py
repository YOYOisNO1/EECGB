    import sys
    
def main():
        s = input()
        l = len(s)
        
        freq = {}
        substrings = [s[i:j+1] for i in xrange(l) for j in xrange(i, l)]
        for s in substrings:
    	freq[s] = freq.get(s, 0) + 1
        
        print max([len(s) for s, cnt in freq.items() if cnt > 1  ])
        
    if __name__ == '__main__':
        main()