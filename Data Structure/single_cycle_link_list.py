"""
        使用python实现简单的 单向循环链表 的基本操作
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


class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """获取链表长度"""
        if self.is_empty():
            count = 0
        else:
            """ cur 游标 用来移动遍历节点 """
            cur = self.__head
            count = 1
            while cur.next != self.__head:
                count += 1
                cur = cur.next
        return count

    def travel(self):
        """遍历链表 """
        cur = self.__head
        if self.is_empty():
            return
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 尾节点时已不满足while条件 需要追加打印尾节点的elem
        print(cur.elem)

    def add(self, item):
        """ 从头部添加 """
        cur = self.__head
        node = Node(item)
        if cur == None:
            self.__head = node
            node.next = node
            return
        while cur.next != self.__head:
            cur = cur.next
        # 退出循环时cur指向表尾
        node.next = self.__head
        self.__head = node
        cur.next = node

    def append(self, item):
        """ 从尾部添加 """
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

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
        if self.is_empty():
            return
        else:
            cur = self.__head
            pre = None
            while cur.next != self.__head:
                if cur.elem == item:
                    # 需要判断删除的是否为头节点
                    if pre == None:
                        # 头节点
                        # 需要找到尾节点
                        rear = self.__head
                        while rear.next != self.__head:
                            rear = rear.next
                        rear.next = cur.next
                        self.__head = cur.next
                    else:
                        # 中间节点
                        pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            # 尾节点
            if cur.elem == item:
                if pre == None:
                    self.__head = None
                else:
                    pre.next = self.__head

    def search(self, item):
        """查找元素"""
        cur = self.__head
        if cur == None:
            return False
        else:
            while cur.next != self.__head:
                if cur.elem == item:
                    return True
                else:
                    cur = cur.next
            # 退出循环时cur指向表尾 判断表尾的值是否于查找的值相等
            if cur.elem == item:
                return True
            return False


if __name__ == "__main__":
    node= Node(100)
    sl = SingleCycleLinkList(node)
    # sl.add(200)
    # sl.add(400)
    print("链表长度：", sl.length())
    # sl.insert(4, 6000)
    # sl.append(0)
    sl.remove(100)
    print(sl.search(0))
    print("为空：", sl.is_empty())
    print("链表长度：", sl.length())
    sl.travel()




