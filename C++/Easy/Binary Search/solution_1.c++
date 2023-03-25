#include <vector>
#include <cmath>

using namespace std;

//Recursive Solution, It  can be also solved using while loop.
int binarySearch(vector<int> array , int target);
int binarySearchHelper(vector<int> array, int target, int leftPtr, int rightPtr);

int binarySearch(vector<int> array , int target)
{
    return binarySearchHelper(array, target, 0, array.size() -1);

}

int binarySearchHelper(vector<int> array, int target, int leftPtr, int rightPtr)
{
    if (leftPtr > rightPtr)
        return -1;

    auto midPtr {floor((leftPtr + rightPtr) / 2)};
    auto midElement {array[midPtr]};

    if(target == midElement)
        return midPtr;
    else if(target < midElement)
    {
        rightPtr = midPtr - 1;
        return binarySearchHelper(array, target, leftPtr, rightPtr);
    }else
    {
        leftPtr = midPtr + 1;
        return binarySearchHelper(array, target, leftPtr, rightPtr);   
    }

}
