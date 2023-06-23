def main():
    	x = int(input())
    	ans = 0
    	for i in range(2, x):
    		ans += i*(i+1)
    	print ans
    
    if __name__ == '__main__':
    	main()