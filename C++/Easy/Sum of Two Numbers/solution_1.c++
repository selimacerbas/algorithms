#include <vector>

using namespace std;

vector<int> twoNumberSum(vector<int> array , int targetSum) {

    for (int i {} ; i < array.size() - 1 ; i++) 
    {
        
        for(int j {i + 1} ; j < array.size() ; j++) 
        {
            auto first = array[i];
            auto second = array[j];

            if(first + second == targetSum)
            {
                return vector<int>{first , second};
            }
        }
    }
    return {};

}