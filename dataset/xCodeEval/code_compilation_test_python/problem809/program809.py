    #!/usr/bin/env python
    # -*- coding:utf-8 -*-
    #
    
    from string import letters, digits
    
def readint(): return int(input())
def readfloat(): return float(input())
def readarray(N, foo):
            res = []
            for _ in xrange(N):
                    res.append(foo())
            return res
def readlinearray(foo): return map(foo, input().split())
    
def is_only_letters_digits_and_underscore(word):
        for l in word:
                if l not in letters and l not in digits and l != '_' :
                    return False
        return True
    
def is_len(min, max, word):
        return min <= len(word) <= max
    
def is_jabber_id(jabber_id):
        #<username>@<hostname>[/resource]
    
        if jabber_id.count('@') > 1 or jabber_id.count('/') > 1:
            return False
        
        try:
            username = jabber_id.split('@')[0]
            hostname = jabber_id.split('@')[1].split('/')[0]
            resource = None
            if '/' in jabber_id:
                resource = '/'.join(jabber_id.split('@')[1].split('/')[1:])
        except IndexError:
            return False
        
        if not is_len(1, 16, username):
            return False
        
        if not is_only_letters_digits_and_underscore(username):
            return False
        
        if not is_len(1, 32, hostname):
            return False
        
        for word in hostname.split('.'):
            if not is_len(1, 16, word):
                return False
            if not is_only_letters_digits_and_underscore(word):
                return False
        
        if resource is None:
            return True
        
        if not is_len(1, 16, resource):
            return False
        if not is_only_letters_digits_and_underscore(resource):
                return False
        return True
    
    if __name__ == '__main__':
        
        jabber_id = input()
        if is_jabber_id(jabber_id):
            print 'YES'
        else:
            print 'NO'