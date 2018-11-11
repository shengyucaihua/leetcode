# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1:
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"


def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    n1 = 0
    n2 = 0
    dic = {'0': 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    if num1 == '0' or num2 == '0':
        return '0'

    for i in num1:
        val = dic[i]
        n1 = 10 * n1 + val

    for i in num2:
        val = dic[i]
        n2 = 10 * n2 + val

    return str(n1 * n2)


