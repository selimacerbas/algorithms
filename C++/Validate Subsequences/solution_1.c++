#include <vector>

using namespace std;

bool isValidSubsequence(vector<int> array, vector<int> sequence) {
    
    auto index1 {0};
    auto index2 {0};

    while (index1 < array.size() && index2 < sequence.size()) {

        if (array[index1] == sequence[index2])
            index2++;

        index1++;

    }

  return index2 == sequence.size();
}
