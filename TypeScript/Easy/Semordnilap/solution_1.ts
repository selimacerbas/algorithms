export function semordnilap(words: string[])
{
    const wordsSet = new Set(words);
    const pairs: [string,string][] = [];

    for(const word of words)
    {
        const reversedWord = word.split("").reverse().join("");
        if(wordsSet.has(reversedWord) && reversedWord !== word)
        {
            pairs.push([word,reversedWord]);
            wordsSet.delete(word);
            wordsSet.delete(reversedWord);
        }
    }
    return pairs;
}