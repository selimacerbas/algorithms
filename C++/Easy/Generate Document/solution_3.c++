#include <unordered_map>
#include <string>
using namespace std;

bool generateDocument(string characters, string document);
int countCharacterFrequency(char character, string target);

bool generateDocument(string characters, string document) {

  unordered_map<char, int> characterCounts;

  for(auto character : characters){
    if(characterCounts.find(character) == characterCounts.end())
      characterCounts[character] = 0;

    characterCounts[character]++;
  }
    for(auto character : document){
    if(characterCounts.find(character) == characterCounts.end() ||
      characterCounts[character] == 0)
      return false;
      

    characterCounts[character]--;
  }
  return true;
}