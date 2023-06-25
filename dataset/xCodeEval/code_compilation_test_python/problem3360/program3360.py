    from math import ceil, floor
    
    
def readint():
        return int(input())
    
    
def readline():
        return [int(c) for c in input().split()]
    
    
def main():
        la, ra, ta = readline()
        lb, rb, tb = readline()
    
        res = []
        if lb > la:
            left_limit_left = int(ceil((lb - la) / ta))
            left_limit_right = int(floor((rb - la) / ta))
    
            kl = list(range(left_limit_left, left_limit_right+1))
            for k in kl:
                lla = la + k * ta
                rra = ra + k * ta
                res.append(min(rra, rb) - max(lla, lb) + 1)
    
            right_limit_left = int(ceil((lb - ra) / ta))
            right_limit_right = int(floor((rb - ra) / ta))
            kr = list(range(right_limit_left, right_limit_right+1))
            for k in kr:
                lla = la + k * ta
                rra = ra + k * ta
                res.append(min(rra, rb) - max(lla, lb) + 1)
    
            print(max(res))
        else:
            left_limit_left = int(ceil((la - lb) / tb))
            left_limit_right = int(floor((ra - lb) / tb))
            kl = list(range(left_limit_left, left_limit_right+1))
            for k in kl:
                llb = lb + k * tb
                rrb = rb + k * tb
                res.append(min(rrb, ra) - max(llb, la) + 1)
    
            right_limit_left = int(ceil((la - rb) / tb))
            right_limit_right = int(floor((ra - rb) / tb))
            kr = list(range(right_limit_left, right_limit_right+1))
            for k in kr:
                llb = lb + k * tb
                rrb = rb + k * tb
                res.append(min(rrb, ra) - max(llb, la) + 1)
    
            print(max(res))
    
            
        
    
    if __name__ == '__main__':
        main()