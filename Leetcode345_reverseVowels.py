# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
#
# 输入: "hello"
# 输出: "holle"

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    res = []
    Vowels = []
    for i in range(len(s)):
        if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            Vowels.append(s[i])

    Vowels = Vowels[::-1]
    character = list(s)
    index = 0
    for i in character:
        if i not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            res.append(i)
        else:
            res.append(Vowels[index])
            index += 1
    return "".join(res)

print(reverseVowels("hello"))






