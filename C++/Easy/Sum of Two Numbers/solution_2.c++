#include <vector>
#include <unordered_set>

using namespace std;

vector<int> twoNumberSum(vector<int> array, int targetSum)
{
    unordered_set<int> hashed_numbers;

    for(auto element : array)
    {
        auto match = targetSum - element;

        if (hashed_numbers.find(match) != hashed_numbers.end())
        {
            return vector<int>{match, element};
        }
        else
        {
            hashed_numbers.insert(element);
        }

    }
    return {};
}