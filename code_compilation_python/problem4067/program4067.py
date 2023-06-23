def program4067():
    num = [0 for i in range(10)]
    line = input()
    for i in line:
        num[ord(i) - ord('0')] += 1
    ans = 0
    ansstrX = ansstrY = ''.join(sorted(list(line)))
    for firstX in range(1, 10):
        firstY = (10 - firstX) % 10
        cntX = [0 for i in range(10)]
        cntY = [0 for i in range(10)]    
        cntX[firstX] += 1
        cntY[firstY] += 1
        if cntX[firstX] > num[firstX] or cntY[firstY] > num[firstY]:
            continue
        tmpstrX = chr(ord('0') + firstX)
        tmpstrY = chr(ord('0') + firstY)
        tmp = 1
        for i in range(10):
            l = min(num[i] - cntX[i], num[9 - i] - cntY[9 - i])
            cntX[i] += l
            cntY[9 - i] += l
            tmp += l
            tmpstrX += chr(ord('0') + i) * l
            tmpstrY += chr(ord('0') + 9 - i) * l
        l = min(num[0] - cntX[0], num[0] - cntY[0])
        cntX[0] += l
        cntY[0] += l
        tmp += l
        tmpstrX = chr(ord('0')) * l + tmpstrX
        tmpstrY = chr(ord('0')) * l + tmpstrY
        for i in range(10):
            tmpstrX += chr(ord('0') + i) * (num[i] - cntX[i])
            tmpstrY += chr(ord('0') + i) * (num[i] - cntY[i])
        if ans < tmp:
            ans = tmp
            ansstrX = tmpstrX
            ansstrY = tmpstrY
    print ansstrX[::-1]
    print ansstrY[::-1]