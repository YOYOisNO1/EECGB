def solution(l1):
        #do the two separately
        rect2 = l1[2]+l1[3]
        rect1 = l1[0]+l1[2]
        bottom = l1[0]+2*l1[1]+2
        top = l1[2]+2*l1[3]+2
        hang = abs(l1[0]-l1[2])
        return top+bottom+hang
        
def answer():
        l1 = [int(x) for x in input().split()]
        print(solution(l1))
    answer()