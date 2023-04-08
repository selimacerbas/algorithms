#include <string>
#include <vector>

using namespace std;

string runLengthEncoding(string str);
void addChar(int num, char character, vector<char>* array);

string runLengthEncoding(string str)
{
    auto left {0};
    auto right {0};
    auto counter {0};
    vector<char> charArray;

    while(right < str.size())
    {
        auto mainChar {str[left]};
        auto walkingChar {str[right]};

        if((mainChar == walkingChar) && counter != 9)
        {
            right++;
            counter++;

            if(right == str.size())
                addChar(counter, mainChar, &charArray);
        } else {   
            addChar(counter, mainChar, &charArray);
            left = right;
            counter = 0;
        }
    }
    string lastOne(charArray.begin(), charArray.end());
    return lastOne;
}

void addChar(int num, char character, vector<char>* array)
{
    array->push_back(to_string(num)[0]);
    array->push_back(character);

}