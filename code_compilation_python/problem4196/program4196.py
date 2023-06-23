def sort(a):
      n = len(a)
      b = [0 for i in range(n)]
  def mergeSort(l, r):
        if r - l <= 1: return
        global cnt
        m = (l + r) >> 1
        mergeSort(l, m)
        mergeSort(m, r)
        i, j, k = l, m, l
        while i < m and j < r:
          if log[cnt] == '0':
            g[a[i]].append(a[j])
            b[k] = a[i]
            i += 1
          else:
            g[a[j]].append(a[i])
            b[k] = a[j]
            j += 1
          k += 1
          cnt += 1
        while i < m:
          b[k] = a[i]
          i += 1
          k += 1
        while j < r:
          b[k] = a[j]
          j += 1
          k += 1
        for p in range(l, r):
          a[p] = b[p]
      mergeSort(0, n)
      return "".join(log)
    
def dfs(v, p):
      u[v] = 1
      for to in g[v]:
          if (to != p and not u[to]):
            dfs(to, v)
      top_sort.append(v)
    
    log = input()
    g = [[] for i in range(16)]
    top_sort, u = [], [0 for i in range(16)]
    cnt = 0
    
    sort([i for i in range(16)])
    
    for i in range(16):
      if (not u[i]):
        dfs(i, -1)
    
    ans = [0 for i in range(16)]
    top_sort = top_sort[::-1]
    for i in range(16):
      ans[top_sort[i]] = i + 1
    print(16)
    print(*ans)
    