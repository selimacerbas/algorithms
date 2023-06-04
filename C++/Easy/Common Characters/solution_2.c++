#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

string getSmallest(const vector<string> &strings);
void removeLetter(const string str , unordered_set<char> &potential);
vector<string> commonCharacters(vector<string> strings);

vector<string> commonCharacters(vector<string> strings)
{
    string smallest = getSmallest(strings);
    unordered_set<char> potential;
    
    for(int i{0}; i < smallest.length() ; i++)
    {
        potential.insert(smallest[i]);
    }

    for(auto const &string : strings)
    {
        removeLetter(string, potential);
    }
    vector<string> output;
    for(auto chr : potential)
    {
        output.push_back(string(1,chr));
    }

    return output;
}

string getSmallest(const vector<string> &strings)
{
    string smallest {strings[0]};
    for(auto const &string : strings)
    {
        if(string.length() < smallest.length())
        {
            smallest = string;
        }
    }
    return smallest;
}

void removeLetter(const string str, unordered_set<char> &potential)
{
    unordered_set<char> unique;
    for(int i{0} ; i < str.length() ; i++)
    {
        unique.insert(str[i]);
    }
    
    unordered_set<char> removeThis;
    for(auto letter : potential)
    {
        if(!unique.count(letter))
            removeThis.insert(letter);
    }
    for(auto letter : removeThis)
    {
        potential.erase(letter);
    }
}
