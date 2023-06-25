    #stdin.readline()
    #int(stdin.readline())
    #stdout.write()
    #input()
    #map(int,input().split())
    #map(int,stdin.readline().split())
def main():
        n=input()
        print(n+(n*(n*(n-1))/2)-((n-1)*n*(2*n-1))/6)
    if __name__ == "__main__":
        from sys import stdin, stdout
        main()