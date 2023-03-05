#include <vector>

using namespace std;


vector<int> sortedSquaredArray(vector<int> array) {
    
    vector<int> lst(array.size() , 0);

    for (int i {} ; i < array.size()  ; i++)
    {
        auto val = array[i];
        lst[i] = val * val;
    }

    sort(lst.begin() , lst.end());

    return lst;
}

