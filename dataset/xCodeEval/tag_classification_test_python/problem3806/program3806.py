    """CodeForce Q915C - Permute Digits (http://codeforces.com/contest/915/problem/C)
    """
    
    import bisect
    
def main():
        a = list(input())
        b = list(input())
    
        a.sort()
        ans = ''
        if len(a) < len(b):
            ans = ''.join(reversed(a))
        else:
            for i in range(len(b)):
                idx = bisect.bisect_left(a, b[i])
                if idx < len(a) and a[idx] == b[i]:
                    del a[idx]
                    if a > b[i + 1:]:
                        ans += a[idx - 1]
                        a[idx - 1] = b[i]
                        ans += ''.join(reversed(a))
                        break
                    ans += b[i]
                else:
                    ans += a.pop(idx - 1)
                    ans += ''.join(reversed(a))
                    break
    
        print(ans)
    
    
    if __name__ == '__main__':
        main()