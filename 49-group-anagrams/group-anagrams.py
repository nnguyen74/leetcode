from collections import defaultdict

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            groupings[tuple(count)].append(word)
        return list(groupings.values())