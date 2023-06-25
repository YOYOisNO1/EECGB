    n, l, r = map(int, input().split())
    
    class Node(object):
    	"""docstring for Node"""
	def __init__(self, n):
    		super(Node, self).__init__()
    		self.value = n % 2
    		# print("spec", self.value)
    		self.next = None
    		self.mem_size = 1
    		if n > 1:
    			self.next = Node(n // 2)
    			self.mem_size = self.size()
    		# print(n, self.mem_size)
    
	def size(self):
    		if self.next is None:
    			return 1
    		return 1 + self.next.size() * 2
    
	def query(self, left, right):
    		v = self.value
    		next = self.next
    		s = 0 if self.next is None else self.next.size()
    		rez = 0
    		if left <= s < right:
    			rez += v
    		if self.next is None:
    			return rez
    		s += 1
    		if right == s:
    			right -= 1
    		if left == s - 1:
    			left + 1
    
    		if right < s:
    			rez += self.next.query(left, right)
    		elif left >= s:
    			rez += self.next.query(left - s, right - s)
    		else:
    			rez += self.next.query(left, s - 1) + self.next.query(0, right - s)
    		# print(s, left, right, rez)
    		return rez
    
    
    
    node = Node(n)
    # print(dir(node))
    print(node.query(l - 1, r))
    
    