#include <algorithm>
#include <vector>

using namespace std;

int nonConstructibleChange(vector<int> coins)
{
	auto currentChangeCreated {0};

	sort(coins.begin() , coins.end());

	for(auto coin : coins)
	{
		if(coin > currentChangeCreated +1)
			return currentChangeCreated +1;
		
		currentChangeCreated += coin;
		
	}

	return currentChangeCreated +1;

}



