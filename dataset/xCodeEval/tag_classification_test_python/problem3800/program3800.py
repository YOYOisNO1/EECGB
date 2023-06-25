def GI(): return int(input())
def GIS(): return map(int, input().split())
    
def convert(digits, base):
        s = 0
        for i, d in enumerate(reversed(digits)):
            s += d * base ** i
        return s
    
def main():
        _, base_x = GIS()
        x_s = GIS()
        _, base_y = GIS()
        y_s = GIS()
    
        x, y = convert(x_s, base_x), convert(y_s, base_y)
        return ('=' if x == y else 
                '>' if x >  y else
                '<')
    
    
    print(main())