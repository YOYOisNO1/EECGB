def program421():
    interval, guess = map(int, input().split())
    primes = []
    
    for num in range(2, interval + 1):
        if num > 1:
            for i in range(2, num):
                # check for divisors
                if (num % i) == 0:
                    break
    			# if prime
    			else:
    				primes.append(num)
    
    count = 0
    for i in range(len(primes) - 1):
        if count == guess:
            break
        # if found the prime number
        if primes[i] + primes[i+1] + 1 in primes:
            count += 1
            if count == guess:
                break
    
    if count == guess:
        print('YES')
    else:
        print('NO')