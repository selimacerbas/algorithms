#include <string>

using namespace std;

bool generateDocument(string characters, string document);
int countCharacterFrequency(char character, string target);

bool generateDocument(string characters, string document) {

  for(auto character : document) {

    auto documentFrequency = countCharacterFrequency(character, document);
    auto characterFrequency = countCharacterFrequency(character, characters);

    if(documentFrequency > characterFrequency)
      return false;
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