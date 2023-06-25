def program5070():
    from sys import stdin, stdout
    
    x, y = [int(z) for z in stdin.readline().split()]
    
    answer = "NO"
    
    if x == y:
        answer = "YES"
    
    x_reduced = x
    while x_reduced % 2 == 0:
        x_reduced = x_reduced // 2
    y_bin = str(bin(y))[2:]
    
    x_reduced_bin = str(bin(x_reduced))[2:]
    if len(x_reduced_bin) <= len(y_bin):
        delta = len(y_bin) - len(x_reduced_bin)
        for i in range(delta+1):
            candidate = '1'*i + x_reduced_bin + '1'*(delta-i)
            if candidate == y_bin:
                answer = "YES"
    
    x_reduced_bin = x_reduced_bin[::-1]
    if len(x_reduced_bin) <= len(y_bin):
        delta = len(y_bin) - len(x_reduced_bin)
        for i in range(delta+1):
            candidate = '1'*i + x_reduced_bin + '1'*(delta-i)
            if candidate == y_bin:
                answer = "YES"
    
    x_reduced_bin = str(bin(x))[2:] + '1'
    if len(x_reduced_bin) <= len(y_bin):
        delta = len(y_bin) - len(x_reduced_bin)
        for i in range(delta+1):
            candidate = '1'*i + x_reduced_bin + '1'*(delta-i)
            if candidate == y_bin:
                answer = "YES"
    
    x_reduced_bin = x_reduced_bin[::-1]
    if len(x_reduced_bin) <= len(y_bin):
        delta = len(y_bin) - len(x_reduced_bin)
        for i in range(delta+1):
            candidate = '1'*i + x_reduced_bin + '1'*(delta-i)
            if candidate == y_bin:
                answer = "YES"
    
    stdout.write(answer + '\n')