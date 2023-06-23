    from math import floor,ceil
    
def find_possible_number(guess_number,digit,possible_table):
        if digit==len(phone_numbers):#base condition
            return 1
        
        m_number=int(phone_numbers[digit])
        guess_number=int(guess_number)
        
        num_index_configuration=str(guess_number)+str(digit)    
        if num_index_configuration in possible_table:
            return possible_table[num_index_configuration]    
        possible_table[num_index_configuration]=0
        
        has_remainder=(m_number+guess_number)%2
        if has_remainder:
            has_remainder_case(m_number, guess_number, possible_table, num_index_configuration, digit)
            return possible_table[num_index_configuration]
        else:
            has_no_remainder_case(m_number, guess_number, possible_table, num_index_configuration, digit)
            return possible_table[num_index_configuration]
    
    
def has_remainder_case(m_number, guess_number, possible_table, num_index_configuration, digit):
        upper_number=ceil((m_number+guess_number)/2)
        possible_table[num_index_configuration]+=find_possible_number(upper_number,digit+1,possible_table)
        lower_number=floor((m_number+guess_number)/2)
        possible_table[num_index_configuration]+=find_possible_number(lower_number,digit+1,possible_table)
        
        
def has_no_remainder_case(m_number, guess_number, possible_table, num_index_configuration, digit):
        next_number=(m_number+guess_number)/2
        possible_table[num_index_configuration]+=find_possible_number(next_number,digit+1,possible_table)
    
def has_exception(number):
        for i in range(1,len(phone_numbers)-1):  
            
            if (int(phone_numbers[i])+number)%2:
                upper=ceil((int(phone_numbers[i])+number)/2)
                lower=floor((int(phone_numbers[i])+number)/2)
                if upper==int(phone_numbers[i]):
                    number=int(phone_numbers[i])           
                elif lower==int(phone_numbers[i]):
                    number=int(phone_numbers[i])    
                else:
                    return False
            else:
                if (int(phone_numbers[i])+number)/2==int(phone_numbers[i]):
                    number = int(phone_numbers[i])
                else:
                    return False
        return True
    
    
    phone_numbers=input()
    possible_table={}#with the format of ["ab"]=c. a for number, b for digit, c for possible ways
    first_number=phone_numbers[0]
    count=0
    for i in range(10):
        count+=find_possible_number(i,1,possible_table)
    if has_exception(int(phone_numbers[0])):
        count-=1
    
    #print(possible_table)
    print(count)
    
    