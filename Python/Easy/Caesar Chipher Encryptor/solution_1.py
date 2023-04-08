def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    input_idx = 0
    lst = []

    while input_idx < len(string):

        letterInString = string[input_idx]
        #In order to make it more abstract
        nextLetter = findAndShift(letterInString, key, alphabet)
        lst.append(nextLetter)
        input_idx += 1
    
    return "".join(lst)


def findAndShift(letter, shift, alphabet) -> str:

    new_letterIdx = alphabet.find(letter) + shift
    return alphabet[new_letterIdx % 26]


    
    
