    #!/usr/bin/python
    
    import sys
    
        
def solve(N):
        strN = str(N)
        no_digits = len(strN)
        res_list = []
        if int(strN[0]) < 8:
            res_list.append((0, N))
        if int(strN[0]) > 4:
            felso = int('1' * (no_digits + 1))
            res_list.append((no_digits + 1, felso - N))
        for i in range(no_digits):
            res_list_copy = [r for r in res_list]
            res_list = []
            my_num = no_digits - i
            oneone = int('1' * my_num)
            for steps, remainder in res_list_copy:
                also = remainder // oneone
                felso = also + 1
                res_list.append((steps + also * my_num, remainder - oneone * also))
                res_list.append((steps + felso * my_num, oneone * felso - remainder))
            steps = [s[0] for s in res_list]
            step_min = min(steps)
            step_max =(my_num + 1) * 6 + step_min
            res_list = [r for r in res_list if r[0] < step_max]
        res_list = [x - i for (x,i) in res_list]
        return (min(res_list))
        
            
def run():
        out = ""    
        N = int(input())
        print(solve(N))
    
    run()
    