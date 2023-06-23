    import heapq
    
    
def main():
        n, m = map(int, input().split())
        stack = [(0,n)]
        while stack:
            count, node = heapq.heappop(stack)
            if node == m:
                print(count)
                break
            a ,b = node*2, node -1
            if 1<=a<=10000:
    
                heapq.heappush(stack,(count+1,a))
            if 1<=b<=10000
                heapq.heappush(stack,(count+1,b))
    
    
    
    if __name__=="__main__":
        main()