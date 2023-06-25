def program2480():
    input()
    number_in = 0
    length_out = 0
    in_, out_ = False, True
    data = input()
    current_length = 0
    for s in data:
        if s == '(':
            in_, out_ = True, False
            length_out = max(length_out, current_length)
            current_length = 0
        elif s == ')':
            in_, out_ = False, True
            if current_length > 0:
                number_in += 1
                current_length = 0
        elif s == '_':
            if in_ and current_length > 0:
                number_in += 1
            elif out_:
                length_out = max(length_out, current_length)
            current_length = 0
        else:
            current_length += 1
    length_out = max(length_out, current_length)
    print(length_out,) number_in
    
    
    
    