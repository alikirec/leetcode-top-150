from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        min_n_citations = [0] * 1001
        for n in citations:
            min_n_citations[n] += 1

        sum = 0
        for i in range(1000, -1, -1):
            sum += min_n_citations[i]
            if sum >= i:
                return i


if __name__ == "__main__":
    s = Solution()
    print(s.hIndex([5, 5, 5]))
