def read_ints():
        return [int(x) for x in input().split()]
    
    
    F0 = 'What are you doing at the end of the world? Are you busy? Will you save us?'
    Fi = 'What are you doing while sending ""? Are you busy? Will you send ""?'
    LEN_F0 = len(F0)
    LEN_Fi = len(Fi)
    
    
    F = [LEN_F0]
    
    
def get_char(n, k):
        total_len = F[n]
        if k > total_len:
            return '.'
    
        while True:
            if n == 0:
                return F0[k]
    
            len_f_i_1 = F[n-1]
            if k < 34:
                return Fi[k]
            elif k < 34 + len_f_i_1:
                n -= 1
                k -= 34
            elif k < 34 + len_f_i_1 + 32:
                return Fi[k-len_f_i_1]
            else:
                n -= 1
                k -= 34 + len_f_i_1 + 32
    
    
def main():
        global F
        num_questions, = read_ints()
    
        for i in range(1, 100000):
            F.append(2 * F[i - 1] + LEN_Fi)
    
        for _ in range(num_questions):
            n, k = read_ints()
            c = get_char(n, k-1)
            print(c, end='')
    
    
    if __name__ == '__main__':
        main()