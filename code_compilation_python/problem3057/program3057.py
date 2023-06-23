    # нужно выспаться 
def main():
        n, m = map(int, input().split())
        a_arr = map(int, input().split())
        result = set()
        for i, a_i in enumerate(a_arr):
            tmp = m - a_i
            j = i + 1
            if tmp != 0:
                while j < len(a_arr) and tmp != 0:
                    if a_arr[j] <= tmp:
                        tmp -= a_arr[j]
                        j += 1
                    else:
                        break
            result.add(j)
        print len(result)
    
    
    if __name__ == '__main__':
        main()