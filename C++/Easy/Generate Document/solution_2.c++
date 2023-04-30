#include <string>
#include <unordered_set>

using namespace std;

bool generateDocument(string characters, string document);
int countCharacterFrequency(char character, string target);

bool generateDocument(string characters, string document) {

  unordered_set<char> alreadyCounted;

  for(auto character : document) {

    if(alreadyCounted.find(character) != alreadyCounted.end())
      continue;

    auto documentFrequency = countCharacterFrequency(character, document);
    auto characterFrequency = countCharacterFrequency(character, characters);

    if(documentFrequency > characterFrequency)
      return false;

    alreadyCounted.insert(character);
  }
  
  return true;
}

int countCharacterFrequency(char character, string target) {

  int frequency = 0;
  for(auto c : target){
    if(c == character)
      frequency++;
  }
return frequency;
}