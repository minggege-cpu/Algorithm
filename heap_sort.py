

def exchange(arr, start, end):      # 将待排序列排序得到一个大堆顶
    begin = start
    child = begin * 2 + 1      # 节点的左孩子
    while child <= end:
        # 如果右孩子下标小于最后的叶节点并且右孩子的数值大于左孩子，使用右孩子与他的父节点进行比较
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[child] > arr[begin]:    # 子节点的值大于父节点
            arr[child], arr[begin] = arr[begin], arr[child]     # 交换值
            begin = child           # 把子节点作为父节点继续排序
            child = begin * 2 + 1   # 这个子节点的左孩子
        else:
            break


def heapSort(arr):
    """
    堆排序：利用堆这种数据结构而设计的一种排序算法，堆排序是一种选择排序
    堆：相当于完全二叉树
    步骤：先构造大顶堆(用于升序排序）
          将大顶堆的最后一个元素和第一个元素交换值
          剩余的元素继续构建大顶堆，并且交换
    :param arr:
    :return:
    """
    first = len(arr)//2 - 1     # 最后的有子节点的父节点
    for i in range(first, -1, -1):      # 从下至上循环父节点
        exchange(arr, i, len(arr)-1)    # 最后得到大顶堆的序列
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]     # 将最大值移至序列的最后
        # 由于顶部元素交换了值， 所以从顶部开始重新构建大顶堆序列，并且最后排好序的元素不介入重新排序
        exchange(arr, 0, i - 1)
    return arr


if __name__ == "__main__":
    l = [8, 2, 6, 5, 4, 1, 3, 7, 9]
    print(heapSort(l))