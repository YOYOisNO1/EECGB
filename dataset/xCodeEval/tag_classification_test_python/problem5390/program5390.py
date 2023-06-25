    # RANK1ZEN; 3966 PEAK NA FLEX SUPPORT; Battlenet ID -> Knuckles#11791
    # region -----------------------------------------------------------------------------------------|
    # MNNNNNNNNNNNNNNNNMNho///++//+oooooossssssssssssysssooyyyyyso+//++//shNNNNNNNNNNNNNM
    # MNNNNNNNNNNNNNNMNy////////++++oooooooooossssssssoosssssysyyysoossss+/oshNNNNNNNNNNM
    # MNNNNNNNNNNNNMNs///////+oooooo++++oooooooooooso+ossssssssssssssssssss++soymMNNNNNNM
    # MNNNNNNNNNNNMd/:-//+//shNNmhsoo+++++++++ooooo++oooooooooossssssssssssso+ooosmNNNNNM
    # MNNNNNNNNNNMh::://+/+ymMMMMmhsoso+++++++++o+/+ooooooooooooooooooooossso++o+++hMNNNM
    # MNNNNNNNNNMy//-:/+/osmMMMMNhssyshNdssoooo++:++++++++++oooooooooooooooooo++-++/sMMNM
    # MNNNNNNNNMd:/:///+/ohNMMMNhsohyyNMNNNdhhs+:++++++++++++++++++++ooooooooo/+.o+:/+NNM
    # MNNNNNNNMm/:/-///++ooshmmhs+sysdMMMMNdMMd/+++++ooo++++++++++++++++++++++::-++/:/sNM
    # MNNNNNNMN/://-+++++++++oo+//yosNMNMNmNMNo/o/oshNmhyoo+++++++++++++++++++/-/+++:/:sM
    # MNNNNNMNo://-/+++++:/+++++//++osyhmdhMNs/o/+shMMMMmsooooyo++/+++++++++++://+++://oM
    # MNNNNNMs:///:/++++//++-/+/:++++++ooooyo++o-oyNNMMmysooymmso/+shysyyysooo+/++o+/-s+M
    # MNNNNMd:///+:/++++-++:`++:/++++//++++++:+-/oyhsmys+oohmyo++:sNMdmMMNNysy+-ohNs+-myM
    # MNNNMN::///+-:+++:.+/``++/++++++++++++:+/`+++oo/:/++oyo+oy+odNddMMMMmyyh:-sdMh/odyN
    # MNNNNo:///++-:+o/`::```++/+++++++++++//+-.o++:-:/++/+/+ymo/+ossyyhdhssy+.:ohhd/sy+M
    # MMNMh-///+++--oo:`/````++-+++++++++++-o/`/+:.:/+++//+hmNo/++++++ooooooo-`/+o++/++-M
    # MMMN/:///+++-.o/````-s:+/:++++++++++/++`.:.-/++++/+sdmmo/+++++++++++++: -+++++////M
    # MMMh:///++++-`+:```/dN+/::++++++++++++:``.+ooo++ohNMNm++oooooooo+++++o+ :++++/-//oM
    # MMd:/-/+++++-`/.``:hmm//./+++++++++o/o..:osoooymmdddmoooooooooooooo+oms.+++++////+M
    # MMo// -+++++:`.`` dNddo-.:+++++++++++--/soo:.--::ymh+ssssssssssooo+sNN/++++++++/-dM
    # Md/// `/+++o/```` dMddN.-:++++++++++/`/o/+:``-:-`/ooyssssssssssssoodmMo++++++++//NM
    # M/:// `-+oooo.``` oMNMM+--/+++++++++/:yd-``.`-+o+hoyyoosyyyyyyys:+o+o++o//+++++/hMM
    # m++:/```:oooo/````.dmNNm/-/+++++++//+dhy::ohs:/hysyosyyyyyyyyys:----:-/o/ooo++/-mMM
    # s:++//```/oooo-  ``yNmdm:-/++++++////MMNmdhoys+ssssyyyyyysoysss:-.odd/o+/+oo++-+MMM
    # s`:++/````:oooo. ```:hNNh-/++++++//:hNNNMMNMdsossyyyyyyss+osdM/o/:yNyoo///ooo/.MMNM
    # d `-++/-```:+oo+-`````-+ds/++++++//-mMMMNNhs+syyysysyys+osdMMNyoshdh/+/o:ooo+.+MMNM
    # M/` `-/+/-``.:ooo-```````s:++++++++/mNdhsoossssyyhyo/-+hmMMMMNNNNNNo//+.:oo++ oMMNM
    # MMo``:..-//-.`-+oo:.`````/+++++++++:ooossyhyyyo+:-:ohNMmMMMMMNmNNNh:/:` :oo/: mMMNM
    # MMMh.oMh+``.-:-.-/o+-````mh/+++++++:++++/:--:+syhmMMMMMNMMMMMMMMMo-.//``+oo:`-MMNNM
    # MMMMh-omNd+````..`./+/.`hMMs+++++++/dmmmmNMMNNMMMMMMMMMMMMMMMMms:`` :/..+oo: yMNNNM
    # MNNNMN/``..``````````.-.+dNy-oooooo/o+s++sNMMNmNMMmmNMMMMMMMmo-   ``-/.-oo+- yMNNNM
    # MNNNNMMNdy-``````..``````-+o/+ooooo/++///:`:yMMMMMMMMMMMMds/`/++/````o--o++- MMNNNM
    # MMNNMMMMMN:`........-:+oyssoo+ssssss:ooo+/+:`:mMMMMMNho/.````+ooohd+//:+ooo-/MMMMMM
    # MMMMMMMMMMs.-...-.-osyyyyysdMhshhhhhossssssdh-.ss+/-.``----.sdhy+mMMMsosssy:sMMMMMM
    # endregion --------------------------------------------------------------------------------------|
    # region -----------------------------------------------------------------------------------------|
    class Dsu:
    def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [1] * n
    
    def find(self, x):
            while x != self.parent[x]:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x
    
    def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px == py: return 0
            if self.rank[py] > self.rank[px]:
                px, py = py, px
            self.parent[py] = px
            self.rank[px] += self.rank[py]
            return 1
    
    def get_size(self, x):
            return self.rank[self.find(x)]
    
    class SegTree:
    def __init__(self, n, array):
            self.n = n
            self.tree = [0] * (2 * n)
            for i in range(n, 2 * n):
                self.tree[i] = array[i - n]
            for i in range(n - 1, -1, -1):
                self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
        
    def update(self, i, val):
            i += self.n
            self.tree[i + self.n] = val
            while i:
                self.tree[i//2] = self.tree[i] + self.tree[i ^ 1]
                i //= 2
    
    def query(self):
            pass
    
    def top(self):
            return self.tree[0]
    
    class Comba:
    def __init__(self) -> None:
            self.facs = [0] * MX; self.facs[0] = 1
            self.fac_invs = [0] * MX
    
            for i in range(1, MX):
                self.facs[i] = (self.facs[i - 1] * i) % mod
    
            self.fac_invs[MX - 1] = pow(self.facs[MX - 1], mod - 2, mod)
            for i in range(MX - 2, -1, -1):
                self.fac_invs[i] = (self.fac_invs[i + 1] * (i + 1)) % mod
    
    def ncr(self, n, r):
            if r > n or n < 0 or r < 0: return 0
            return ((self.facs[n] * self.fac_invs[r]) % mod * self.fac_invs[n - r]) % mod
        
    def npr(self, n, r):
            if r > n or n < 0 or r < 0: return 0
            return (self.facs[n] * self.fac_invs[n - r]) % mod
    
def is_prime(n):
        for div in range(2, int(2, n ** 0.5) + 1):
            if n % div == 0: return False
        return True
    
def lcm(x, y): return (x * y) // gcd(x, y)
    
def rw_file(confirm):
        if not confirm: return None
        sys.stdin = open(r"", "r")
        sys.stdout = open(r"", "w")
    
def re(data=str): return data(sys.stdin.readline().rstrip())
def mp(data=str): return map(data, sys.stdin.readline().split())
    
    import sys
    from bisect import bisect_left, bisect_right, insort_left
    from math import ceil, floor, log, gcd, sqrt
    from collections import Counter, deque
    from heapq import heappush, heappop, heapify
    
    mod, inf, MX, nl = 1000000007, 1e18, 210001, "\n"
    # endregion --------------------------------------------------------------------------------------|
    
def solve(tc):
        n, k = mp(int)
        even, odd = 0, 0
        for i in range(n):
            if i & 1: odd += c.ncr(n, i)
            else: even += c.ncr(n, i)
        
        dp = [[0, 0] for i in range(k + 1)]
        dp[0][0] = 1
        for i in range(1, k + 1):
            dp[i][1] += dp[i - 1][1] * odd
            dp[i][1] += dp[i - 1][1] * even
            dp[i][0] += dp[i - 1][0] * even
            dp[i][1] += dp[i - 1][1]
            if n & 1:
                dp[i][0] += dp[i - 1][0]
            else:
                dp[i][1] += dp[i - 1][0]
            dp[i][1] %= mod; dp[i][0] %= mod
        
        print((dp[-1][0] + dp[-1][1]) % mod)
    
        return None
     
def main():
        rw_file(False)
        global c; c = Comba()
        cases = 1; cases = re(int)
        for tc in range(cases):
            solve(tc + 1)
     
    main()