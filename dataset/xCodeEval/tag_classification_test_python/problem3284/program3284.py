    
def loop(arr, n):
      
      if arr[0] > 15: return 15
    
      for i in range(n):
        if arr[i] + 15 < arr[i + 1]:
          return arr[i] + 15
      
      return 90
      
def main():
      
      n = int(input())
      
      arr = list(map(int, input().split()))
      
      arr.append(90)
      
      print(loop(arr, n))
    
    if __name__ == "__main__": main()