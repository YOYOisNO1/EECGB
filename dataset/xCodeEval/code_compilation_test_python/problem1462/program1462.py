    def count_days(r,b):
            hipster = min(r,b)  # 👲
            normal = abs(r-b)//2  # 👨
            return hipster, normal
         
         
        if __name__ == "__main__":
            red, blue = map(int, input().split())
            res = count_days(red, blue)
            print(" ".join(map(str, res)))