def program5819():
    position = int(input())
    sequence_length = 1
    iterator = 1
    
    while sequence_length < position:
        iterator += 1
        sequence_length += iterator
    
    print(position + iterator - sequence_length)