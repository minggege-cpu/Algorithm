from timeit import Timer


# 五种给列表赋值的方法
def t1():
    l = []
    for i in range(10000):
        l += [i]


def t2():
    l = []
    for i in range(10000):
        l.append(i)


def t3():
    l = [i for i in range(10000)]


def t4():
    l = [range(10000)]


def t5():
    l = []
    for i in range(10000):
        l.extend([i])


# 监听程序运行1000次时间
time1 = Timer("t1()", "from __main__ import t1")
time2 = Timer("t2()", "from __main__ import t2")
time3 = Timer("t3()", "from __main__ import t3")
time4 = Timer("t4()", "from __main__ import t4")
time5 = Timer("t5()", "from __main__ import t5")
print("累加所需时间：", time1.timeit(1000))         # 0.9064521秒
print("append所需时间：", time2.timeit(1000))       # 0.7193688999999999秒
print("循环迭代器所需时间：", time3.timeit(1000))    # 0.41138169999999974秒
print("迭代器生成时间：", time4.timeit(1000))        # 0.00036559999999985493秒     需要时间最短
print("extend生成时间：", time5.timeit(1000))       # 1.2288228秒                  需要时间最多


# 测试append和insert
def t6():
    l = []
    for i in range(10000):
        l.append(i)


def t7():
    l = []
    for i in range(10000):
        l.insert(0, i)


time6 = Timer("t6()", "from __main__ import t6")
time7 = Timer("t7()", "from __main__ import t7")
print(time6.timeit(1000))       # 0.8277587000000001秒
print(time7.timeit(1000))       # 21.1961429秒
# 为何运行效率相差如此之大？
# append从尾部插入，时间复杂度为O(1)
# insert从头部插入，时间复杂度为O(n)
# 虽然说两者的效率相差悬殊，但是在特定的场合选择不同的方法才是正确之道