class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        # Each of the first n-1 trains takes at least 1 hour. 
        # If hour is less than or equal to n-1, it's impossible.
        if hour <= len(dist) - 1:
            return -1
        
        low = 1
        high = 10**7
        ans = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            # Calculate time for this speed
            time_needed = 0.0
            # Trains 0 to n-2 (waiting required)
            for i in range(len(dist) - 1):
                # Manual ceil to avoid some math library overhead:
                # (dist[i] + mid - 1) // mid
                time_needed += math.ceil(dist[i] / float(mid))
            
            # Last train (no waiting)
            time_needed += dist[-1] / float(mid)
            
            if time_needed <= hour:
                ans = mid
                high = mid - 1 # Try to go slower
            else:
                low = mid + 1 # Must go faster
                
        return ans