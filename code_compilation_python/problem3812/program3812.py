    import re
    
    class Cond(object):
    def __init__(self, s):
            s = s.strip()
            i, j = 0, len(s)-1
            while i <= j and s[i] == '_':
                i += 1
            while i <= j and s[j] == '_':
                j -= 1
            if i > j or s[i:j+1] not in ['<', '=', '>', '<=', '>=']:
                print s[i:j+1]
                raise ValueError
            self.va, self.op, self.vb = s[:i], s[i:j+1], s[j+1:]
    def check(self, val):
             if self.va in val and self.vb in val:
                 return eval('%d%s%d' % (val[self.va], self.op, val[self.vb]))
             else:
                 return True
    
def feed(var, conds, val):
        for x in conds:
            if not x.check(val):
                return False
        if var == []:
            return True
        if var[0] in val:
            return feed(var[1:], conds, val)
        c = var[0]
        for v in range(10):
            val[c] = v
            if feed(var[1:], conds, val):
                return True
            del val[c]
        return False
    
    s= input()
    jaw, stomach = s.split(':-')
    if stomach[-1] == '.':
        stomach = stomach[:-1]
    var = re.findall(r'_+', jaw)
    conds = [Cond(c) for c in stomach.split(',')]
    val = dict()
    if not feed(var, conds, val):
        print 'false'
    else:
        o = ''.join([str(val[x]) for x in var])
        print o