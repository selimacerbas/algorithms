package main

const HOME_TEAM_WON = 1

func TournamentWinner(competitions [][]string, results []int) string {

	currentBestTeam := ""
	scores := map[string]int{currentBestTeam: 0}

	for i, competition := range competitions {

		result := results[i]
		homeTeam, awayTeam := competition[0], competition[1]

		winner := awayTeam

		if result == HOME_TEAM_WON {
			winner = homeTeam
		}

		updateScores(winner, 3, scores)

		if scores[winner] > scores[currentBestTeam] {
			currentBestTeam = winner
		}

	}

	return currentBestTeam

}

func updateScores(team string, points int, scores map[string]int) {

	scores[team] += points
}
