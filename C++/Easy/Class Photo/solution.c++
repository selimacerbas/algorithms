#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool classPhotos(vector<int> redShirtHeights, vector<int> blueShirtHeights);

bool classPhotos(vector<int> redShirtHeights , vector<int> blueShirtHeights)
{   
    sort(redShirtHeights.begin() , redShirtHeights.end());
    sort(blueShirtHeights.begin() , blueShirtHeights.end());

    string firstLineColor = (redShirtHeights[0] > blueShirtHeights[0]) ? "RED" : "BLUE";

    if(firstLineColor == "RED")
    {
        for(int i {0} ; i < redShirtHeights.size() ; i++)
        {
            auto redOfHeight {redShirtHeights[i]};
            auto blueOfHeight {blueShirtHeights[i]};

            if(redOfHeight <= blueOfHeight)
                return false;
        }
    }

        if(firstLineColor == "BLUE")
    {
        for(int i {0} ; i < blueShirtHeights.size() ; i++)
        {
            auto redOfHeight {redShirtHeights[i]};
            auto blueOfHeight {blueShirtHeights[i]};

            if(blueOfHeight <= redOfHeight)
                return false;
        }
    }

    return true;
}