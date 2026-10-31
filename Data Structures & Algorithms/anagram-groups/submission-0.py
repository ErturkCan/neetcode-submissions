class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for i in strs:
            key = tuple(sorted(i))

            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(i)

        return list(anagrams.values())