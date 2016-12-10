from numpy import *
import math as mt

# 首先生成一些用于测试的样本
# 指定两个高斯分布的参数，这两个高斯分布的方差相同
sigma = 8
miu_1 = 200
miu_2 = 181

# 随机均匀选择两个高斯分布，用于生成样本值
N = 200
X = zeros((1, N))
for i in range(N):
    ran = random.random()
    if ran > 0.5:  # 使用的是numpy模块中的random
        X[0, i] = (ran-0.5) * sigma + miu_1
    else:
        X[0, i] = ran * sigma + miu_2

# 上述步骤已经生成样本
# 对生成的样本，使用EM算法计算其均值miu

# 取miu的初始值
k = 2
miu = random.random((1, k))
#miu[0] = [20,60]
print('初始数据:',miu)
# miu = mat([40.0, 20.0])
Expectations = zeros((N, k))

for step in range(100):  # 设置迭代次数
    # 步骤1，计算期望
    for i in range(N):
        # 计算分母
        denominator = 0
        for j in range(k):
            denominator = denominator + mt.exp(-1 / (2 * sigma ** 2) * (X[0, i] - miu[0, j]) ** 2)
        # 计算分子
        for j in range(k):
            numerator =                 mt.exp(-1 / (2 * sigma ** 2) * (X[0, i] - miu[0, j]) ** 2)
            Expectations[i, j] = numerator / denominator

    # 步骤2，求期望的最大
    oldMiu = zeros((1, k))
    for j in range(k):
        # oldMiu = miu
        oldMiu[0, j] = miu[0, j]
        numerator = 0
        denominator = 0
        for i in range(N):
            #print('numerator', numerator, Expectations[i, j], X[0, i], denominator)
            numerator = numerator + Expectations[i, j] * X[0, i]
            denominator = denominator + Expectations[i, j]
            #print('numerator', numerator,Expectations[i, j],X[0, i],denominator)
            #print('')
        miu[0, j] = numerator / denominator
        print(miu[0, j])
    # 判断是否满足要求
    epsilon = 1e-10
    if sum(abs(miu[0, 1] - oldMiu[0, 1])) < epsilon and sum(abs(miu[0, 0] - oldMiu[0, 0])) < epsilon:
        break
    print('第', step+1, '次结果:', miu)

print('最终结果:', miu)
