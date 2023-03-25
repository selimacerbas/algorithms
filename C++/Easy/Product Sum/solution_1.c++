#include <any>
#include <vector>

using namespace std;

// Tip: You can use el.type() == typeid(vector<any>) to check whether an item is
// a list or an integer.
// If you know an element of the array is vector<any> you can cast it using:
//     any_cast<vector<any>>(element)
// If you know an element of the array is an int you can cast it using:
//     any_cast<int>(element)
int productSum(vector<any> array, int multiplier = 1) {
  int sum {0};

  for(auto element : array)
  {
    if(element.type() == typeid(vector<any>))
       sum += productSum(any_cast<vector<any>>(element), multiplier + 1);
    else
        sum += any_cast<int>(element);
  }

  return sum * multiplier;
}
