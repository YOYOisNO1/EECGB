def main():
        n,p,k = input().split()
        n = int(n)
        p = int(p)
        k = int(k)
        s = ""
        if p -k > 1 and p + k <n :
            s = s + "<< "
            for i in range(p-k , p + k + 1):
                if i == p:
                    s = s + '(' + str(i) + ')' + " "
                else:
                    s = s + str(i) + " "
            s = s + ">>"
        if p - k <= 1 and p + k< n:
            for i in range(1, p + k + 1):
                if i == p:
                    s = s + '(' + str(i) + ')' + " "
                else:
                    s = s + str(i) + " "
            s = s + ">>"
        if p + k >= n and p - k > 1:
            s = s + "<< "
            for i in range(p - k, n + 1):
                if i == p:
                    s = s + '(' + str(i) + ')' + " "
                else:
                    s = s + str(i) + " "
        if p - k <= 1 and p + k >= n:
            for i in range(1,n + 1):
                if i == p:
                    s = s + '(' + str(i) + ')' + " "            
                else:
                    s = s + str(i) + " "
        print(s)
    if __name__ == "__main__":
        main()