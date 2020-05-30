"""
    实现了自动机识别句子是否属于该自动机描述的语言
"""


# 状态转换式构造类
class Edge(object):
    def __init__(self):
        self.PriorityState = None   # 转换式的左部
        self.ch = None              # 输入符号
        self.NextState = None       # 转换状态


class DFA(object):
    def __init__(self):
        self.edgeList = []          # 状态集
        self.S = None               # 初始态
        self.Z = None               # 终态

    def generate(self):
        s = input('请输入开始符：')
        self.S = s
        z = input('请输入终止符(全部终止符组成的字符串)：')
        self.Z = z
        print("请输入正规文法 以end结束(形式如下图)：")
        print("|  S-aU |")
        print("|  end  |")
        instr = input('')
        while instr != 'end':
            subStr = instr.split('-')       # 将 - 前后分隔开
            s = subStr[0]                   # 转换式左部
            for i in range(1, len(subStr)):
                edge = Edge()
                if len(subStr[i]) == 2:         # S-aU 情况
                    edge.PriorityState = s      # 转换式左部
                    edge.ch = subStr[i][0]      # 输入符号
                    edge.NextState = subStr[i][1]   # 转换状态
                    self.edgeList.append(edge)
                elif len(subStr[i]) == 1:       # B-空
                    edge.PriorityState = s
                    edge.ch = subStr[i][0]
                    edge.NextState = self.Z[0]
                    self.edgeList.append(edge)
            instr = input('')


def judeDFA():
    instr = input("输入要判断的字符串：")
    while instr != 'end':
        temp = dfa.S[0]
        count = 0
        for i in range(len(instr)):
            if instr[i] == 'a':
                temp = judeNextState(temp, 'a')
                count += 1
            elif instr[i] == 'b':
                temp = judeNextState(temp, 'b')
                count += 1
            else:
                break
        if (count == len(instr)) and judeZ(temp):
            print("此字符串“属于”该文法！")
        else:
            print("此字符串“不属于”该文法！")
        instr = input("再次判断请输入字符串(退出程序输入end):")


def judeNextState(s, ch):       # 获取此状态的转移状态
    for i in range(len(dfa.edgeList)):
        if s == dfa.edgeList[i].PriorityState and ch == dfa.edgeList[i].ch:
            return dfa.edgeList[i].NextState
    else:
        return 0


def judeZ(ch):              # 判断最后状态是否为终态
    for i in range(len(dfa.Z)):
        if ch == dfa.Z[i]:
            return True
    return False


if __name__ == "__main__":
    dfa = DFA()
    dfa.generate()
    judeDFA()


