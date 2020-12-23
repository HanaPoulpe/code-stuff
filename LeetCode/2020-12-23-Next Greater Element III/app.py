class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Convert number into a list of digit
        digits: list = []
        digit_count: int = 0
        ret:  int = n

        while ret > 0:
            digit_count += 1
            digits.append(ret % 10)
            ret = int(ret / 10)

        max_digit: int = digits[0]
        max_index: int = 0
        for i in range(1, digit_count):
            if i == digit_count:
                continue
            # Check if current digit is smaller that the max digit found
            i_val = digits[i]
            if i_val < max_digit:
                # Look for lower digit bigger than current digit with the lower index
                min_digit: int = max_digit
                min_index: int = -1
                for j in range(i, -1, -1):
                    j_val: int = digits[j]

                    if i_val < j_val <= min_digit:
                        min_digit, min_index = j_val, j

                # If a bigger digit is present
                if min_index != -1:
                    digits[i] = min_digit
                    digits[min_index] = i_val
                    tail: list = digits[:i]
                    tail.sort(reverse=True)
                    tail.extend(digits[i:])

                    ret = 0
                    for d in tail[::-1]:
                        ret = ret * 10 + d

                    return ret if ret < 2**31 else -1

            elif max_digit < i_val:
                # If a new maximum digit have been found
                max_digit, max_index = i_val, i

        return -1