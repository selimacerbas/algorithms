#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int tandemBicycle(vector<int> redShirtSpeeds, vector<int> blueShirtSpeeds, bool fastest);

int tandemBicycle(vector<int> redShirtSpeeds, vector<int> blueShirtSpeeds, bool fastest)
{
    int sumOfSpeeds {0};
    sort(redShirtSpeeds.begin() , redShirtSpeeds.end());

    if(fastest == true)
    {
        sort(blueShirtSpeeds.begin() , blueShirtSpeeds.end());

        for(int idx {0} ; idx < redShirtSpeeds.size() ; idx++)
        {
            auto riderRed {redShirtSpeeds[redShirtSpeeds.size() - (idx + 1)]};
            auto riderBlue {blueShirtSpeeds[idx]};

            auto maxPairedSpeed {max(riderBlue,riderRed)};

            sumOfSpeeds += maxPairedSpeed;

        }
    }

    if(fastest == false)
    {
        sort(blueShirtSpeeds.end() , blueShirtSpeeds.begin());

        for(int idx {0} ; idx < redShirtSpeeds.size() ; idx++)
        {
            auto riderRed {redShirtSpeeds[redShirtSpeeds.size() - (idx + 1)]};
            auto riderBlue {blueShirtSpeeds[idx]};

            auto maxPairedSpeed {max(riderBlue,riderRed)};

            sumOfSpeeds += maxPairedSpeed;

        }
    }

    return sumOfSpeeds;

}