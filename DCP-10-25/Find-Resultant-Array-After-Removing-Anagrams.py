class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        word = {}
        last = {}
        res = []

        for i, w in enumerate(words):
            new_word = Counter(w)
            if new_word != last:
                word[i] = new_word
            last = new_word

        for key in word.keys():
            res.append(words[key])

        return res


        
