    import math
    import time
    
    
def input_int():
        return int(input())
    
    
def input_int_list():
        return [int(_) for _ in input().split()]
    
    
def input_str():
        return input()
    
    
def input_str_list():
        return [_ for _ in input().split()]
    
    
def print_solution(solution_list):
        for solution in solution_list:
            print(solution)
    
    
def print_solution_list(solution_list):
        for solution in solution_list:
            out = ''
            for i in solution:
                out += str(i) + ' '
            print(out)
    
    
    if __name__ == "__main__":
        p = 10 ** 9 + 7
        t = input_int()
        solution_list = []
        for _ in range(t):
            n, k = input_int_list()
            if k == 0:
                solution_list.append(1)
                continue
    
            c2 = 0
            if n % 2 == 1:
                c = 2 ** (n - 1) + 1
                c %= p
                s = 1
                for i in range(k):
                    s *= c
                    s %= p
    
            else:
                sl = 2 ** (n - 1)
                qc = sl * 2
                c = sl - 1
    
                c %= p
                qc %= p
    
                cl = []
                qcl = []
    
                s = 1
                for i in range(k):
                    cl.append(s)
                    s *= c
                    s %= p
    
                s2 = 1
                for i in range(k):
                    qcl.append(s2)
                    s2 *= qc
                    s2 %= p
    
                for i in range(k):
                    s += cl[i] * qcl[k - i - 1]
                    s %= p
    
            solution_list.append(s)
    
        print_solution(solution_list)
    
    	 	   				    		     			      	