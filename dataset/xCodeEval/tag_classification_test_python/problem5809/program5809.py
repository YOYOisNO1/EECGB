    #!/usr/bin/env python
    
    from sys import stdin, stderr
    
def main():
       N = int(stdin.readline())
       A = map(int, stdin.readline().split())
    
       print('Alice') if A.count( min(A) ) <= N/2 else 'Bob'
    
       return 0
    
    if __name__ == '__main__': main()