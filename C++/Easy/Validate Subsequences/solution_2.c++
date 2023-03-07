#include <vector>

using namespace std;

bool isValidSubsequence(vector<int> array, vector<int> sequence) {
    
    auto index {0};

    for (auto val : array){

        if (index == sequence.size())
            break;

        if (val == sequence[index])
            index++;

    }

  return index == sequence.size();
}
