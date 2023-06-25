def program710():
    """
    Created on Tue Sep 15 17:11:02 2020
    
    @author: ADMIN
    """
    
    
    if __name__ == "__main__":
        numbers = input().split("+")
        numbers =  [int(number) for number in numbers]
        numbers.sort()
        
        res = ""
        for i in range(len(numbers) - 1):
            # print(numbers[i])
            # print("+")
            res += str(numbers[i]) + "+"
            
        res += str(numbers[-1])
        
        print(res)