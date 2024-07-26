from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        t = len(words[0])
        n_w = len(words)
        original_map = {}
        for w in words:
            if w in original_map:
                original_map[w] += 1
            else:
                original_map[w] = 1

        for k in range(t):
            curr_map = original_map.copy()
            i = j = k
            wc = 0
            while i <= len(s) - (n_w * t):
                if wc == len(words):
                    res.append(i)
                    curr_map[s[i:i+t]] += 1
                    i += t
                    wc -= 1
                elif s[j:j+t] not in original_map:
                    i = j = j + t
                    wc = 0
                    curr_map = original_map.copy()
                else:
                    while not curr_map[s[j:j+t]] and i < j:
                        curr_map[s[i:i+t]] += 1
                        i += t
                        wc -= 1
                    wc += 1
                    curr_map[s[j:j+t]] -= 1
                    j += t

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.findSubstring(
        "abababab", ["ab", "ba"]
    ))
