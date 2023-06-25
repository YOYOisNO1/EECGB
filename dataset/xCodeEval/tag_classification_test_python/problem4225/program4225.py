def program4225():
    m = input()
    s = input()
    
    if ('11' in s) or s.startswith('00') or s.endswith('00') or ('000' in s) or s=='0':
        print("No")
    else:
        print("Yes") 