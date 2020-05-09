

def bubble_sort(nums):
    '''
    冒泡排序
    比较相邻的元素，如果前面的比后面的大，就交换他们
    时间复杂度：T(n)=O(n^2)
    '''
    for i in range(len(nums)-1):      #冒泡排序一共要运行的次数
        count = 0
        for j in range(len(nums)-i-1):   #j是下标 每循环一次还未排好序的最大值都会找到正确的位置
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                count += 1
        if count == 0:  # 优化 循环了N次后发现没有变化即退出循环
            break
    return nums


print(bubble_sort([91, 52, 63, 4]))



