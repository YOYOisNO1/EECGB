    #!/usr/bin/env python
    
def main():
        n,k = map(int, input().split())
        print(n) + k - n % k
    
    if __name__ == '__main__':
        main()