    #!/usr/bin/env python
    
    from sys import stdin
    
def main():
       N, M = map(int, stdin.readline().split())
    
       if N == 1 and M == 1:
          res = 1.0
       else:
          res = 1.0/N + (N-1)*1.0/N * (M-1) * 1.0 / (M*N-1)
    
       print('%.9lf') % (res)
    
       return 0
    
    if __name__ == '__main__': main()