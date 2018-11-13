# 给定两个由小写字母构成的字符串
# A
# 和
# B ，只要我们可以通过交换
# A
# 中的两个字母得到与
# B
# 相等的结果，就返回
# true ；否则返回
# false 。
#
#
#
# 示例
# 1：
#
# 输入： A = "ab", B = "ba"
# 输出： true
# 示例
# 2：
#
# 输入： A = "ab", B = "ab"
# 输出： false
# 示例
# 3:
#
# 输入： A = "aa", B = "aa"
# 输出： true
# 示例
# 4：
#
# 输入： A = "aaaaaaabc", B = "aaaaaaacb"
# 输出： true
# 示例
# 5：
#
# 输入： A = "", B = "aa"
# 输出： false
import collections
def buddyStrings(A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    if len(A) != len(B):
        return False
    diff = 0
    idx = []
    for i, a in enumerate(A):
        if a != B[i]:
            diff += 1
            idx.append(i)

    counter = collections.Counter(A)
    if diff == 0:
        for char, count in counter.items():
            if counter[char] >= 2:
                return True

    if diff != 2:
        return False

    return A[idx[0]] == B[idx[1]] and A[idx[1]] == B[idx[0]]


print(buddyStrings(A = "aa", B = "aa"))









