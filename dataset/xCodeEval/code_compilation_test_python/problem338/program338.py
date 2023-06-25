    from itertools import combinations as com
def Triangles():
        N = int(input())
        sides = list(map(int, input().split()))
        if 3 in sides and 4 in sides and 5 in sides:
            return "YES"
        for i in sorted(com(sides,3)):
            if i[0] + i[1] > i[2] and i[0] + i[2] > i[1] and i[1] + i[2] > i[0]:
                return "YES"
        return "NO"
    print(Triangles())