def toGoatLatin(S):
    """
    :type S: str
    :rtype: str
    """

    words = S.split(" ")
    print(words)
    for i in range(len(words)):
        if words[i][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            words[i] = words[i] + 'ma' + 'a' * (i + 1)
        else:
            words[i] = words[i][1:] + words[i][0] + 'ma' + 'a' * (i + 1)

    return " ".join(words)

print(toGoatLatin("The quick brown fox jumped over the lazy dog"))
