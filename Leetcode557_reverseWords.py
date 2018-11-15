# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#
# 示例 1:
#
# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc"


def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]


    return " ".join(words)


print(reverseWords("Let's take LeetCode contest"))