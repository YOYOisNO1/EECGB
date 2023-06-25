def program290():
    f,l = input().strip().split(" ")
    lenf = len(f)
    lo = []
    for x in range(1,lenf+1):
    	lo += [f[:x] + l[0]]
    lo.sort()
    print(lo[0])