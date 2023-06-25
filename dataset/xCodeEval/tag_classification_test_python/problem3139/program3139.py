def program3139():
    n = int(input())
    r = n%10
    if r>5:
    	n = n-r+10
    else:
    	n = n-r+0
    print(n)