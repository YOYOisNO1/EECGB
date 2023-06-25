    lst = []
def dedistyvna(string):
        try:
            indx = string.index('(')
            indx1 = string.index(')')
            s = string[indx + 1:indx1]
            lst.append(s)
            return dedistyvna(string[indx1 + 1:])
        except ValueError:
            pass
        return lst
    
    
    lst1 = []
    inp1 = input()
    inp = input()
    # frchxilebshi stringis pasuxi
def dedistyvna1():
        for x in dedistyvna(inp):
            a = x.split('_')
            for line in a:
                if len(line) > 0:
                    lst1.append(line)
        return len(lst1)
    lst2 = []
    # gareta stringis amogeba
def remove_string(string1):
        try:
            a = string1.index('(')
            b = string1.index(')')
            lst2.append(string1[:a])
            return remove_string(string1[b + 1:])
        except ValueError:
            lst2.append(string1)
        return lst2
    lst3 = []
    # gareta stringis pasuxi
def dedistyvna3():
        for y in remove_string(inp):
            b = y.split('_')
            for line in b:
                if len(line) > 0:
                    lst3.append(line)
        return lst3
    k = 0
    if len(dedistyvna3()) == 0:
        k = 0
    else:
        k = max(map(len, dedistyvna3()))
    print(str(k) + ' ' + str(dedistyvna1()))