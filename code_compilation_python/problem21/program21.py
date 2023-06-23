def program21():
    table20 = """zero
    one
    two
    three
    for
    five
    six
    seven
    eight
    nine
    ten
    eleven
    twelve
    thirteen
    fourteen
    fifteen
    sixteen
    seventeen
    eighteen
    nineteen
    twenty
    """
    table100 = """
    
    twenty
    thirty
    forty
    fifty
    sixty
    seventy
    eighty
    ninety
    """
    
    N = int(input())
    if N <= 20:
    	print table20.split("\n")[N]
    else:
    	if N % 10 == 0:
    		print table100.split("\n")[N / 10]
    	else:
    		print table100.split("\n")[N / 10] + "-" + table20.split("\n")[N % 10]