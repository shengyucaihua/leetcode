# # # 给定两个二进制字符串，返回他们的和（用二进制表示）。
# # #
# # # 输入为非空字符串且只包含数字 1 和 0。
# # #
# #
# #
# # 输入: a = "11", b = "1"
# # 输出: "100"
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"


def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    ans = int(a, 2) + int(b, 2)
    return bin(ans)[2:]

