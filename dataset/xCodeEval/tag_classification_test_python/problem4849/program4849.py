    #  =========     /\       /|    |====/|
    #      |        /  \       |    |   / |
    #      |       /____\      |    |  /  |
    #      |      /      \     |    | /   |
    #  ========= /        \  =====  |/====|  
    #  code
    
def main():
        MOD = int(1e9) + 7
        a , b = map(int , input().split())
        k1 = ((b - 1)*b)//2
        k2 = ((a + 1)*a)//2
        k1 %= MOD
        k2 %= MOD
        ans = (k2 * b + a)%MOD
        ans = (ans * k1)%MOD
        print(ans)
        return
    
    if __name__ == "__main__":
        main()