    # python3
    # utf-8
    
def string___ins__outs(string):
        string = string
        # '(___)'
        splted_by_op = string.split('(')
        # print(splted_by_op)
        # ['', '___)']
        ins = [x.split(')')[0] for x in splted_by_op if ')' in x]
        # ['___']
    
        # ['', '___)']
        outs = [(x + '_').split(')')[-1] for x in splted_by_op]
        # ['_', '_']
        # print(ins, outs)
        return (ins, outs)
    
    
def outs___max_len(outs):
        words = insouts___words(outs)
        if len(words) == 0:
            return 0
        lens = [len(x) for x in words]
        return max(lens)
    
def ins___nr(ins):
        words = insouts___words(ins)
        return(len(words))
    
def insouts___words(inouts):
        # ['__', '_a', 'b_', '']
        words = []
        for string in inouts:
            words += string.split('_')
        # ['', '', '', 'a', 'b', '']
        words = [x for x in words if x != '']
        # ['a', 'b']
        # print(words)
        return words
    
    string_len = int(input())
    string = input()
    ins, outs = string___ins__outs(string)
    print(outs___max_len(outs), ins___nr(ins))