    #!/usr/bin/env python
    
    from collections import defaultdict
    
def rmZeros(num):
    	num = str(num)
    	num = num.translate(None, '0')
    	return int(num)
    
    import sys
    data = sys.stdin.readlines()
    num1 = int(data[0].strip())
    num2 = int(data[1].strip())
    summ = num1 + num2
    if rmZeros(num1) + rmZeros(num2) == rmZeros(summ):
    	print('YES')
    else:
    	print('NO')