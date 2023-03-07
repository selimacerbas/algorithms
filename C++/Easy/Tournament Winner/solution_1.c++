#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

const int HOME_TEAM_WON {1};

string tournamentWinner(vector<vector<string>> competitors, vector<int> results)
{
    string currentBestTeam {""};
    unordered_map<string,int> scores = {{currentBestTeam, 0}};

    for (int i {0} ; i < competitors.size() ; i++)
    {
        auto result = results[i];
        auto competitor = competitors[i];
        auto homeTeam = competitors[0];
        auto awayTeam = competitors[1];
        auto winner = result == HOME_TEAM_WON ? homeTeam : awayTeam;

    
        updateScores(winner, 3, scores);

        if (scores[winner] > scores[currentBestTeam])
            currentBestTeam = winner;

    }
    
    return currentBestTeam;
}

void updateScores (string team, int point , unordered_map<string, int> &scores)
{
    if (scores.find(team) == scores.end())
        scores[team] = 0;
    
    scores[team] += point;
    

}