#include <vector>
#include <cmath>

using namespace std;


vector<int> sortedSquaredArray(vector<int> array) {
    
   vector<int> lst(array.size(), 0);

   auto left_ptr {0};
   auto right_ptr {array.size() - 1};

   for (int i = array.size() - 1 ; i >= 0 ; i--)
   {
       auto left_val {array[left_ptr]};
       auto right_val {array[right_ptr]};

       if (abs(left_val) > abs(right_val))
       {
           lst[i] = left_val * left_val;
           left_ptr++;
       } else {
           lst[i] = right_val * right_val;
           right_ptr--;

       }
   }

   return lst;

}

