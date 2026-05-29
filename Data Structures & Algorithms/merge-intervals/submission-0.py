class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        merged = []
        current = intervals[0]
        for interval in intervals[1:]:
            if current[1] >= interval[0]:
                current[1] = max(current[1],interval[1])
            else:
                merged.append(current)
                current = interval
        merged.append(current)
        return merged
