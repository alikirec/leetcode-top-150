from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        def backtrack(n, message):
            if n == len(digits):
                if message:
                    res.append(message)
                return

            for ch in letters[digits[n]]:
                backtrack(n+1, message + ch)

        backtrack(0, "")

        return res


letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("2"))
