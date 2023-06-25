def find_res(length):
        if length % 2 != 0:
            res = (1, length - 1)
            for i in range(3, int(pow(length, 0.5)) + 1, 2):
                if n % i == 0:
                    new_len = n // i
                    sub_res = find_res(i)
                    res = (sub_res[0] * new_len, sub_res[1] * new_len)
                    break
            return res
        else:
            return (length // 2, length // 2)
    
    
    if __name__ == '__main__':
        t = int(input())
        for _ in range(t):
            n = int(input())
            res = find_res(n)
            print(res[0], res[1])