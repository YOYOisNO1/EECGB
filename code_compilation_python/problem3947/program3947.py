    #!/usr/bin
    f={'2':'5', '5':'2', '6':'9', '9':'6'}
    class mime(str):
    def __init__(self, me):
            if me in f: self.next = f[me]
            else: self.next = me
    t = map( mime, input() );ice = input()
    skip, kate = {}, []
    num = { s: ice.count(s) for s in {}.fromkeys(ice) }
    for a in {}.fromkeys(t):
        if a in skip: continue
        if a in num:
            if a.next != a and a.next in num:
                kate.append((num[a]+num[a.next])/(t.count(a)+t.count(a.next)))
            else: kate.append(num[a]/(t.count(a)+t.count(a.next)))
        elif a.next != a and a.next in num:
            kate.append(num[a.next]/(t.count(a) + t.count(a.next)))
        else: print 0; quit()
        skip[a.next] = None
        if kate[-1] == 0: break
    print min(kate)