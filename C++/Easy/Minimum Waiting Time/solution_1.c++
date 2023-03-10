#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int minimumWaitingTime(vector<int> queries);


int minimumWaitingTime(vector<int> queries)
{
    unordered_map<int, int> hash_tbl;
    sort(queries.begin(), queries.end());
    auto waitingTime {0};
    auto totalWaitingTime {0};

    for(int idx = 0 ; idx < queries.size() - 1 ; idx ++)
     {
         auto first {queries[idx]};
         auto second {queries[idx + 1]};
         waitingTime += first;

         hash_tbl[waitingTime] = second;

     }

     for(auto keys : hash_tbl)
     {
         totalWaitingTime += keys.first;

     }

     return totalWaitingTime;

}