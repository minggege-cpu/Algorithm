"""
    用python实现顺序表
    python封装的list就是一个顺序表
    需要完成的方法：
    is_empty：判断线性表是否为空
    if_full：判断线性表是否为满
    __getitem__：获取线性表中某一位置的值
    __setitem__：修改线性表中某一位置的值
    locate_item：按值查找第一个等于该值的索引
    count：返回线性表中元素的个数
    append_last：在表尾插入一个元素
    insert：在表中任意位置插入一个元素
    remove:删除表中某一位置的值
    print_list：打印线性表
    destroy:清空
"""


class SeqList(object):

    def __init__(self, size=50):  # 初始化线性表
        # 定义线性表的最大长度为50
        self.max = size
        self.num = 0
        self.data = [None]*self.max

    def is_empty(self):  # 判断线性表是否为空
        return self.num is 0

    def if_full(self):  # 判断线性表是否为满
        return self.num is self.max

    def __getitem__(self, index):  # 获取线性表中某一位置的值
        if not isinstance(index, int):
            raise TypeError
        if 0 <= index < self.max:
            return self.data[index]
        else:
            raise IndexError

    def __setitem__(self, index, value):  # 修改线性表中某一位置的值
        if not isinstance(index, int):
            raise TypeError
        if 0 <= index < self.max:
            self.data[index] = value
        else:
            raise IndexError

    def locate_item(self, value):  # 按值查找第一个等于该值的索引
        for i in range(self.num):
            if self.data[i] == value:
                return i
        return -1

    def count(self):  # 返回线性表中元素的个数
        return self.num

    def append_last(self, value):  # 在表尾插入一个元素
        if self.num > self.max:
            print("list is full")
        else:
            self.data[self.num] = value
            self.num += 1

    def insert(self, index, value):  # 在表中任意位置插入一个元素
        if self.num >= self.max:
            print("list is full")
        if not isinstance(index, int):
            raise TypeError
        if index < 0 or index > self.num:
            raise IndexError
        for i in range(self.num, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = value
        self.num += 1

    def remove(self,index):  # 删除表中某一位置的值
        if isinstance(index, int):
            raise TypeError
        if index < 0 or index >= self.num:
            raise IndexError
        for i in range(index, self.num):
            self.data[i] = self.data[i+1]
        self.num -= 1

    def print_list(self):  # 打印线性表
        for i in range(0, self.num):
            print(self.data[i])

    def destroy(self):   # 销毁线性表
        self.__init__()


if __name__ == '__main__':
    seqlist = SeqList()
    print(seqlist.is_empty())
    seqlist.append_last(18)
    print(seqlist.__getitem__(0))


