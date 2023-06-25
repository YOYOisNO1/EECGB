def main():
        lgames = []
        nteams = int(input())
        for i in range(nteams):
            lgames.append(tuple(map(int, input().split())))
    def games(lgames, nteams):
            counter = 0
            for team in range(nteams):
                current_team = lgames[team]
                for agnist_team in lgames:
                    if current_team[0] == agnist_team[1]:
                        counter += 1
            return counter
    
        print(games(lgames, nteams))
    
    if __name__ == "__main__":
        main()