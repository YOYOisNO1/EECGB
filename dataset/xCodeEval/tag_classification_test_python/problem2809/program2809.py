    n, array = int(input()), input().split()
    array = [int(ch) for ch in array]
    
    
def is_unimodal(seq):
        i = 1
        end = len(seq)
        while i < end and seq[i - 1] < seq[i]:
            i += 1
        while i < end and seq[i - 1] == seq[i]:
            i += 1
        while i < end and seq[i - 1] > seq[i]:
            i += 1
    
        if i == end:
            print("YES")
        else:
            print("NO")
    
    
    is_unimodal(array)