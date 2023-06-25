    from string import *
    from math import *
    from random import *
    from itertools import *
    
    class Test:
	def __init__(self):
    		self.__tests = []
    		self.__iteration = 0
    
	def add(self, test_input, test_output):
    		self.__tests.append((tuple(test_input), test_output))
    
	def __iter__(self):
    		return self
    
	def next(self):
    		if self.__iteration == len(self.__tests):
    			raise StopIteration
    		else:
    			self.__iteration += 1
    			return self.__tests[self.__iteration - 1]
    
	def test(self, soln_func):
    		for test in self:
    			i,o = test
    			print("Input:"), i
    			print("Expected Out:"), o
    			actual = soln_func(*i)
    			print("Actual Out:"), actual
    			print(tests) = Test()
    tests.add([3],3)
    tests.add([11],0)
    
def solution(n):
    	digits = ""
    
    	num = 1
    	while len(digits) < n:
    		digits += str(num)
    		num += 1
    
    	#print(digits)
    
    	return digits[n-1]
    
    #tests.test(solution)
    print(solution(int(input().strip())))