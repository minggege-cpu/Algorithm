
def merge_sort(l):
    """
        归并排序
        采用分治法  分而治之
        先递归分解列表  在列表合并
        递归求出 left和 right两个有序列表，然后合并两个列表，基本方法是
        比较两个列表最前面的数值大小，如果左边的列表的第一个值
        比右边第一个列表的值小，则取左边第一个的值加入 result，同时相应的下标加一
        右边小则将右边的元素值加入 result，循环比较直至一方列表索引越界
        最优时间复杂度：O(nlogn)
        最坏时间复杂度：O(nlogn)
        稳定
    """
    n = len(l)
    if n <= 1:
        return l    # 递归退出条件
    mid = n // 2
    l_left = merge_sort(l[:mid])        # 递归取左有序列表
    l_right = merge_sort(l[mid:])       # 递归取右有序列表
    left_pointer, right_point = 0, 0    # 设置下标起点
    result = []                         # 用于存放数据的新列表
    # 循环退出条件 下标越界
    while left_pointer < len(l_left) and right_point < len(l_right):
        if l_left[left_pointer] < l_right[right_point]:
            result.append(l_left[left_pointer])     # 数据插入新列表
            left_pointer += 1                       # 下标加一
        else:
            result.append(l_right[right_point])
            right_point += 1
    result += l_left[left_pointer:]         # 退出循环时还有一个有序列表剩余一个数的情况
    result += l_right[right_point:]
    return result                           # return新列表


if __name__ == "__main__":
    l = [15, 48, 31, 20, 80, 1]
    l2 = merge_sort(l)
    print(l)
    print(l2)



