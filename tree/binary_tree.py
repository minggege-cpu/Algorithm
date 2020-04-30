
class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem       # 值
        self.lchild = None      # 左子树
        self.rchild = None      # 右子树


class Tree(object):
    """
        二叉树
        插入
        广度遍历：按层遍历
        先序遍历：根        左子树     右子树
        中序遍历：左子树    根         右子树
        后序遍历：左子树    右子树     根
    """
    def __init__(self):
        self.root = None        # 根节点

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:                    # 代表树的节点
            cur_node = queue.pop(0)     # 弹出第一个节点
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):       # 广度遍历 也称层次遍历
        if self.root is None:       # 为空直接return
            return
        queue = [self.root]         # 从根节点开始循环
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end="")
            if cur_node.lchild is not None:     # 左子树不为空，将左子树加入循环列表
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:     # 右子树不为空，将右子树加入循环列表
                queue.append(cur_node.rchild)

    def preorder(self, node):                   # 先序遍历 给定根节点
        if node is None:
            return
        print(node.elem, end="")                # 先打印根
        self.preorder(node.lchild)              # 递归打印左子树
        self.preorder(node.rchild)              # 递归打印右子树

    def inorder(self, node):                   # 中序遍历 给定根节点
        if node is None:
            return
        self.inorder(node.lchild)              # 递归打印左子树
        print(node.elem, end="")               # 打印根
        self.inorder(node.rchild)              # 递归打印右子树

    def postorder(self, node):                   # 后序遍历 给定根节点
        if node is None:
            return
        self.postorder(node.lchild)              # 递归打印左子树
        self.postorder(node.rchild)              # 递归打印右子树
        print(node.elem, end="")                 # 打印根


if __name__ == "__main__":
    t = Tree()
    for i in range(10):
        t.add(i)
    t.breadth_travel()
    print("")
    t.preorder(t.root)
    print("")
    t.inorder(t.root)
    print("")
    t.postorder(t.root)



