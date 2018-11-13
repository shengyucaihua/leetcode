# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。
#
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)
#
# 注意：
#
# 你可以假设两个字符串均只含有小写字母。
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

import collections


def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """

    m_counter = collections.Counter(magazine)
    r_counter = collections.Counter(ransomNote)

    for item, count in r_counter.items():
        if item not in m_counter:
            return False
        else:
            if r_counter[item] > m_counter[item]:
                return False
    return True


print(canConstruct("aa", "ab"))