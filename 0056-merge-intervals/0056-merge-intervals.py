class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # Sort by the start time of each interval
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        for current in intervals[1:]:
            # If current interval does not overlap with the last merged one
            if merged[-1][1] < current[0]:
                merged.append(current)
            else:
                # There is an overlap, merge by updating the end time
                merged[-1][1] = max(merged[-1][1], current[1])
                
        return merged
            