"""
    求AOE图的关键路径
    可拓展为求工程的最快完成时间
    运用了递归的方法，通过递归求汇点的最早发生时间最后得到整个项目的最快完成时间
"""


class Pro(object):
    def __init__(self, pro_id, require_time, previous, pro_list=[]):
        self.pro_id = pro_id
        self.require_time = require_time
        self.previous = previous
        pro_list.append(self)

    def run(self):
        total = 0
        tmp = []
        if self.pro_id == 0:
            return 0
        a = len(self.previous)
        # 递归求指向当前点的点的最早发生时间 直至递归到源点时return
        for x in range(a):
            tmp.append(pro_list[self.previous[x]].run() + self.require_time[x])
        print(tmp)
        # 求最大值作为最早发生时间
        total = max(tmp)
        print(total)
        return total

# 书140例题
# pro_list = []
# pro_0 = Pro(0, [0], [0], pro_list)
# pro_1 = Pro(1, [6], [0], pro_list)
# pro_2 = Pro(2, [4], [0], pro_list)
# pro_3 = Pro(3, [5], [0], pro_list)
# pro_4 = Pro(4, [1, 1], [1, 2], pro_list)
# pro_5 = Pro(5, [2], [3], pro_list)
# pro_6 = Pro(6, [9], [4], pro_list)
# pro_7 = Pro(7, [7, 4], [4, 5], pro_list)
# pro_8 = Pro(8, [2, 4], [6, 7], pro_list)

# https://wenku.baidu.com/view/a66f1fbe6394dd88d0d233d4b14e852459fb3943.html例题
# pro_list = []
# pro_0 = Pro(0, [0], [0], pro_list)
# pro_1 = Pro(1, [3], [0], pro_list)
# pro_2 = Pro(2, [10], [0], pro_list)
# pro_3 = Pro(3, [9], [1], pro_list)
# pro_4 = Pro(4, [13, 12], [1, 2], pro_list)
# pro_5 = Pro(5, [7], [2], pro_list)
# pro_6 = Pro(6, [8], [3], pro_list)
# pro_7 = Pro(7, [4, 6, 11], [3, 4, 5], pro_list)
# pro_8 = Pro(8, [2, 5], [6, 7], pro_list)

# https://zhidao.baidu.com/question/2053594708605493587.html例题
pro_list = []
pro_0 = Pro(0, [0], [0], pro_list)
pro_1 = Pro(1, [5], [0], pro_list)
pro_2 = Pro(2, [6], [0], pro_list)
pro_3 = Pro(3, [3, 12], [1, 2], pro_list)
pro_4 = Pro(4, [3, 3], [2, 3], pro_list)
pro_5 = Pro(5, [3], [3], pro_list)
pro_6 = Pro(6, [5, 1], [3, 4], pro_list)
pro_7 = Pro(7, [4], [4], pro_list)
pro_8 = Pro(8, [5, 2], [6, 7], pro_list)
pro_9 = Pro(9, [4, 2], [5, 8], pro_list)

total_time = pro_9.run()    # 此处为总项目，也可以是单个项目
print("Total_time:", total_time)

