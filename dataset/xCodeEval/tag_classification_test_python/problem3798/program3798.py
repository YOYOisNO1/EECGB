def deposit(cash):
        if cash >= 0:
            return cash
        if str(cash)[-1] < str(cash)[-2]:
            result = str(cash)[:-2] + str(cash)[-1]
        else:
            result = str(cash)[:-1]
        return int(result)
        
    print(deposit(int(input())))