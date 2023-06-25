def program2321():
    input() # skip line with list lengths
    xs = {int(r) for r in input().split()}
    ys = {int(r) for r in input().split()}
    
    zs = xs & ys
    if len(zs) > 0:
        print(min(zs))
    else:
        a = min(xs)
        b = min(ys)
        print(str(min(a, b)) + str(max(a, b)))