# 编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。

# 输入: ["flower","flow","flight"]  输出: "fl"
# 输入: ["dog","racecar","car"]  输出: "" 解释: 输入不存在公共前缀。

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    ans = ""
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    for each in zip(*strs):
        if len(set(each)) == 1:
            ans = ans + each[0]
        else:
            return ans
    return ans


print(longestCommonPrefix(["dog","racecar","car"] ))



#get to know zip function in python
# a = [1,2,3]
# b = [4,5,6]
# c = [4,5,6,7,8]
# zipped = zip(a,b)     # 打包为元组的列表
# [(1, 4), (2, 5), (3, 6)]
# zip(a,c)              # 元素个数与最短的列表一致
# [(1, 4), (2, 5), (3, 6)]
# zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# [(1, 2, 3), (4, 5, 6)]
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

