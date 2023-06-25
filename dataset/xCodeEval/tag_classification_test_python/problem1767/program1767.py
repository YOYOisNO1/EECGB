    from sys import stdin, stdout
    
    
def read_line():
        return stdin.readline().strip()
    
    
def print(value):
        stdout.write(str(value))
    
    
def main():
        desired_i, desired_j = 2, 2
        for i in range(5):
            row_line = read_line()
            row_lst = row_line.split(" ")
            try:
                j = row_lst.index("1")
                minimal_moves = abs(i - desired_i) + abs(j - desired_j)
                print(minimal_moves)
                break
            except:
                continue
    
    
    if __name__ == '__main__':
        main()