def program6044():
    l, d, v, g, r = list(map(int, input().split(" ")))
    
    t_ate_sinal = d / v
    d_depois_sinal = l - d
    t_depois_sinal = d_depois_sinal / v
    
    t_no_sinal = 0
    
    resto_sinal = t_ate_sinal % (g+r)
    
    if resto_sinal >= g:
    	t_no_sinal = (g-resto_sinal) + r
    
    resultado = t_ate_sinal + t_no_sinal + t_depois_sinal
    print("%.8f" % resultado)
    
    