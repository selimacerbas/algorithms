#include <string>
#include <unordered_map>

using namespace std;

int firstNonRepeatingCharacter(string string);

int firstNonRepeatingCharacter(string string)
{
    unordered_map<char,int> frequency;

    for(auto character : string)
    {
        frequency[character] = frequency[character] + 1;
    }

    for(auto i {0} ; i < string.size() ; i++)
    {
        char character = string[i];
        if(frequency[character] == 1)
            return i;
    }

    return -1;
}