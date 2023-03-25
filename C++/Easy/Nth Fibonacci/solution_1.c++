#include <vector>

using namespace std;

int getNthFib(int n)
{
    vector<int> fib_lst {0,1};
    auto counter {3};
    auto idx {0};

    if(n == 2)
        return 1;
    if(n == 1)
        return 0;

    while(counter <= n)
    {
        auto nextFibNumber = fib_lst[idx] + fib_lst[idx + 1];

        fib_lst.push_back(nextFibNumber);

        counter++;
        idx++;

    }

    return fib_lst.back();

}