    #!/usr/bin/python
    
    # -*- coding: koi8-r -*-
    
def main():
        a = input()
        b = input()
        a = [int(i) for i in a.strip().split()]
        b = [int(i) for i in b.strip().split()]
        
        if b[0]-a[1]>=3 and b[1]-a[0]>=3:
            print 'NO'
        elif a[0]-b[1]>=2 and a[1]-b[0]>=2:
            print 'NO'
        else:
            print 'YES'
    
    if __name__ == '__main__':
        main()