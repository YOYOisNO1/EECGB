def change_color(color, n):
        can_be_used = 'ROYGBIV'
        can_be_used = can_be_used.replace(color[n-3], '')
        can_be_used = can_be_used.replace(color[n-2], '')
        can_be_used = can_be_used.replace(color[n-1], '')
        can_be_used = can_be_used.replace(color[n+1], '')
        can_be_used = can_be_used.replace(color[n+2], '')
        can_be_used = can_be_used.replace(color[n+3], '')
        if color[n] in can_be_used:
    	return color
        elif n == -1:
    	return color[:n] + can_be_used[0]
        else:
    	return color[:n] + can_be_used[0] + color[n+1:]
    
def solve(n):
        color = 'ROYGBIV' * (n / 7) + 'ROYGBIV'[:n % 7 - 7]
        color = change_color(color, -4)
        color = change_color(color, -3)
        color = change_color(color, -2)
        color = change_color(color, -1)
        print(color)
    
def main():
        n = int(input())
        solve(n)
    
    main()