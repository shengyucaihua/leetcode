# path = "/a/./b/../../c/", =>"/c"
#
# 整个过程：
#
# l  “/”根目录
#
# l  “a”进入子目录a，目前处于“/a”
#
# l  “.”当前目录，不操作仍处于“/a”
#
# l  “/b”进入子目录b，目前处于“/a/b”
#
# l  “..”返回上级目录，处于“/a”
#
# l  “..”返回上级目录，处于根目录“/”
#
# l  “c”进入子目录c，目前处于“/c”








def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    stack = list()
    folder = path.split("/")
    for i in folder:
        if i == "." or not i:
            continue
        elif i == "..":
            if stack:
                stack.pop()
        else:
            stack.append(i)

    return "/" + "/".join(stack)



print(simplifyPath("/a/./b/../../c/")
)





