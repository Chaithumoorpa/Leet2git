class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        rev_sentence=""
        word=""
        for i in range(-1, -len(s)-1, -1):
            
            if s[i] != " ":
                word = s[i] + word
            else:
                if word != "":
                    rev_sentence += word + " "
                    word=""

        if word != "":
            rev_sentence += word

        return rev_sentence.strip()
        