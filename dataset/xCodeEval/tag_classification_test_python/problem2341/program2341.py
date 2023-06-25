def program2341():
    n = int(input());
    B = list(map(int, input().split()));
    sum = 0;
    A = [];
    for w in range(len(B)):
        sum = 0;
        for q in range(w, len(B)):
            sum = sum + B[q];
            if sum >= 180:
                A.append(min(2 * abs(180 - sum), 2 * abs(180 - sum - B[q])));
                break;
        B.append(B[w]);
    print(min(A));