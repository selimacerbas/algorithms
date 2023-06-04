#include <string>
#include <unordered_set>

using namespace std;

vector<vector<string>> semordnilap(vector<string> words);

vector<vector<string>> semordnilap(vector<string> words)
{
    unordered_set<string> wordsSet(words.begin(), words.end());
    vector<vector<string>> pairs;

    for(auto word : words)
    {
        string reversedWord = word;
        reverse(reversedWord.begin() , reversedWord.end());
        if(wordsSet.find(reversedWord) != wordsSet.end() && reversedWord != word)
        {
            pairs.push_back({word, reversedWord});
            wordsSet.erase(word);
            wordsSet.erase(reversedWord);
        }
    }
    return pairs;
}