class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        # Range of possible capacities
        low = max(weights)
        high = sum(weights)
        ans = high
        
        while low <= high:
            mid = low + (high - low) // 2
            
            # Helper logic to check if 'mid' capacity works
            current_day_weight = 0
            days_needed = 1 # Start with the first day
            
            for w in weights:
                if current_day_weight + w > mid:
                    # Ship is full! Start a new day.
                    days_needed += 1
                    current_day_weight = w
                else:
                    current_day_weight += w
            
            if days_needed <= days:
                # This capacity is enough, but can we go lower?
                ans = mid
                high = mid - 1
            else:
                # Capacity is too small, need a bigger ship
                low = mid + 1
                
        return ans