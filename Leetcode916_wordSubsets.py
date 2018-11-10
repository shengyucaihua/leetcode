# 916. 单词子集
#
# 我们给出两个单词数组 A 和 B。每个单词都是一串小写字母。
#
# 现在，如果 b 中的每个字母都出现在 a 中，包括重复出现的字母，那么称单词 b 是单词 a 的子集。 例如，“wrr” 是 “warrior” 的子集，但不是 “world” 的子集。
#
# 如果对 B 中的每一个单词 b，b 都是 a 的子集，那么我们称 A 中的单词 a 是通用的。
#
# 你可以按任意顺序以列表形式返回 A 中所有的通用单词。

# 输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
# 输出：["facebook","google","leetcode"]
#
# 输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
# 输出：["apple","google","leetcode"]
#
# 输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
# 输出：["google","leetcode"]

# 输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
# 输出：["facebook","leetcode"]
import collections

def wordSubsets(A, B):
    """
    :type A: List[str]
    :type B: List[str]
    :rtype: List[str]
    """
    B = set(B)
    res = []
    count = collections.defaultdict(int)
    for b in B:
        cb = collections.Counter(b)
        for c, v in cb.items():
            count[c] = max(count[c], v)
    res = []
    for a in A:
        ca = collections.Counter(a)
        isSuccess = True
        for c, v in count.items():
            if v > ca[c]:
                isSuccess = False
                break
        if isSuccess:
            res.append(a)
    return res


print(wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]))
