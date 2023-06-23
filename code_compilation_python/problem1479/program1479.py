def main():
        p, d = map(int, input().split())
    
        MAX = -1
        VALUE = None
    
        for x in xrange(p - d, p + 1):
            value = 0
            s = str(x)
            i = len(s) - 1
            while i >= 0 and s[i] == '9':
                value += 1
                i -= 1
            if value >= MAX:
                VALUE = x
                MAX = value
        return VALUE
    
    if __name__ == '__main__':
        print main()