def Triangle(List):
        
        List = sorted(List)[::-1]
        
        if List[1]+List[2] > List[0] or List[1]+List[3] > List[0] or List[2]+List[3] \
        > List[0] or List[2]+List[3] > List[1]: return 'TRIANGLE'
        
        elif List[1]+List[2] == List[0] or List[1]+List[3] == List[0] or \
        List[2]+List[3] == List[0] or List[2]+List[3] == List[1]: return 'SEGMENT'
        
        return 'IMPOSSIBLE'
    
    
    for i in range(1):
        All = [int(i) for i in input().split()]
    
    print(Triangle(All))