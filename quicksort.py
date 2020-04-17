def quicksort(data):
    '''
    0.先判断列表的长度，如果长度为1 直接返回原列表
    1.先取出一个基准数  可以随意选择列表里的一个数
    2.定义两个列表，用于分别存储小于基准数和大于基准数:mid
    3.将基准数移出原列表
    4.循环列表  小于mid加入left列表   大于mid加入right列表
    5.递归执行left列表和right列表
    6.最后left+[mid]+right
    '''
    if len(data) >= 2:
        mid = data[len(data)//2]   # 在列表中取一个值作为基准，可以选择第一个也可以选择任意一个
        left, right = [], []       # 定义两个列表 分别存储小于基准的数和大于基准的数
        data.remove(mid)           # 移出基准
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quicksort(left) + [mid] + quicksort(right)   # 递归
    else:
        return data


l = [15, 48, 31, 20, 80, 1]
print(quicksort(l))




