def program2629():
    #!/usr/bin/env python
    
    x = int(input())
    numOfDoubles = x / 3;
    remaining = x % 3;
    final = 0
    if remaining > 0 :
        final += 1
    print(final) + 2 * numOfDoubles