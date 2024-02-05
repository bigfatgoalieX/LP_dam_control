import pulp

#sign
#0000
sign1 = 1
sign2 = 1
sign3 = 1
sign4 = 1

# 创建线性规划问题
problem = pulp.LpProblem("Optimization Problem", pulp.LpMinimize)

# 定义LP中的变量_两个大坝的放水量
P1 = pulp.LpVariable('P1', lowBound=1, upBound=None)
P2 = pulp.LpVariable('P2', lowBound=1, upBound=None)
P3 = pulp.LpVariable('P3', lowBound=1, upBound=None)
P4 = pulp.LpVariable('P4', lowBound=1, upBound=None)
P5 = pulp.LpVariable('P5', lowBound=1, upBound=None)
#其他常量_来自数据
x_real = 1
x_optimal = 1
y_real = 1
y_optimal = 1
z_real = 1
z_optimal = 1
w_real = 1
w_optimal = 1
#取决于地形
alpha = 0.2
beta = 0.15
#湖面积
S1 = 4
S2 = 3
S3 = 2
S4 = 1

x_diff = x_real - x_optimal
y_diff = y_real - y_optimal
z_diff = z_real - z_optimal
w_diff = w_real - w_optimal

# 目标函数
# problem += abs((D1 + x_diff)/S1) + abs((-(1 - alpha)*D1 + y_diff)/S2) + \
#            abs((-alpha*(1 - beta)*D1 + z_diff)/S3) + abs((-alpha*beta*D1 + D4 + w_diff)/S4)
problem += sign1*((D1 + x_diff)/S1) + sign2*((-(1 - alpha)*D1 + y_diff)/S2) + \
           sign3*((-alpha*(1 - beta)*D1 + z_diff)/S3) + sign4*((-alpha*beta*D1 + D4 + w_diff)/S4)


# 添加约束条件
D1_min = 1
D1_max = 100
D4_min = 1
D4_max = 100
problem += D1 + x_real <= D1_max
problem += D1_min <= D1 + x_real
problem += -alpha*beta*D1 + D4 + w_real >= D4_min
problem += -alpha*beta*D1 + D4 + w_real <= D4_max
#拆开绝对值
#0000
problem += sign1*(D1 + x_diff) >= 0
problem += sign2*(-(1 - alpha)*D1 + y_diff) >= 0
problem += sign3*(-alpha*(1 - beta)*D1 + z_diff) >= 0
problem += sign4*(-alpha*beta*D1 + D4 + w_diff) >= 0

# 求解线性规划问题
problem.solve()

# 打印结果
print("Status:", pulp.LpStatus[problem.status])
print("Optimal values:")
for v in problem.variables():
    print(v.name, "=", v.varValue)
print("Optimal objective value:", pulp.value(problem.objective))









# 目标函数
# problem += abs((D1 + x_diff)/S1) + abs((-(1 - alpha)*D1 + y_diff)/S2) + \
#            abs((-alpha*(1 - beta)*D1 + z_diff)/S3) + abs((-alpha*beta*D1 + D4 + w_diff)/S4)
problem += sign1*(P1 + x_diff) + sign2*(-(1 - alpha)*P2 + y_diff) + \
           sign3*(-alpha*(1 - beta)*P3 + z_diff) + sign4*(-alpha*beta*P4 + P5 + w_diff)

print("Doing nothing: ",x_diff + y_diff + z_diff + w_diff,"\n")
#添加约束条件
#单位：km square
#P = D/S km
P_min = -0.05*0.001
P_max = 0.05*0.001


problem += P1 <= P_max
problem += P_min <= P1 
problem += -alpha*beta*P4 + P5  >= P_min
problem += -alpha*beta*P4 + P5  <= P_max
#拆开绝对值
#0000
problem += sign1*(P1 + x_diff) >= 0
problem += sign2*(-(1 - alpha)*P2 + y_diff) >= 0
problem += sign3*(-alpha*(1 - beta)*P3 + z_diff) >= 0
problem += sign4*(-alpha*beta*P4 + P5 + w_diff) >= 0

problem += P2 == P1*(S1/S2)
problem += P3 == P1*(S1/S3)
problem += P4 == P1*(S1/S4)