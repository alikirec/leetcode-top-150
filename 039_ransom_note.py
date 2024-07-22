class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        letters_count = [0] * 26
        for m in magazine:
            letters_count[ord(m) - 97] += 1

        for r in ransomNote:
            h = ord(r) - 97
            if not letters_count[h]:
                return False

            letters_count[h] -= 1

        return True
