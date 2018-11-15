# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba"也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"






def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if len(set(s)) == 1: return s
    dp = [[0] * len(s) for _ in range(len(s))]
    start, end, max_length = 0, 0, 0
    for i in range(len(s)):
        for j in range(i):
            dp[j][i] = (s[i] == s[j]) and (i - j < 2  or dp[j+1][i-1])
            if dp[j][i] and i - j  + 1> max_length:
                max_length = i- j + 1
                start = j
                end = i
        dp[i][i] =1

    return s[start: end + 1]








print(longestPalindrome("babad"))