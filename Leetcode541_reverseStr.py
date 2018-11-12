# 反转字符串 II
#
# 给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
#
# 输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"


def reverseStr(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    if len(s) < k:
        return s[::-1]
    elif k <= len(s) < 2 * k:
        return s[0:k][::-1] + s[k:]
    else:
        return s[0:k][::-1] + s[k: 2*k] + reverseStr(s[2* k :], k)





print(reverseStr(s = "abcdefg", k = 2)
)
