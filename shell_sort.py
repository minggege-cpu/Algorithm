
def shell_sort(l):
    """
        希尔排序：插入排序的改进版 又称缩小增量排序
        通过设置增量，将整个有序序列分割成若干小的子序列分别进行插入排序。
        最优时间复杂度：随着增量的选择而不同
        最坏时间复杂度：0(n^2)
        不稳定
    """
    n = len(l)
    gap = n // 2        # 设置增量
    while gap > 0:      # 增量大于零时继续进行排序
        for i in range(gap, n):     # 从增量对应的下标的元素开始进行插入排序
            j = i
            while j > 0:
                if l[j] < l[j-gap]:     # 插入排序的算法
                    l[j], l[j-gap] = l[j-gap], l[j]
                    j -= gap
                else:
                    break
        gap //= 2                   # 可以自定义增量的变化方式
    return l


if __name__ == "__main__":
    l = [15, 48, 31, 20, 80, 1]
    print(shell_sort(l))


