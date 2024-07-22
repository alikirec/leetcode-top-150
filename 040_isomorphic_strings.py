class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        table = [-1] * 128
        reverse_table = table[:]
        for i in range(len(s)):
            k, h = ord(s[i]), ord(t[i])
            if table[k] == -1 and reverse_table[h] == -1:
                table[k] = h
                reverse_table[h] = k
            elif table[k] != h or reverse_table[h] != k:
                return False

        return True
