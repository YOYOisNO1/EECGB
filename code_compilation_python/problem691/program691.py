def program691():
    'use strict'
    
    const gcd = (x, y) => { while(y) y = x % (x = y); return x; }
    
    const prime_factors = n => {
        if (n === 1) return [1];
        let i = 2;
        const factors = [];
        while (i * i <= n) {
            if (n % i) i += 1;
            else {
                while (n % i === 0) n /= i;
                factors.push(i);
            }
        }
        if (n > 1) factors.push(n);
        return factors;
    }
    
    const factors = prime_factors(+readline());
    print(factors.slice(1).reduce((r, i) => gcd(r, i), factors[0]));