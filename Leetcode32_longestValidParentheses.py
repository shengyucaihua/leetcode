# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
# 示例 1:
#
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 示例 2:
#
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"


def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    stack = []
    left_most = -1
    max_length = 0
    for idx in range(len(s)):
        if s[idx] == "(":
            stack.append(idx)
        else:
            if stack:
                stack.pop()
                if stack and idx - stack[-1] > max_length:
                    max_length = idx -  stack[-1]
                if not stack and idx - left_most > max_length:
                    max_length = idx - left_most

            else:
                left_most = idx

    return max_length

print(longestValidParentheses("))))((()(("))


