class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len: int = len(s)
        if s_len <= 1:  # don't care 0 or 1 char strings
            return s

        ret, ret_len = s[0], 1
        left: int = 0
        right: int = 1

        while ret_len < s_len - left:
            if left > 0 and right < s_len and s[left - 1] == s[right] and s[left - 1:right + 1] == s[left - 1:right + 1][::-1]:  # previous and next are the same
                if right - left + 2 > ret_len:
                    ret_len = right - left + 2
                    ret = s[left - 1:right + 1]

                left -= 1
                right += 1
            elif right < s_len and s[left] == s[right] and s[left:right + 1] == s[left:right + 1][::-1]:  # first character == character after next character
                if right - left + 1 > ret_len:  # longer palindrome to the right
                    ret_len = right - left + 1
                    ret = s[left:right + 1]

                right += 1

            elif left > 0 and s[left - 1] == s[right - 1] and s[left - 1] == s[right] and s[left - 1:right] == s[left - 1:right][::-1]:  # previous character == last character
                if right - left + 1 > ret_len:  # longer palindrome to the left
                    ret_len = right - left + 1
                    ret = s[left - 1:right]

                left -= 1
            else:
                left += 1
                right += 1

            if left < 0:
                left = 0

        return ret

