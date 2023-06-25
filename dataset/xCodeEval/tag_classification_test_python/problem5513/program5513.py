def program5513():
    a, x, y = map(int, input().split())
    ans = 0
    if abs(x) >= a:
        ans = -1
    elif a / 2 <= abs(x) < a:
        if y < a:
            ans = -1
        else:
            if (y // a) % 2 != 0 or y % a == 0:
                ans = -1
            else:
                if x > 0:
                    ans = 4 + 3 * ((y - a) // (2 * a))
                else:
                    ans = 3 + 3 * ((y - a) // (2 * a))
    elif abs(x) < a / 2:
        if x == 0:
            if 0 < y < a:
                ans = 1
            else:
                if (y // a) % 2 != 0 and y % a != 0:
                    ans = 2 + 3 * ((y - a) // (2 * a))
                else:
                    ans = -1
        else:
            if y % a == 0:
                ans = -1
            else:
                if 0 < y < a:
                    ans = 1
                else:
                    if (y // a) % 2 == 0:
                        if x > 0:
                            ans = 4 + 3 * ((y - a) // (2 * a))
                        else:
                            ans = 3 + 3 * ((y - a) // (2 * a))
                    else:
                        ans = 2 + 3 * ((y - a) // (2 * a))
    print(ans)