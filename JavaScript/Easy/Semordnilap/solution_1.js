function semordnilap(words) 
{
    
    const wordsSet = new Set(words);
    const pairs = [];

    for(const word of words)
    {
        const reversedWord = word.split("").reverse().join("");
        if(wordsSet.has(reversedWord) && reversedWord !== word)
        {
            pairs.push([word, reversedWord]);
            wordsSet.delete(word);
            wordsSet.delete(reversedWord);
        }

    }
    return pairs;
}

exports.semordnilap = semordnilap;