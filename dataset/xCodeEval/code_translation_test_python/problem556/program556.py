def main():
        turnNum = int(input())
        # choices include rock, scissor, paper respectively
        aliceChoices = list(map(int, input().split(' ')))
        bobChoices = list(map(int, input().split(' ')))
        
        bobChoices.append(bobChoices.pop(0))
        minWin, maxWin = [0, 0]
        
        # calculate the maximum number of rounds Alice can win
        for i, choice in enumerate(aliceChoices):
            maxWin += min([choice, bobChoices[i]])
            
        # calculate the minimum number of rounds Alice can win
        maximum = max(bobChoices)
        for i, choice in enumerate(bobChoices):
            if choice == maximum and choice + aliceChoices[i] > minWin:
                minWin = choice + aliceChoices[i]
        maximum = max(aliceChoices)
        for i, choice in enumerate(aliceChoices):
            if choice == maximum and choice + bobChoices[i] > minWin:
                minWin = choice + bobChoices[i]
        minWin = minWin - turnNum if minWin > turnNum else 0
        print(f'{minWin} {maxWin}')
    
    if __name__ == '__main__':
        main()