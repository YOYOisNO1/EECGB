def program2511():
    a = int(input())
    s = "ROYGBIV"
    s4 = s[:4]
    s3 = s[4:]
    if a > 7:
        ls = a // 4
        ds = a - ls
        all_aggs = ls * s4 + s3
        print(all_aggs[:a])
     lse:
        print(s[:a])