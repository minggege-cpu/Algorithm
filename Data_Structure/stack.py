"""
    栈的实现
    利用python顺序表list储存栈的元素
    完成以下基本操作
    push: 压栈 添加元素到栈顶
    pop: 出栈 弹出栈顶元素
    peek: 返回栈顶元素
    is_empty: 判断是否为空
    size: 返回栈的大小
"""


class Stack(object):
    """栈的实现"""

    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加到栈顶"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        if self.is_empty():
            return
        self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.is_empty():
            return None
        else:
            return self.__list[-1]

    def is_empty(self):
        """判断是否为空"""
        return self.__list == []

    def size(self):
        """返回栈的size"""
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    s.push(12)
    print(s.is_empty())
    # s.pop()
    s.push(2)
    print(s.peek())
    print(s.size())



