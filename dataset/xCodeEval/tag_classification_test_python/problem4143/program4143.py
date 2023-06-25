def r(): return input().strip()
def ri(): return int(r())
def riv(): return map(int, r().split())
    
def happy(a,b):
        return "".join(filter(lambda s: s in ("4", "7"), list(a))) == b
    
def main():
        a,b = r().split()
        ai,bi = map(int, [a,b])
        if bi > ai:
            print(b)
            exit(0)
        
        i = 1
        while True:
            if happy(str(ai+i), b):
                print(str(ai+i))
                exit(0)
            i += 1
            
    if __name__ == "__main__":
        main()