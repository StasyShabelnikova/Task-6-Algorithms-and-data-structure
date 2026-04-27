def longest_palindrome(s):
    if not s:
        return ""

    left_ans = 0
    right_ans = 0

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1

    for i in range(len(s)):
        left1, right1 = expand(i, i)

        if right1 - left1 > right_ans - left_ans:
            left_ans = left1
            right_ans = right1

        left2, right2 = expand(i, i + 1)

        if right2 - left2 > right_ans - left_ans:
            left_ans = left2
            right_ans = right2

    return s[left_ans:right_ans + 1]