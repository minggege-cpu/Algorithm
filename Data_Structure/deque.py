"""
    双端队列
    头部尾部均可插入和删除
    add_front：头部插入
    add_rear：尾部插入
    pop_front：头部取出
    pop_rear：尾部取出
    is_empty：判断是否为空
    size：返回队列长度
"""


class Deque(object):

    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """头部插入"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """尾部插入"""
        self.__list.append(item)

    def pop_front(self):
        """头部取出"""
        if self.is_empty():
            return
        self.__list.pop(0)

    def pop_rear(self):
        """尾部取出"""
        if self.is_empty():
            return
        self.__list.pop(0)

    def is_empty(self):
        """判断是否为空"""
        return self.__list == []

    def size(self):
        """返回队列长度"""
        return len(self.__list)


if __name__ == "__main__":
    d = Deque()
    print(d.is_empty())
    d.add_front(1)
    d.add_front(2)
    d.add_rear(2)
    d.pop_front()
    d.pop_rear()
    print(d.is_empty())
    print(d.size())


