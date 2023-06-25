def program3883():
    frendz, k, l, c, d, sal, ml_cana, g_sal = map(int, input().split())
    
    cana = k * l
    fatias_limao = c * d
    toasts = 0
    
    bebe = frendz * ml_cana
    lambe = frendz * g_sal
    
    while (bebe <= cana and lambe <= sal and frendz <= fatias_limao):
        cana -= bebe
        sal -= lambe
        fatias_limao -= frendz
        toasts += 1
    
    print(toasts)