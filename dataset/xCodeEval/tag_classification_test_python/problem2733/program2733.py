    s = input()
    t = input()
def str_to_dic(s):
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        return d
    
def need_delete(s, t): 
        if len(s) < len(t): 
            return False 
        if len(s) == len(t): 
            return s == t 
    
        index = 0
        pos = 0
        for c in t: 
            index = s[pos:].find(c) 
            if index < 0: 
                return False 
            pos += index + 1 
        return True 
    
    if need_delete(s,t):
        print("automaton")
    else:
        s_dic = str_to_dic(s)
        t_dic = str_to_dic(t)
        if len(t) == len(s) and s_dic == t_dic:
            print("array")
        else:
            both_flag = True
            for c in t_dic.keys():
                if s_dic.get(c, 0) < t_dic[c]:
                    both_flag = False
                    break
            for c in s_dic.keys():
                if t_dic.get(c,0) > s_dic[c]:
                    both_flag = False
            if both_flag:
                print("both")
            else:
                print("need tree")