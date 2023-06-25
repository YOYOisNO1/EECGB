def main():
        dic = {0: 'Sheldon', 1: 'Leonard', 2: 'Penny', 3: 'Rajesh', 4: 'Howard'}
        n = int(input())
        n -= 1
        while n >= 5:
            n -= 5
            n = n // 2
        print(dic[n])
    
    
    if __name__ == "__main__":
        main()