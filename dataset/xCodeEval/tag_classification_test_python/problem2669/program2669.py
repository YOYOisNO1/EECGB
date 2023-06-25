def program2669():
    h, m = input().strip().split(":")
    if 10 > int(h) > 5:
        print("10:01")
    else:
        if int(h) < 6:
            if int(m) < int("".join(reversed(str(h)))):
                print("".join([h, ":", "".join(reversed(h))]))
            else:
                print("".join(["0",str(int(h)+1), ":", "".join(reversed(str(int(h)+1))), "0"]))
        if int(h) == 10:
            if m == "00":
                print("10:01")
            else:
                print("11:11")
        else:
            if int(h) > 10 :
                if int(h) == 23 and int(m) > 32:
                    print("00:00")
                else:
                    if 20 > int(h) >= 15 and int("".join(reversed(str(h)))) >= 51:
                        print("20:02")
                    else:
                        if int(m) < int("".join(reversed(str(h)))):
                            print("".join([h, ":", "".join(reversed(h))]))
                        else:
                            print("".join([str(int(h) + 1), ":", "".join(reversed(str(int(h) + 1)))]))
    
    
    
    
    
    
    
    