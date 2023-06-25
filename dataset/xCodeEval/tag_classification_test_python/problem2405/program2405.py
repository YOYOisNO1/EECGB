def program2405():
    import re
    
    x = int(input())
    
    s = input()
    
    inside = re.findall(r'\([a-z,A-Z,_]+\)', s)
    
    if len(inside) == 0:
        count = 0
    else:
        count = 0
        for i in inside:
            count += len(re.findall(r'[a-z,A-Z]+', i))
            s = s.replace(i, '_')
    
    sl_vne_skobok = re.findall(r'[a-z,A-Z]+', s)
    if len(sl_vne_skobok) == 0:
        dl_vne_skobok = 0
    else:
        dl_vne_skobok = max([len(i) for i in sl_vne_skobok])
    
    print(dl_vne_skobok,) count