    
    
def quick_way(b):
        if (b[0] == b[1] == b[2]):
            return b[0]
        if ((b[0] + b[1]) * 2 <= b[2]):
            return b[0] + b[1]
        else:
            return (b[0] + b[1] + b[2]) / 3
    
    if __name__ == "__main__":
        a = input()
        players_num = 5
        coins = a.split(" ")
    
        ballunes = sorted([int(x, 10) for x in a.split(" ")])
        print(quick_way(ballunes))
    