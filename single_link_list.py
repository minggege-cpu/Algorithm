"""
        使用python实现简单的单向链表的基本操作
        is_empty：判断是否为空
        length： 获取链表长度
        travel：便利链表
        add：从头部添加
        append：从尾部添加
        insert：指定位置添加
        remove：删除
        search:查询是否存在
"""


class Node:
    '''
    节点类
    '''
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next


class SingleLinkList(object):

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """获取链表长度"""
        """ cur 游标 用来移动遍历节点 """
        cur = self.__head
        """ 游标移动次数 即代表链表长度"""
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表 """
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next

    def add(self, item):
        """ 从头部添加 """
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """ 从尾部添加 """
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加
        pos  位置参数   从零开始
        """
        if pos > self.length()-1:
            self.append(item)
        elif pos < 0:
            print("插入位置不能为负数")
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            if pos == 0:
                self.add(item)
                return
            else:
                while count != pos-1:
                    pre = pre.next
                    count += 1
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除指定的元素"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 需要判断删除的是否为头节点
                if pre == None:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找元素"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    node= Node(100)
    sl = SingleLinkList(node)
    sl.append(200)
    sl.append(300)
    sl.add(500)
    print("链表长度：", sl.length())
    sl.insert(4, 0)
    sl.remove(500)
    print(sl.search(0))
    print("为空：", sl.is_empty())
    print("链表长度：", sl.length())
    sl.travel()