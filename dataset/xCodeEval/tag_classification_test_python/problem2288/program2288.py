    import sys;
    
    class MyReader:
    #    file = null;
    def __init__(self):
            filename = "file.in";
            if self.isLocal():
                self.file = open(filename);
            self.str = [""];
            self.ind = 1;
                
    def isLocal(self):
            return len(sys.argv) > 1 and sys.argv[1] == "SCHULLZ";
    
    def nextString(self):
            if self.isLocal():
                return self.file.read();
            else:
                return input();
            
    def nextInt(self):
            return int(self.nextToken());
    
    def nextToken(self):
            if (self.ind >= len(self.str)):
                self.ind = 0;
                self.str = self.nextString().split();
            self.ind += 1;
            return self.str[self.ind - 1];
    
def Solve():
        n = -1;
        try:
            n = rdr.nextInt();
        except Exception:
            return False;
    
        if (n == 0):
            print("O-|-OOOO")
    
        while (n > 0):
            k = n % 10
            if k >= 5:
                sys.stdout.write("-O")
            else:
                sys.stdout.write("O-")
            sys.stdout.write("|")
            m = n % 5
            for i in range (0, m):
                sys.stdout.write("O")
            sys.stdout.write("-")
            for i in range(0, 5 - m - 1):
                sys.stdout.write("O");
            n = n // 10;
            print("");
    
        return True;
    
    rdr = MyReader();
    
    if (not rdr.isLocal()):
        Solve();
    else:
        while (Solve()):
            print("")
    
    