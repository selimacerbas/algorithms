#include <string>
#include <vector>


using namespace std;

string caesarCypherEncryptor(string str, int key);
char findAndShift(char letter, int shift, string alphabet);

string caesarCypherEncryptor(string str, int key) {
  
  auto alphabet = "abcdefghijklmnopqrstuvwxyz";
  vector<char> chars {};
  auto input_idx {0};

  while(input_idx < str.size())
  {
      auto firstLetter {str[input_idx]};
      //Abstraction
      char newLetter {findAndShift(firstLetter, key, alphabet)};
      chars.push_back(newLetter);
      input_idx++;

  }
  return string(chars.begin(),chars.end());
}

char findAndShift(char letter, int shift, string alphabet)
{
    auto newLetterCode = alphabet.find(letter) + shift;
	auto newLetter = alphabet[newLetterCode % 26];
	return newLetter;

}