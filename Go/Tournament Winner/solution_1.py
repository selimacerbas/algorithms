HOME_TEAM_WON = 1

def tournamentWinner(competitions, results):
    currentWinner = ""
    dic = {currentWinner : 0} 

    for i , competition in enumerate(competitions):
        result = results[i]
        homeTeam , awayTeam = competition

        winner = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winner , 3 , dic)

        if dic[winner] > dic[currentWinner]:
            currentWinner = winner

    return currentWinner

def updateScores(team, points, hashTable):

    if team not in hashTable:
        hashTable[team] = 0
    
    hashTable[team] += points

