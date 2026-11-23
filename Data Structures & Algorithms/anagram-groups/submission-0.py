class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        h1 = dict()
        
        for word in strs:
            letters = sorted(word)
            sort = "".join(letters)

            if sort in h1:
                h1[sort] += [word]
            else:
                h1[sort] = []
                h1[sort] += [word]
        
        return list(h1.values())
