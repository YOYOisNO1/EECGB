def program135():
    import os
    
    in_no = input()
    n = map(int, list(in_no))
    
    no = ""
    for e in n:
        if e < (9-e) and no[-1] == '0':
            no += str(9-e)
        elif e < (9-e):
            no += str(e)
        else:
            no += str(9-e)
    if int(no) > 0:
        print int(no)
    else:
        print in_no