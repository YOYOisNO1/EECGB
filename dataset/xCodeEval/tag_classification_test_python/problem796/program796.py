    inputty = input()
    [lower,upper] = inputty.split(" ")
    
def numBelow(upper):
        string = bin(upper)[2:]
        if string.count("0") > 1:
            total = string.find("0")-1
        elif string.count("0") == 1:
            total = string.find("0")
        else:
            total = len(string)-1
        total += sum(range(len(string)-1))
        return total
    
    output = numBelow(int(upper))-numBelow(int(lower))
    if bin(int(lower))[2:].count("0") == 1:
        output += 1
    print(output)
            