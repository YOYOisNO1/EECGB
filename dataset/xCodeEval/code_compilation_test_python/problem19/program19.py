    class Solution:
    def remove(self,a):
            b = []
            i = len(a)-1
            n = len(a)
            while i >= 0:
                if a[i] not in b:
                    b.append(a[i])
                i = i - 1
            return b
def printc(x):
        i = len(x) - 1
        while i >= 0:
            print (x[i])
            i = i - i
    x = input()
    a = [int(x) for x in input().split()]
    t = Solution()
    printc(t.remove(a))