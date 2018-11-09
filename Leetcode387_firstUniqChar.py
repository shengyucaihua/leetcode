# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
#
#
# s = "leetcode"
# 返回 0.
#
# s = "loveleetcode",
# 返回 2.


def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    res = {}
    for i in s:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1            #use a dict to store how many times each character appear in the string

    for i in range(len(s)):
        if res[s[i]] == 1:
            return i

    return -1

