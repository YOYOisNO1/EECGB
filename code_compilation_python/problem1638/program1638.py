    509 ~/codeforces/208$ mv 209 ProbA.py
    510 ~/codeforces/208$
def do_pairs_intersect(start1, end1, start2, end2):
        if ((end1 <= start2 or start1 >= end2) or
            (start2>=start1 and start2<=end1 and end2>=start1 and end2<=end1) or
            (start1>=start2 and start1<=end2 and end1>=start2 and end1<=end2)):
            return False
        return True
    
def is_intersecting(points):
        if len(points) == 1:
            print 'no'
        else:
            n = len(points) - 1
            is_intersecting = False
            for i in xrange(n-1):
                for j in xrange(i+1,n):
                    if points[i] <= points[i+1]:
                        start1, end1 = points[i], points[i+1]
                    else:
                        start1, end1 = points[i+1], points[i]
                    if points[j] <= points[j+1]:
                        start2, end2 = points[j], points[j+1]
                    else:
                        start2, end2 = points[j+1], points[j]
                    #print 'comparing(',start1,',',end1,') and (',start2,',',end2,')'
                    if ((start1 == start2 and end1 == end2) or
                        (do_pairs_intersect(start1,end1,start2,end2))):
                        is_intersecting = True
        if is_intersecting:
            print 'yes'
        else:
            print 'no'
    
    nums = map(int, input('').split())
    nums = map(int, input('').split())
    is_intersecting(nums)