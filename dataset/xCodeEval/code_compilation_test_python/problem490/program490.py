def pba():
        ri=input()
        print 'yes' if or ri.lstrip('0').count('0')>=6 else 'no'
    
def pbb():
        import itertools
    def doable(cube,num):
            for perm in itertools.permutations(cube,len(num)):
                sweg=True
                for i in range(len(num)):
                    if num[i] not in perm[i]:
                        sweg=False
                if sweg:
                    return True
            return False
        cube=[]
        ncubes=int(input())
        for _ in range(ncubes):
            cube.append(input().split())
        i=1
        while doable(cube,str(i)):
            i+=1
        print i-1
    
def pbc():
        cube=input().split()
        configs=[[1,3,6,8,5,7,10,12,9,11,21,23,2,4,22,24,13,14,15,16,17,18,19,20],
                 [1,3,21,23,22,24,10,12,9,11,6,8,5,7,2,4,13,14,15,16,17,18,19,20],
                 [13,14,7,8,5,6,19,20,17,18,23,24,21,22,15,16,9,10,11,12,1,2,3,4],
                 [5,6,15,16,17,18,7,8,21,22,19,20,13,14,23,24,1,2,3,4,9,10,11,12],
                 [1,2,17,19,18,20,9,10,11,12,14,16,13,15,3,4,5,6,7,8,21,22,23,24],
                 [1,2,14,16,13,15,9,10,11,12,17,19,18,20,3,4,5,6,7,8,21,22,23,24]]
        goodconf=False
        for config in configs:
            assert sorted(config)==range(1,25)
            goodtmp=True
            for i in range(0,24,4):
                if not cube[config[i]-1]==cube[config[i+1]-1]==cube[config[i+2]-1]==cube[config[i+3]-1]:
                    goodtmp=False
            if goodtmp:
                goodconf=True
        if goodconf:
            print 'YES'
        else:
            print 'NO'
    pba()
                    