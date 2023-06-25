def program4672():
    n, k = input().split()
    guests = input()
    
    
    if __name__=="__main__":
        guests_dict = dict()
        
        for i in range(0, len(guests)):
            guests_dict[guests[i]] = i
        k = int(k)
        doors = 0
        b = set()
        for i in range(0,len(guests) - 1):
            b.add(guests[i])
            if len(b) > k:
                print("YES")
                exit()
            if guests_dict[guests[i]] == i:
                b.remove(guests[i])
        print("NO")