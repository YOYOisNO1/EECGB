def main():
    	n, m = map(int, input().split())
    	if n > m: n, m = m, n
    	if 1 == n: print(m)
    	elif 2 == n: print(m) / 4 * 4 + (4 if m % 4 >= 2 else 2 * (m % 4))
    	else: print((n) * m + 1) / 2
     
    if __name__ == "__main__": main()