def program2188():
    n = int(input())
    binary = bin(n)
    binary = binary[2:]
    count = 0
    for letter in binary:
        count+=int(letter)
    print(count)