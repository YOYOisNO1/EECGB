    import sys
    input = sys.stdin.readline
    
    class Node:
  def __init__(self, val, j =None, l1 = None, l2 = None):
        self.val = val
        self.l1 = l1
        self.l2 = l2
        self.limit = j
    
def bfs(arr, n, k, l):
      # for i in range(len(arr)):
      #   for j in range(len(arr[0])-1):
      #     print(arr[i][j].val, arr[i][j].l1, arr[i][j].l2)
      start = arr[0][0]
      from collections import deque
      q = deque([])
      closed = []
      q.append(start)
      while len(q) > 0:
        node = q.popleft()
        closed.append(node)
        if node.val <= l:
          # print(node.val, node.limit, n-1, node.l1, node.l2, q), 
          if node.limit == n-1:
            if node.val <= l:
              return "Yes"
            else:
              if len(q) == 0:
                return "No"
          else:
            if node.l1 or node.l2:
              if node.l1.val:
                if node.l1 not in closed:
                  q.append(node.l1)
              if node.l2.val:
                if node.l2 not in closed:
                  q.append(node.l2)
    
      return None
    
def riverCross(arr, n, k, l):
      sample = [[Node(ele) for ele in arr]]
      # print(sample)
      for i in range(k):
        sample.append(list(map(lambda x: Node(x.val + 1), sample[i])))
      for i in range(k-1):
        sample.append(list(map(lambda x: Node(x.val - 1), sample[i+k])))
      # for i in range(len(sample)):
      #   for j in range(len(sample[0])):
      #     print(sample[i][j].val)
    
      # adj = [None for i in range(100)]
      for i in range(len(sample)):
        for j in range(len(sample[0])):
          # sample[i][j] = 0
          # nodes = None
          if i< 2*k -1 and j < n-1:
            sample[i][j].l1 = sample[i + 1][j]
            sample[i][j].l2 = sample[i + 1][j + 1]
            sample[i][j].limit = j
            # print(i, j, 'f')
          elif j < n-1:
            sample[i][j].l1 = sample[0][j]
            sample[i][j].l2 = sample[0][j + 1]
            sample[i][j].limit = j
    
            # print(i, j, 's')
          else:
            sample[i][j].l1 = None
            sample[i][j].l2 = None
            sample[i][j].limit = j
    
            # print(i, j, 't')
    
      # for i in range(len(sample)):
      #   for j in range(len(sample[0])-1):
      #     print(sample[i][j].val, sample[i][j].l1.val, sample[i][j].l2.val)
      ans = bfs(sample, n, k, l)
      # print(sample)
      # print(ans)
      if ans == None:
        print('No')
      else:
        print(ans)
    
    
def solution():
     
      values = list(map(lambda x: int(x), input().split()))
      n = values[0]
      k = values[1]
      l = values[2]
      # n = 5
      # k = 2
      # l = 3
      # arr = [1, 2, 3, 2, 2]
      arr = list(map(lambda x: int(x), input().split()))
      riverCross(arr, n, k, l)
      
    t = int(input());
    # t = 1
    for i in range(0, t):
      solution()
      