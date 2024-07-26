from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        reverse_list(nums, 0, len(nums) - 1)
        reverse_list(nums, 0, k - 1)
        reverse_list(nums, k, len(nums) - 1)


def reverse_list(nums: List[int], s: int, e: int):
    while s < e:
        nums[s], nums[e] = nums[e], nums[s]
        s += 1
        e -= 1
