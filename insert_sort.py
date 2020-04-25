
def insertSort(l):
    """
        插入排序
        假设将列表分为有序的和无序的两部分，默认左边为有序的，从第二个数开始与有序列表中的元素进行比较
        如果无序队列中的元素比有序队列中的小则插入到正确的位置
        最优时间复杂度：o(n)
        最坏时间复杂度：O(n^2)
        稳定
    """
    for i in range(1, len(l)):      # 开始的时候设置第一个数为有序列表，从1开始到最后为无序列表
        cur = l[i]                  # 获取无序列表第一个元素的值
        j = i-1                     # 有序列表最后一个数的索引
        # 也可以使用for in range(j, -1, -1) 即代表从j开始循环，每次减一，直到j = -1
        while j >= 0:
            if cur < l[j]:          # 无序列表第一个元素的值小于有序列表的数的值
                l[j], l[j+1] = l[j+1], l[j]       # 交换数值
                j -= 1                            # 继续往前推进
            else:
                break               # 优化 比有序列表最大值还要大 直接退出循环，取无序列表下一个数进行循环
    return l


if __name__ == "__main__":
    l = [15, 48, 31, 20, 80, 1, 2]
    print(insertSort(l))


