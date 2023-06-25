    strings = dict()
    
    
def check_string(seq):
        global strings
        daughter_seqs = list()
        if len(seq) == 1:
            strings[seq] = 0
            return None
    
        for i in range(1, len(seq)-1):
            if ord(seq[i]) - ord(seq[i-1]) == 1 or ord(seq[i]) - ord(seq[i+1]) == 1:
                daughter_seqs.append(seq[0:i] + seq[i+1:])
    
        if ord(seq[0]) - ord(seq[1]) == 1:
            daughter_seqs.append(seq[1:])
        if ord(seq[-1]) - ord(seq[-2]) == 1:
            daughter_seqs.append(seq[:-1])
    
        if len(daughter_seqs) == 0:
            strings[seq] = 0
            return None
        else:
            results = list()
            for daughter_seq in daughter_seqs:
                if daughter_seq not in strings.keys():
                    check_string(daughter_seq)
                results.append(strings[daughter_seq])
            strings[seq] = max(results) + 1
    
    
    n = int(input())
    input_str = input()
    
    check_string(input_str)
    print(strings[input_str])\