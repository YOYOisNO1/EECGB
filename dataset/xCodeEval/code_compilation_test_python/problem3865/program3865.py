    import itertools
    from datetime import date
    
def main(a, b):
        cd = [int(s, 10) for s in a.split('.')][::-1]
        bd = [int(s, 10) for s in b.rsplit('.')][::-1]
        
        for d in itertools.permutations(bd):
            try:
                t = date(*cd) - date(*d)
                if t.days/365 >= 18:
                    print("YES")
            except ValueError:
                pass
        print("NO")
    
    
    a = input()
    b = input()
    main(a, b)