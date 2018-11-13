# 767. 重构字符串
#
# 给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
#
# 若可行，输出任意可行的结果。若不可行，返回空字符串。
#
# 示例 1:
#
# 输入: S = "aab"
# 输出: "aba"
# 示例 2:
#
# 输入: S = "aaab"
# 输出: ""

import collections

def reorganizeString(S):
    """
    :type S: str
    :rtype: str
    """
    counter = collections.Counter(S)
    ans = "#"
    while counter:
        stop = True
        for item, times in counter.most_common():
            if ans[-1] != item:
                ans += item
                counter[item] -= 1
                if not counter[item]:
                    del counter[item]
                stop = False
                break
        if stop: break
    return ans[1:] if len(ans) == len(S) + 1 else ""






print(reorganizeString("aaab"))
