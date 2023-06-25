    from __future__ import print_function
    from fractions import Fraction;
def main():
        a,b,c = map(int,input().split())
        x = Fraction(a,b);
        x=x.limit_denominator(c);
        print(x.numerator,'/',x.denominator,sep='')
    if __name__ == '__main__':
        main()