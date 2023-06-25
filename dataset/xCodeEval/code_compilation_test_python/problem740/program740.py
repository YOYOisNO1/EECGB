def program740():
    import sys
    import re
    str = #input()
    names = ['Danil', 'Olya', 'Slava', 'Ann','Nikita']
    count = 0
    for name in  names: 
        tmp_count = 0
        for m in re.finditer(name,str):
            if m.start() >= 0:
                tmp_count += 1
        
        if tmp_count > 1:
            print('NO')
            sys.exit(0)
        elif tmp_count == 1:
            count += 1    
    
    if(count == 1):
        print('YES')
    else:
        print('NO')