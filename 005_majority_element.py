from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        count = 0
        for n in nums:
            if not count:
                majority = n
                count = 1
            elif n == majority:
                count += 1
            else:
                count -= 1

        return majority
