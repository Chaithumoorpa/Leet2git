class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        last_word_len = 0

        list_of_words = list(s.split())

        return len(list_of_words[-1])


        