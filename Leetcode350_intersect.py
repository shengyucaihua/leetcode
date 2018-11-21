# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1:
#
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
# 示例 2:
#
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]

import collections

def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    res = []
    counter_num1 = collections.Counter(nums1)
    counter_num2 = collections.Counter(nums2)

    for digit, count in counter_num1.items():
        if digit in counter_num2:
            if counter_num2[digit] <= count:
                for i in range(counter_num2[digit]):
                    res.append(digit)
            else:
                for i in range(count):
                    res.append(digit)
    return res

print(intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))





