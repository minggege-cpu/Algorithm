
def select_sort(l):
    '''
        选择排序
        遍历列表，每次找到还未排序的最小的值放到列表的前面
        时间复杂度：T(n)=O(n^2)
        稳定性:不稳定
    '''
    # 总共该选择排序n-1次
    for i in range(len(l)-1):
        # 假设了l[i]为最小值
        min = i
        # 将l[min]和它之后的每个元素比较
        for j in range(i+1, len(l)):
            if l[min] > l[j]:
                # 如果有比l[min]还要小的则将j赋值给min
                min = j
        # 交换l[i]和l[min]的值
        l[i], l[min] = l[min], l[i]
    return l


l = [25, 19, 89, 56, 43]
print(select_sort(l))



