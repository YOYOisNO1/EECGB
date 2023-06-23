def main ():
      n, k = [int(n) for n in input().split()]
      S = input();
      doors = {}
    
      for i, s in enumerate(S):
        doors[s] = i
    
      activeDoors = set();
      for i, s in enumerate(S):
        if doors[s] == i:
          activeDoors.remove(s);
        else:
          activeDoors.add(s);
          if(len(activeDoors) > k):
            return "YES"
      
      return "NO"
    
    print(main())