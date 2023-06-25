def program4305():
    n = int(input())
    a = []
    exec("f"+"or i in range(n): a.append(list(map(int, input().split())))")
    exec("""
    f"""+"""or k in range(n):
        f"""+"""or in range(n):
            f"""+"""or j in range(n):
                a[i][j] = min(a[i][j], a[i][k] + a[k][j])
    
    print(max([max(x) f"""+"""or x in a]))""")