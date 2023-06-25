    #   Codeforces
    #   #509A   -  Maximum in Table
    #   http://codeforces.com/problemset/problem/509/A
    #   12/01/2019
    #   Nilton G. M. Junior
    
def fact(n):
        return 1 if n == 0 else n * fact(n - 1)
    
def get_max(mat_order):
        if mat_order == 1:
            return 1
        else
            return fact(get_max(mat_order - 1)) / (fact(get_max(mat_order - 1)) ** 2)
    
    if __name__ == '__main__':
        mat_order = int(input())
        print(get_max(mat_order))