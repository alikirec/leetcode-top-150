from typing import List


class Solution:
    def insert(
            self,
            intervals: List[List[int]],
            newInterval: List[int]
    ) -> List[List[int]]:
        # empty intervals
        if not intervals:
            return [newInterval]
        # no overlapping - merge before
        if newInterval[1] < intervals[0][0]:
            return [newInterval, *intervals]
        # no overlapping - merge after
        if newInterval[0] > intervals[-1][1]:
            return [*intervals, newInterval]

        start_idx = 0
        for i, interval in enumerate(intervals):
            if newInterval[0] <= interval[1]:
                start_idx = i
                break
        end_idx = len(intervals) - 1
        while end_idx >= start_idx and newInterval[1] < intervals[end_idx][0]:
            end_idx -= 1

        return [*intervals[:start_idx],
                [
                    min(intervals[start_idx][0], newInterval[0]),
                    max(intervals[end_idx][1], newInterval[1])
                ],
                *intervals[end_idx+1:]
                ]


if __name__ == "__main__":
    s = Solution()
    intervals = [[1, 2], [3, 5], [6, 7], [8,  10], [12, 16]]
    newInterval = [19, 23]
    print(s.insert(intervals, newInterval))
