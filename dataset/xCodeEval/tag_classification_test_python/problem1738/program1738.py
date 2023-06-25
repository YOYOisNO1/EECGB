    #! /usr/bin/env python3
    
    
def read(type_):
        data = [type_(x) for x in input().split()]
        if len(data) == 1:
            return data[0]
        else:
            return data
    
    
def main():
        l, r, x, y, k = read(int)
        for i in range(x, y + 1):
            if i * k in range(l, r + 1):
                print('yes')
                break
        else:
            print('no')
    
    
    if __name__ == '__main__':
        main()