#include <vector>
using namespace std;

vector<int> selectionSort(vector<int> array)
{
  for(int i {0}; i < array.size(); i++)
  {
     auto k {i};
     for(int j {i + 1}; j < array.size(); j++)
     {
         if(array[k] > array[j])
            k = j;
     }
     swap(array[k], array[i]);
  }
  return array;
}
