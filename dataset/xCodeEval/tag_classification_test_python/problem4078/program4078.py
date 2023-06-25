    import sys;
    
def as_ternary_string (decimal) :
        ternary = "";
        tmp = decimal;
        while tmp >= 3 :
            ternary = str(tmp % 3) + ternary;
            tmp = int(tmp / 3);
        ternary = str(tmp) + ternary;
    
        return ternary;
    
def as_decimal_int (ternary) :
        decimal = 0;
        for i in range(len(ternary)) :
            decimal = decimal + int(ternary[i]) * (3 ** (len(ternary) - i - 1));
        return decimal;
    
    line = sys.stdin.readline().split("\n")[0].split();
    a, c = map(int, line);
    a, c = map(as_ternary_string, [a, c]);
    
    if len(a) < len(c) :
        for _ in range(len(c) - len(a)) :
            a = "0" + a;
    elif len(a) > len(c) :
        for _ in range(len(a) - len(c)) :
            c = "0" + c;
        
    b = ""
    for i in range(len(a)) :
        if c[i] == a[i] :
            b = b + "0";
        elif a[i] == "0" :
            b = b + c[i];
        elif c[i] == "0" and a[i] == "1" :
            b = b + "2";
        elif c[i] == "0" and a[i] == "2" :
            b = b + "1";
        elif c[i] == "1" and a[i] == "2" :
            b = b + "2";
        elif c[i] == "2" and a[i] == "1" :
            b = b + "1";
        else :
            print("nanika okasii");
            exit(1);
    
    print(as_decimal_int(b);)