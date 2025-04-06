from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_set_list = []
        result = []
        for word in strs:
            sorted_word = sorted(list(word))
            match = False
            for i, check_sorted_word in enumerate(word_set_list):
                if sorted_word == check_sorted_word:
                    match = True
                    result[i].append(word)
                    break
            if not match:
                word_set_list.append(sorted_word)
                result.append([word])
        return result
    
    #optimal: prime multiplication (assign prime for each letter of the word)
        