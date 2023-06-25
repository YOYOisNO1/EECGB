    q = int(input())
    
    c = 'What are you doing at the end of the world? Are you busy? Will you save us?'
    a = 'What are you doing while sending "'
    b = '"? Are you busy? Will you send "'
    d = '"?'
    
    
def read_question():
        return list(map(int, input().split()))
    
    
    sizes = dict()
    
    
def fill_sizes():
        sizes[0] = len(c)
        for k in range(1, int(pow(10, 5))):
            if sizes[k - 1] >= pow(10, 18):
                break
            sizes[k] = len(a) + len(b) + len(d) + 2 * sizes[k - 1]
    
    
    fill_sizes()
    result = ""
    
    sizes_list = sorted(list(sizes.values()))
    
    
def find_in_which_one(n):
        for k in range(56):
            if sizes_list[k] > n:
                return k
        return 53
    
    
def get_char(n, k):
        if n == 0:
            return c[k]
    
        if k < len(a):
            return a[k]
    
        if len(a) <= k < len(a) + sizes_list[n - 1]:
            return get_char(n - 1, k - len(a))
    
        if len(a) + sizes_list[n - 1] <= k < len(a) + sizes_list[n - 1] + len(b):
            return b[k - (len(a) + sizes_list[n - 1])]
    
        if len(a) + sizes_list[n - 1] + len(b) <= k < len(a) + sizes_list[n - 1] + len(b) + sizes_list[n - 1]:
            return get_char(n - 1, k - (len(a) + sizes_list[n - 1] + len(b)))
    
        return d[k - (len(a) + sizes_list[n - 1] + len(b) + sizes_list[n - 1])]
    
    
def find_char(n, k):
    
        if n > 53:
            if k < (n - 53) * len(a):
                return a[k % len(a)]
            k -= (n - 53) * len(a)
            n = 53
        if n in sizes and sizes[n] <= k:
            return "."
        return get_char(n, k)
    
    
    for _ in range(q):
        n, k = read_question()
        result += find_char(n, k - 1)
    
    print(result)