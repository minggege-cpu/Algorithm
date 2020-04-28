"""
        二分查找  又称折半查找
        限制：只能查找排好序的顺序表
        所以通常用于 不经常变动而查找频繁的有序队列
        取列表中间值 即取下标为中间的元素值
        将搜索的数与列表中间值进行比较
        比中间值小就与中间值左边的数再次进行二分查找
        直到找到相同的值或者直到列表的长度为1
        比中间值大则与中间值右边的数进行二分查找
        最优时间复杂度：O(1)
        最坏时间复杂度:O(logn)
"""


def binary_search(l, item):
    """
        递归写法
    """
    n = len(l)
    if n > 0:
        mid = n // 2
        if l[mid] == item:  # 刚好与中间值相等
            return True
        elif l[mid] > item: # 比中间值小 左边元素递归
            return binary_search(l[:mid], item)
        else:
            return binary_search(l[mid+1:], item)
    return False            # 找不到相同的元素或者查找的列表为空


def binary_search2(l, item):
    """
        非递归写法
    """
    n = len(l)
    first = 0               # 起始
    last = n-1              # 结尾
    while first <= last:    # 判断是否达到临界情况
        mid = (first + last)//2
        if l[mid] == item:
            return True
        elif l[mid] > item:     # 比中间值小
            last = mid - 1      # 改变尾部下标值
        else:                   # 比中间值大
            first = mid + 1     # 改变头部部下标值
    return False


if __name__ == "__main__":
    l = [15, 21, 31, 40, 80, 100]
    print(binary_search(l, 0))
    print(binary_search2(l, 0))




