    class GlobalMembers(object):
	def __init__(self):
    		self._maxn = 1e6 + 100
    		self._a = System.String(Array.CreateInstance(Char, 1005))
    		self._vis = Array.CreateInstance(int, self._maxn)
    
	def Main():
    		tempVar = ConsoleInput.scanfRead()
    		if tempVar != None:
    			self._a = Byte.parseByte(tempVar)
    		n = self._a.length()
    		flag = 0
    		ans = 'a'
    		self._vis[0] = 1
    		if self._a.charAt(0) != 'a':
    			flag = 1
    		i = 0
    		while i < n:
    			if self._vis[self._a.charAt(i) - 'a'] == 0:
    				if self._a.cha