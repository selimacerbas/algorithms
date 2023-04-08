#include <string>

using namespace std;

bool isPalindrome(string str) {
  
  auto left {0};
  auto right {str.size() - 1};
  bool isFound {true};

  while(left <= right)
  {
      if(str[left] == str[right])
      {
          isFound = true;
          left += 1;
          right -= 1;
      } else {
          isFound = false;
          return isFound;
      }
  }

  return isFound;

}
