def ret_input():
        data = [int(x) for x in input().split()]
        return data 
    
def bas(data):
        k = data[0]
        r = data[1] 
        for index in xrange(1,11):
            if (k % 10 * index) % 10 == r:
                return index
            elif (k % 10 * index) % 10 == 0:
                return index
            else:
                continue
        return (r / 10) + 1
    
def main():
        data = ret_input()
        print(bas(data))
    
    if __name__ == '__main__':
        main()