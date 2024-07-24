from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        summary = []
        start_idx = end_idx = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                end_idx = i
            else:
                if end_idx == start_idx:
                    summary.append(f"{nums[start_idx]}")
                else:
                    summary.append(f"{nums[start_idx]}->{nums[end_idx]}")

                start_idx = i
                end_idx = i

        if start_idx == end_idx:
            summary.append(f"{nums[start_idx]}")
        else:
            summary.append(f"{nums[start_idx]}->{nums[end_idx]}")

        return summary
