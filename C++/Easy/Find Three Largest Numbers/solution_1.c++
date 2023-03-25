#include <vector>
#include <climits>

using namespace std;

void updateLargest(vector<int> &array , int element);
void shiftAndUpdate(vector<int> &array , int element, int idx);
vector<int> findThreeLargestNumbers(vector<int> array);


vector<int> findThreeLargestNumbers(vector<int> array)
{
    vector<int> threeLargest{INT_MIN,INT_MIN,INT_MIN};

    for(auto element : array)
    {
        updateLargest(threeLargest, element);
    }

    return threeLargest;
}

void updateLargest(vector<int> &array , int element)
{
    if (element > array[2]) {
		shiftAndUpdate(array, element, 2);
	} else if (element > array[1]) {
		shiftAndUpdate(array, element, 1);
	} else if (element > array[0]) {
		shiftAndUpdate(array, element, 0);
	}
}


void shiftAndUpdate(vector<int> &array , int element, int idx)
{

	for (int i = 0; i < idx+1; i++) {

		if (i == idx) {
			array[i] = element;
		} else {
			array[i] = array[i+1];
		}
	}
}