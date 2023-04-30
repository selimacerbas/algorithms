#include <string>

using namespace std;

int firstNonRepeatingCharacter(string string);

int firstNonRepeatingCharacter(string string)
{

    for(int first {0} ; first < string.size() ; first++)
    {
        auto found {false};

        for(int second {0} ; second < string.size() ; second++)
        {
            if(first != second && string[first] == string[second])
            {
                found = true;

            }
        }

        if(found)
            return first;
    }
    return -1;
}