from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        key = None
        for element in strs:
            key = "".join(sorted(element))
            if key in table:
                table[key].append(element)
            else:
                table[key] = [element]

        return list(table.values())


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
