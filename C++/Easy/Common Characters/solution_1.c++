#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

// O(n*m) time | 0(c) space - where n is the number of strings, m is the length of longest string
// c is the the number of unique characters across all strings
vector<string> commonCharacters(vector<string> strings);

vector<string> commonCharacters(vector<string> strings)
{
    unordered_map<char, int> charCounts;
    
    for(auto const &str : strings)
    {
        unordered_set<char> setOfChars;
        for(int i = 0 ; i < str.length() ; i++)
        {
            setOfChars.insert(str[i]);
        }

        for(auto letter : setOfChars)
        {
            if(!charCounts.count(letter))
            {
                charCounts[letter] = 0;
            }
            charCounts[letter]++;
        }
    }

    vector<char> finalChar;
    for(auto const &charCount : charCounts)
    {
        //Used for maps
        char character = charCount.first;
        int count = charCount.second;

        if(count == strings.size())
        {
            finalChar.push_back(character);   
        }
    }

    vector<string> finalCharArr;
    for(auto character : finalChar)
    {
        finalCharArr.push_back(string(1,character));
    }
    return finalCharArr;
}


