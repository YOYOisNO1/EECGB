def program6805():
    import sys, string
    k = int(input())
    pal = list(input().strip())
    n = len(pal)
    center = (n-1)//2
    for i in range(center+1):
    	j = n-1-i
    	if pal[i] == pal[j]:
    		continue
    	if pal[i] == '?':
    		pal[i] = pal[j]
    	elif pal[j] == '?':
    		pal[j] = pal[i]
    	else:
    		print('IMPOSSIBLE')
    		sys.exit()
    need = []
    for ch in string.ascii_letters[:k]:
    	if ch not in pal:
    		need.append(ch)
    nix = len(need)-1
    for i in range(center, -1, -1):
    	if pal[i] != '?':
    		continue
    	j = n-i-1
    	if nix == -1:
    		pal[i] = pal[j] = 'a'
    	else:
    		pal[i] = pal[j] = need[nix]
    		nix -= 1
    if nix != -1:
    	print('IMPOSSIBLE')
    else:
    	print(''.join(pal))