class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Input: strs = ["act","pots","tops","cat","stop","hat"]
        # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        results = defaultdict(list)

        for str in strs:
            count = [0] * 26

            for char in str:
                count[ord(char) - ord("a")] += 1

            results[tuple(count)].append(str)

        return list(results.values())