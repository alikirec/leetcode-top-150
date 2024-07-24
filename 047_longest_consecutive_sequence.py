from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starting_points = {}
        ending_points = {}
        m = -1
        for n in nums:
            total = 1
            if n in ending_points:
                total += ending_points[n]
            if n+1 in starting_points:
                total += starting_points[n+1]

            starting_points[n] = total
            ending_points[n+1] = total

            if n + 1 in starting_points and total > starting_points[n+1]:
                starting_points[n+1] = total
                ending_points[n+2] = total
            if n in ending_points and total > ending_points[n]:
                ending_points[n] = total
                starting_points[n-1] = total

            m = max(m, total)

        return m


if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    #                          [1, 4, 8, 3, 6, 9, 5, 7, 1, 2] 
