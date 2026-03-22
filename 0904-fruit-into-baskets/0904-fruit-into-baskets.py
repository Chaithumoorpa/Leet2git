class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0
        max_len = 0
        basket = {}

        for right in range(len(fruits)):
            # add current fruit
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            # if more than 2 types → shrink window
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            # update max length
            max_len = max(max_len, right - left + 1)

        return max_len