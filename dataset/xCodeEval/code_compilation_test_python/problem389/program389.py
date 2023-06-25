def program389():
    k = list(map(int, input().split(' ')
    if k[0] + k[1] + k[3] == k[2] + k[4] + k[5] or k[0] + k[1] + k[2] == k[3] + k[4] + k[5] or k[0] + k[1] + k[4] == k[2] + k[3] + k[5] or k[0] + k[1] + k[5] == k[3] + k[4] + k[2] or k[0] + k[2] + k[3] == k[1] + k[4] + k[5] or k[0] + k[2] + k[4] == k[1] + k[3] + k[5] or k[0] + k[2] + k[5] == k[1] + k[4] + k[3] or k[0] + k[4] + k[3] == k[1] + k[2] + k[5] or k[0] + k[5] + k[3] == k[1] + k[4] + k[2] or k[0] + k[4] + k[5] == k[1] + k[2] + k[3]:
    	print('Yes')
    else:
    	print('No')