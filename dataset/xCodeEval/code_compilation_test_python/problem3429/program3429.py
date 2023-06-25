def DFS(depth, start, str, used):
        if start >= len(str):
            return None
        if str[start] in used:
            return None
        if depth == 1:
            return [str[start:]]
        for i in range(start, len(str)):
            res = DFS(depth - 1, i + 1, str, used + str[start])
            if res != None:
                return res + [str[start:i+1]]
        return None
    
    
def main():
        k = int(input())
        str = input()
        res = DFS(k, 0, str, "")
        if res == None:
            print("NO")
        else:
            print("YES")
            res.reverse()
            for token in res:
                print(token)
    
    
    if __name__ == '__main__':
        main()