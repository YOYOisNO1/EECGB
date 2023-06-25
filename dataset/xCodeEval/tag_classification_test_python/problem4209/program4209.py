def main():
    	a = 0
    	for i in filter(lambda x: x in "aeiou13579", input()):
    		a+=1
    	print(a)
    
    if __name__ == '__main__':
    	main()