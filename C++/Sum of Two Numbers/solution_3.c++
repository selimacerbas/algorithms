#include <vector>
#include <algorithm>

using namespace std;

vector<int> twoNumberSum(vector<int> array, int targetSum)
{
    sort(array.begin(), array.end());

    auto left {0};
    auto right = array.size() - 1;

    while(left < right)
    {
        auto currentSum = array[left] + array[right];

        if(currentSum == targetSum)
            return{array[left], array[right]};
        else if(currentSum < targetSum)
            left++;
        else if(currentSum > targetSum)
            right--;
    }
    return {};
}

