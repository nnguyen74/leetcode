from collections import defaultdict
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        predix_dict = defaultdict(list)
        for product in products:
            for i in range(len(product)):
                predix_dict[product[: i + 1]].append(product)
        result = []
        for i in range(len(searchWord)):
            suggest = predix_dict[searchWord[: i + 1]]
            if len(suggest) > 3:
                result.append(sorted(suggest)[:3])
            else:
                result.append(sorted(suggest))
        return result