    import sys
    import math
    import bisect
    
def main():
        A = []
        for i in range(3):
            A.append(int(input()))
        B = [0] * 3
        B[0] = A[0] // 1
        B[1] = A[1] // 2
        B[2] = A[2] // 4
        print(min(B) * 7)
    
    if __name__ == "__main__":
        main()