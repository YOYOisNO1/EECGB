    
def mul_matrix(m1, m2, m):
        return [(m1[0] * m2[0] + m1[1] * m2[2]) % m, (m1[0] * m2[1] + m1[1] * m2[3]) % m,
            (m1[2] * m2[0] + m1[3] * m2[2]) % m, (m1[2] * m2[1] + m1[3] * m2[3]) % m]
    
    
def pow_matrix(a, b, c, d, n, m):
        if n == 0:
            return [1, 0, 0, 1]
        if n == 1:
            return [a, b, c, d]
        result = pow_matrix(a, b, c, d, n / 2, m)
        result = mul_matrix(result, result, m)
        if n % 2 == 1:
            return mul_matrix(result, [a, b, c, d], m)
        return result
    
def pow(a, n, m):
        if n == 0:
            return 1
        if n == 1:
            return a
        result = pow(a, n / 2, m)
        if n % 2 == 1:
            return (result * result * a) % m
        return (result * result) % m
    
def count_1(k):
        count = 0
        while k != 0:
            if k % 2 == 1:
                count += 1
            k /= 2
        return count
    
def main():
        n, k, l, m = [int(s) for s in input().strip().split()]
        if k >= 2 ** l:
            print(0)
            return
    
        matrix = pow_matrix(1, 1, 1, 0, n + 1, m)
        t = matrix[0]
        a = (pow(2, n, m) - t) % m
        b = count_1(k)
        print((pow(a,) b, m) * pow(t, l - b, m)) % m
    
    if __name__ == '__main__':
        main()