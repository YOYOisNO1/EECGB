    
    
def main():
        x = str(input())
        n = int(x, 2)
        
        n <<= len(x) - 1
        n %= 10**9 + 7
        print n
    
    if __name__ == '__main__':
        main()