    
    # get the number of round as n
    # get the amount of first person take rock paper scissors as r1 s1 p1 as follow
    # get the amount of second person take rock paper scissors as r2 s2 p2 as follow
    # how to win ? r1_s2 p1_r2 s1_p2
    
    
    round = int(input())
    firstperson = input().split(" ")
    secondperson = input().split(" ")
    
    
def solve(round, firstperson, secondperson) :
    
        # find mix win
        win = 0
        secondperson.append(secondperson[0])
        for i in range(len(firstperson)) :
            if int(firstperson[i]) <= int(secondperson[i+1]) :
                findless = int(firstperson[i])
            else :
                findless = int(secondperson[i+1])
            win += findless
    
        del secondperson[3]
    
        #find min win
        secondperson.insert(0, secondperson[2])
    
        for i in range(len(firstperson)) :
            if int(firstperson[i]) > 0:
                diff = min(int(firstperson[i]), int(secondperson[i]))
                firstperson[i] = int(firstperson[i]) - int(diff)
                secondperson[i] = int(secondperson[i]) - int(diff)
                if int(firstperson[i]) > 0:
                    diff = min(int(firstperson[i]), int(secondperson[i+1]))
                    firstperson[i] = int(firstperson[i]) - int(diff)
                    secondperson[i+1] = int(secondperson[i+1]) - int(diff)
    
        print(str(int(firstperson[0]) + int(firstperson[1]) + int(firstperson[2])) + " " + str(win))
    
    
    solve(round, firstperson, secondperson)