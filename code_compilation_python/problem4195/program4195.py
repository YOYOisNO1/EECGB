def sort(a):
        n = len(a)
        b = [0 for i in range(n)]
        log = []
    
    def mergeSort(l, r):
            if r - l <= 1:
                return
            m = (l + r) >> 1
            mergeSort(l, m)
            mergeSort(m, r)
            i, j, k = l, m, l
            while i < m and j < r:
                if a[i] < a[j]:
                    log.append('0')
                    b[k] = a[i]
                    i += 1
                else:
                    log.append('1')
                    b[k] = a[j]
                    j += 1
                k += 1
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
    
    
def reverseSort(n, log):
        # print(f"reverseSort {n}")
        assigns = []
    
    def mergeSort(l, r, log_id, run_id):
            if r - l <= 1:
                return log_id, run_id-1
            # print(f"mergeSort {l}-{r} {log_id}")
            assigns.append([])
            m = (l + r) >> 1
            log_id, last_run_id = mergeSort(l, m, log_id, run_id+1)
            log_id, last_run_id = mergeSort(m, r, log_id, last_run_id+1)
            i, j, k = l, m, l
            while i < m and j < r:
                if log[log_id] == '0':
                    assigns[run_id].append((k, 0, i))
                    i += 1
                else:
                    assigns[run_id].append((k, 1, j))
                    j += 1
                log_id += 1
                k += 1
            while i < m:
                assigns[run_id].append((k, 0, i))
                i += 1
                k += 1
            while j < r:
                assigns[run_id].append((k, 1, j))
                j += 1
                k += 1
            return log_id, last_run_id
    
        log_id, next_run_id = mergeSort(0, n, 0, 0)
        # print(log_id, assigns)
        if log_id < len(log):
            return []
    
        a = list(range(1, n+1))
        b = [0] * n
    
    def reverseMergeSort(l, r, run_id):
            if r - l <= 1:
                return run_id-1
            m = (l + r) >> 1
            for k, part, i in assigns[run_id]:
                b[i] = a[k]
            for p in range(l, r):
                a[p] = b[p]
            last_run_id = reverseMergeSort(l, m, run_id+1)
            last_run_id = reverseMergeSort(m, r, last_run_id+1)
            return last_run_id
    
        reverseMergeSort(0, n, 0)
    
        return a
    
    
    log = input()
    n = 1
    a = []
    while not a:
        n += 1
        a = reverseSort(n, log)
    print(len(a))
    print(' '.join(map(str, a)), flush=True)
    # new_log = sort(a)
    # assert new_log == log