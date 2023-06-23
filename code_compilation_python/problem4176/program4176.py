# def f(x,b):
    # 	s = ""
    # 	while x > b:
    # 		s += str(x/b)
    # 		x /= b
    # 	s += str(x)
    # 	return s
    
def digit_to_char(digit):
        if digit < 10:
            return str(digit)
        return chr(ord('a') + digit - 10)
    
def str_base(number,base):
        if number < 0:
            return '-' + str_base(-number, base)
        (d, m) = divmod(number, base)
        if d > 0:
            return str_base(d, base) + digit_to_char(m)
        return digit_to_char(m)
    
    n = input()
    for i in range(1,n):
    	for j in range(1,n):
    			# print '%2d'%f(i*j,n),
    			print str_base(i*j,n),
    	print