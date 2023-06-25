    import sys
    
    
def solve(input_path=None):
        if input_path is None:
            f = sys.stdin
        else:
            f = open(input_path, 'r')
    
        n = int(f.readline())
        paper1, rock1, scissor1 = map(int, f.readline().split())
        paper2, rock2, scissor2 = map(int, f.readline().split())
    
        min_win = n - (min(paper1, paper2 + scissor2) + min(rock1, rock2 + paper2) + min(scissor1, scissor2 + rock2))
        max_win = min(paper1, rock2) + min(rock1, scissor2) + min(scissor1, paper2)
        
        return [f"{min_win} {max_win}"]
    
    
def main():
        for line in solve():
            print(f"{line}")
    
    
    if __name__ == '__main__':
        main()