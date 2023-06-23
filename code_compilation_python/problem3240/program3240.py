def program3240():
    ways = int(input())
    divisors = [val ** 3.0 for val in xrange(2, 170417)]
    intdivisors = [val * val * val for val in xrange(2, 170417)]
    low, high = 1, 4949100894494448
    while low < high:
            mid = (low + high) / 2
            if sum(int(mid / divisors[i]) for i in xrange(min(len(divisors), int(mid ** 0.3336)))) >= ways:
                    high = mid
            else:
                    low = mid + 1
    print -1 if sum(low / divisor for divisor in intdivisors) != ways else low
    