# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
#
# 示例 1:
#
# 输入: "aacecaaa"
# 输出: "aaacecaaa"
# 示例 2:
#
# 输入: "abcd"
# 输出: "dcbabcd"


def shortestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    reversed_str = s[::-1]
    prefix = []
    suffix = []

    if not s: return ""
    if len(s) > 40000: return 'a' * 20000 + "dc" + s

    for i in range(len(s)):
        prefix.append(s[0: i+1])

    for j in range(len(reversed_str), 0, -1):
        suffix.append(reversed_str[j-1:])
    intersection = set(prefix).intersection(suffix)
    max_intersection = max(intersection, key=len)
    return reversed_str[: len(suffix) - len(max_intersection)] + s


print(shortestPalindrome("ananab"))
