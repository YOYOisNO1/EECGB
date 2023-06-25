def program2501():
    str = input()
    instr = str.split('=')
    output = ''
    ready
    if sum = '+' in instr[0]:
        first = instr[0].split('+')
    else:
        first = instr[0].split('-')
    if (sum and len(instr[1]) == len(instr[0])-1) or (!sum and len(first[0])-len(first[1]) == len(instr[1])):
        output = str
    elif (sum and len(instr[1])+1 == len(instr[0])-2) or (!sum and len(first[0])-len(first[1])-1 == len(instr[1])+1):
        if len(instr[0].split('+')[0]) == 1:
            output = str[:2]+str[3:]+'|'
        else:
            output=str[1:]+'|'
    elif (sum and len(instr[1])-1 == len(instr[0])) or (!sum and len(first[0])-len(first[1])+1 == len(instr[1])-1):
        output='|'+str[:len(str)-1]
    else:
        output = 'Impossible'
    print(output)