def program2690():
    if __name__ == '__main__':
        w,h,k = map(int, input().split())
        sum1 = 0
        for i in range(k):
            if w > 0 and h > 0:
                sum1 += 2*(h+w) - 4
                h -= 4
                w -= 4
        print(sum1)