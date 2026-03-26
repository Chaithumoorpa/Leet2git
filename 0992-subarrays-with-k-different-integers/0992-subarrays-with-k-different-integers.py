class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums, k):
        left = 0
        count = 0
        freq = {}

        for right in range(len(nums)):
            # include current element
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # if more than k distinct → shrink
            while len(freq) > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            # count subarrays ending at right
            count += (right - left + 1)

        return count