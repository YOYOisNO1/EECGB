    import sys
    from fractions import Fraction
    
def calc(x, y, n):
        return Fraction(x, y).limit_denominator(n)
        
def solve(lines, output):
        x, y, n = (int(i) for i in lines.readline().split())
        f = calc(x, y, n)
        output.write('{0}/{1}\n'.format(f.numerator, f.denominator))
    
    if __name__ == '__main__':
        solve(sys.stdin, sys.stdout)