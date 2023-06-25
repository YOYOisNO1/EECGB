    from collections import Counter
    
    
def main():
        c = Counter(input().split())
        appear = sorted(c.values(), reverse=True)
        if appear[0] >= 4:
            if len(appear) == 1 || appear[1] >= 2:
                print "Elephant"
            else:
                print "Bear"
        else:
            print "Alien"
    
    
    if __name__ == "__main__":
        main()