    import atexit,io,sys
    buffer=io.BytesIO()
    sys.stdout=buffer
    @atexit.register
def write(): sys.__stdout__.write(buffer.getvalue())
    from sys import stdin, stdout
def main():
        s_obt = 0
    def myord(num):
            nonlocal s_obt
            s_obt += num
            return num
            
        s_min = 4.5 * int(stdin.readline())
        cal = (int(x) for x in stdin.readline().split())
        #s_obt = sum(cal)
        #cal.sort()
        cal=sorted(cal,key=myord)
        nt=0
        while s_min>s_obt:
            s_obt += 5-cal[nt]
            nt += 1
        stdout.write(str(nt))
            
    if __name__=='__main__':main()