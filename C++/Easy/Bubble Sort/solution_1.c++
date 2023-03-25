#include <vector>

using namespace std;

vector<int> bubbleSort(vector<int> array) {
  
  auto sorted {false};
  auto counter {0};

  while(!sorted)
  {
    sorted = true;

    for(int i {0} ; i < array.size() - 1 - counter ; ++i)
    {
        if(array[i] > array[i + 1])
        {
            swap(array[i] , array[i + 1]);
            sorted = false;
        }
    }
    counter++;
  }

  return array;
}