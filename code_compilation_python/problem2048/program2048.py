def program2048():
    print(sum(i-j<i^j>j for i in range(input())+1)for j in range(i//2)))