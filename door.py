
#初始化列表，表示门全部关闭
li = []
for i in range(101):
    li.append(0)

# 从1号服务员开始，到100号服务员结束
for i in range(1, len(li)):
    # 每一位服务员，对门做相反处理
    for j in range(1, 101):
        # 满足门的编号的倍数条件
        if j % i == 0:
            li[j] = not li[j]

for i in range(1, len(li)):
    # 如果门是打开的，就输出
    if li[i] == 1:
        print(i, end=" ")