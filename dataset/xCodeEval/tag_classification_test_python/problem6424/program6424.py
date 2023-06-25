    """RANK1ZEN; 3966 PEAK; NA; FLEX SUPPORT: Zen, Bap; Battlenet ID -> Knuckles#11791"""
    # region ---------------------------------------------------------------------------|
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
    # endregion ------------------------------------------------------------------------|
    # region ---------------------------------------------------------------------------|
    from sys import stdin, stdout
    from bisect import bisect_left, bisect_right
    from math import ceil, floor, log, gcd, sqrt
    from collections import Counter, deque
    from heapq import heappush, heappop, heapify
def re(): return stdin.readline().rstrip()
def ints(): return map(int, stdin.readline().split())
def test(tc): 
        for _ in range(tc): solve()
    mod = 1000000007
    nl = "\n"
    # endregion
    # region ---------------------------------------------------------------------------|
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
            self.tree[i] = val
            while i:
                self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
                i //= 2
    
    def query(self):
            pass
    
    def top(self):
            return self.tree[0]
    
    
    
    # endregion ------------------------------------------------------------------------|
    
def solve():
        n, m = ints()
        dp = [0] * (n + 1); dp[n] = 1
        suf = [0] * (n + 2); suf[n] = 1
        for i in range(n - 1, 0, -1):
            dp[i] = suf[i + 1] % m
            for mul in range(2, n + 1):
                lo = i * mul
                hi = (i + 1) * mul - 1
                if lo > n: break
    
                dp[i] = (dp[i] + suf[lo] - suf[min(n, hi) + 1]) % m
    
            suf[i] = (suf[i + 1] + dp[i]) % m
        
        print(dp[1] % m)
        return
    
    test(1)