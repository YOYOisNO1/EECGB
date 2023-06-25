def program127():
    totalSum = input("")
    output = []
    no = 1
    while (totalSum != 0):
        if (totalSum - no) == no:
            output.append(totalSum)
            totalSum = 0
        if (totalSum - no) in output:
            output.append(totalSum)
            totalSum = 0
        if (totalSum - no >= 0):
            output.append(no)
            totalSum = totalSum - no
            no = no + 1
    
    print(len(output))
    print(' ').join(map(str, output))
    