def program287():
    n, k = map(int, input().split())
    ratings = list(map(int, input().split()))
    
    rating2student_idx = {}  # student idx is 1-indexed
    for i in range(n):
        rating = ratings[i]
        if rating not in rating2student_idx:
            rating2student_idx[rating] = i + 1
    
    if len(rating2student_idx) >= k:
        num_added = 0
        student_idxs = []
        for rating, student_idx in rating2student_idx.items():
            student_idxs.append(str(student_idx))
            num_added += 1
            if num_added == k:
                break
    
        print('YES')
        print(' '.join(student_idxs))
    else:
        print('NO')