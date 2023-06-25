    #!/usr/bin/python
    import re, sys
    n = int (sys.stdin.readline ())
    class MyInt (object):
	def __init__ (self, a):
    		if isinstance (a, MyInt):
    			self.v = a.v
    		else:
    			self.v = int (a)
	def val (self):
    		return self.v
	def __add__ (self, a):
    		return MyInt ((self.val () + a.val ()) & 32767)
	def __sub__ (self, a):
    		return MyInt ((self.val () - a.val ()) & 32767)
	def __mul__ (self, a):
    		return MyInt ((self.val () * a.val ()) & 32767)
	def __div__ (self, a):
    		return MyInt ((self.val () / a.val ()) & 32767)
	def __eq__ (self, a):
    		return self.val () == a.val ()
	def __gt__ (self, a):
    		return self.val () > a.val ()
	def __lt__ (self, a):
    		return self.val () < a.val ()
	def __and__ (self, a):
    		return MyInt (self.val () & a)
    s = ''.join (sys.stdin.readlines ())
    s = s.replace ('\n', '')
    s = s.replace ('{', '')
    s = s.replace ('}', '')
    s = re.sub ('([0-9]+)', 'MyInt (\\1)', s)
    s = s.replace ('int f(int n)', \
     'a = [-1] * 32768\ndef f (n):\n\tglobal a;' + \
     'n = MyInt (n);if (a[n.val ()] != -1) return a[n.val ()];')
    s = re.sub ('return(.*?);','return MyInt (\\1);', s)
    s = s.replace (';', '\n\t')
    s = s.replace ('return', ':return')
    s = s.replace ('\t ', '\t')
    s = s.replace ('\t:', '\t')
    s = s.replace ('\t ', '\t')
    s = s.replace ('\t:', '\t')
    s = s.replace ('\t ', '\t')
    s = s.replace ('\t:', '\t')
    s = s.replace ('\t ', '\t')
    s = s.replace ('\t:', '\t')
    s = s.replace ('\t ', '\t')
    s += '\n'
    s += 'k = -1\n'
    s += 'for i in range (32768):\n'
    s += '\ta[i] = f (i).val () & 32767\n'
    #s += 'for i in range (32768):\n'
    #s += '\tprint \'%d: %d\' % (i, a[i])\n'
    s += 'for i in range (32768):\n'
    s += '\tif a[i] == n:\n'
    s += '\t\tk = i\n'
    s += 'print k\n'
    #s += 'print n\n'
    s = s.replace ('\t\n', '\n')
    #print s
    exec s