def main():
        seat = input()
        n = int(seat[:-1])
        s = seat[-1]
        time = "0fedabc".index( s )
        time += 12 * ( n // 4 )
        time += 6 if n & 1 == 0
        print( time )
    if __name__ == "__main__":
        main()