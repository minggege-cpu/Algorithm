"""
        使用python实现简单的队列
        选择python内置顺序表list存储队列元素
        需要实现的方法:
        enqueue:从尾部添加
        dequeue:头部取出
        is_empty:判断是否为空
        size：得到队列长度
    """


class Queue(object):

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """尾部插入"""
        self.__list.append(item)

    def dequeue(self):
        """头部取出"""
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
    q = Queue()
    print(q.is_empty())
    q.enqueue(2)
    q.dequeue()
    print(q.is_empty())
    print(q.size())


