# # import cvxpy as cp
# #
# # x = cp.Variable()
# # y = cp.Variable()
# #
# # constraints = [-3*x + y <= 6, x + 2*y <= 4]
# #
# # objective = cp.Maximize(-x + 4*y)
# #
# # prob = cp.Problem(objective, constraints)
# #
# # prob.solve(solver=cp.ECOS)
# #
# # print("Optimal value:", prob.value)
# # print("x:", x.value)
# # print("y:", y.value)

# import numpy as np
# import matplotlib.pyplot as plt

# # 定义约束条件
# def constraint1(x):
#     return 6 + 3*x

# def constraint2(x):
#     return (4 - x) / 2

# # 定义 x 的取值范围
# x_values = np.linspace(0, 4, 400)

# # 绘制约束条件的直线
# plt.plot(x_values, constraint1(x_values), label='-3x + y <= 6')
# plt.plot(x_values, constraint2(x_values), label='x + 2y <= 4')

# # 标记可行域的边界
# x = np.linspace(0, 4, 100)
# y1 = constraint1(x)
# y2 = constraint2(x)
# y_min = np.maximum(np.minimum(y1, y2), 0)
# plt.fill_between(x, 0, y_min, color='gray', alpha=0.3)

# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Feasible Region')
# plt.grid(True)
# plt.legend()
# plt.show()
from scipy.optimize import linprog

# 定义目标函数的系数
c = [-3, -5]  # 因为linprog函数用的是最小化，所以要取负号

# 定义不等式约束的系数矩阵和右侧常数
A = [[2, 3], [3, 2]]  # 不等式左侧的系数矩阵
b = [12, 10]  # 不等式右侧的常数

# 定义变量的取值范围
x_bounds = (0, None)  # x的取值范围为非负实数
y_bounds = (0, None)  # y的取值范围为非负实数

# 调用linprog函数求解线性规划问题
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# 输出结果
print('最大化目标函数值:', -res.fun)  # 因为linprog用的是最小化，所以要取负号
print('最优解:', res.x)

D1 = 1
D4 = 1
x_real = 1
x_optimal = 1
y_real = 1
y_optimal = 1
z_real = 1
z_optimal = 1
w_real = 1
w_optimal = 1
alpha = 0.2
beta = 0.15
x_diff = x_real - x_optimal 
y_diff = y_real - y_optimal
z_diff = z_real - z_optimal
w_diff = w_real - w_optimal

#to min this
abs(D1 + x_diff) + abs(-(1 - alpha)*D1 + y_diff) + \
abs(-alpha*(1 - beta)*D1 + z_diff) + abs(-alpha*beta*D1 + D4 + w_diff)

#s.t.
D1_min <= D1 + x_real <= D1_max
D4_min <= -alpha*beta*D1 + D4 + w_real <= D4_max