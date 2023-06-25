    # python2 or 3
    import sys, threading, os.path
    import collections, heapq, math,bisect
    import string
    from platform import python_version
    import itertools
    sys.setrecursionlimit(10**6)
    threading.stack_size(2**27)
    
    
def main():
        if os.path.exists('input.txt'):
            input = open('input.txt', 'r')
        else:
            input = sys.stdin
        #--------------------------------INPUT---------------------------------
        studs = []
        for i in range(5):
            studs.append(list(map(int, input.readline().split())))
        allperm = list(itertools.permutations([1,2,3,4,5]))
        fineres = 0
        allres = []
        for lis in allperm:
            sum = 0
            sum += studs[lis[0]-1][lis[1]-1]+studs[lis[1]-1][lis[0]-1]
            sum += studs[lis[2]-1][lis[3]-1]+studs[lis[3]-1][lis[2]-1]
    
            sum += studs[lis[1]-1][lis[2]-1]+studs[lis[2]-1][lis[1]-1]
            sum += studs[lis[3]-1][lis[4]-1]+studs[lis[4]-1][lis[3]-1]
    
            sum += studs[lis[2]-1][lis[3]-1]+studs[lis[3]-1][lis[2]-1]
            sum += studs[lis[3]-1][lis[4]-1]+studs[lis[4]-1][lis[3]-1]
            allres.append(sum)
        output= max(allres)
        #-------------------------------OUTPUT----------------------------------
        if os.path.exists('output.txt'):
            open('output.txt', 'w').writelines(str(output))
        else:
            sys.stdout.write(str(output))
    
    
    if __name__ == '__main__':
        main()
    #threading.Thread(target=main).start()
    