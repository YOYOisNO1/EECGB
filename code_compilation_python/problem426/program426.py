def program426():
    try :
        import sys
        n, d = map(int, input().split(" "))
        #s = list(map(int, input().split(" ")))
        s = [list(int(n) for n input.split() for _ in range(0, n))]
        l = [i for i in s if s[i] == 1]
        diff = [l[i+1] - l[i] for i in range(0, len(l) - 1) if ((l[i+1] - l[i]) <= d)]
        if not diff :
            print(-1)
        else :
            print(min(diff))
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError as ex:
        print("Could not convert data to an integer.")
        print("value error: {0}".format(ex))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        
       