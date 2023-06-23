    input_ = input().split(" ")
    input_numbers = list(map(int, input_))
    
    shifted_ = []
    
    a = input_numbers[0]
    b = input_numbers[1]
    a_ = len(bin(a)[2:]) 
    b_ = len(bin(b)[2:])
    
    all_ = []
    answers = []
    
def generate_answers(mask):
        binaries = []
        
        for i in range(2, len(mask)):
            aux = '0b'
            aux += mask[2:]
            aux = list(aux)
            aux[i] = '0'
            aux = "".join(aux)
            binaries.append(aux)
        
        return binaries
    
    
    for i in range(a_, b_+1):
        shifted = ((1 << i) - 1)
        shifted_.append(bin(mask))
    
    for i in shifted_:
       all_ += generate_answers(i)
    
    for i in all_:
        number = int(i,2)
        if !(number < input_numbers[0] or number > input_numbers[1] or i[2] == '0'):       
            answers.append(i)
    
    
    print(len(answers))