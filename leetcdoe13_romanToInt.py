#13. 罗马数字转整数
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# 输入: "LVIII"
# 输出: 58
# 解释: L = 50, V= 5, III = 3.

# 输入: "IX"
# 输出: 9

# 输入: "MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dic = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I":1}
    numList = []
    for i in range(len(s) - 1):
        num = 0
        if dic[s[i]] < dic[s[i+1]]:
            num -= dic[s[i]]
            numList.append(num)
        else:
            numList.append(dic[s[i]])
        print(numList)
    return sum(numList) + int(dic[s[-1]])

print(romanToInt(s = "LVIII"))