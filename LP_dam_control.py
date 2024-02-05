import pulp
import sys

with open('real_data.txt', 'r') as file:
    # 读取文件中的一行数据，并使用 split() 方法将其分割成一个列表
    real_data_list = file.readline().split()
# 将列表中的字符串转换为浮点数
real_data_list = [float(x) for x in real_data_list]
# 打印数据列表
print(real_data_list)

with open('optimal_data.txt', 'r') as file:
    optimal_data_list = file.readline().split()
optimal_data_list = [float(x) for x in optimal_data_list]
print(optimal_data_list)

with open('area_data.txt', 'r') as file:
    area_data_list = file.readline().split()
area_data_list = [float(x) for x in area_data_list]
print(area_data_list)


x_real, y_real, z_real, w_real = real_data_list
x_optimal, y_optimal, z_optimal, w_optimal = optimal_data_list
S1, S2, S3, S4 = area_data_list
x_diff = x_real - x_optimal
y_diff = y_real - y_optimal
z_diff = z_real - z_optimal
w_diff = w_real - w_optimal
#取决于地形
alpha = 0.3
beta = 0.2

#sign
#0000
sign1 = 1
sign2 = 1
sign3 = 1
sign4 = 1
       
def LPfunction():
    problem = pulp.LpProblem("Optimization Problem", pulp.LpMinimize)

    P_min = -0.1*0.001
    P_max = 0.1*0.001

# 定义LP中的变量_两个大坝的放水量
    P1 = pulp.LpVariable('P1', lowBound=P_min, upBound=P_max)
    P2 = pulp.LpVariable('P2', lowBound=P_min, upBound=P_max)
    P3 = pulp.LpVariable('P3', lowBound=P_min, upBound=P_max)
    P4 = pulp.LpVariable('P4', lowBound=P_min, upBound=P_max)
    P5 = pulp.LpVariable('P5', lowBound=P_min, upBound=P_max)

    #目标函数
    problem += sign1*(P1*1000 + x_diff) + sign2*(-(1 - alpha)*P2*1000 + y_diff) + \
        sign3*(-alpha*(1 - beta)*P3*1000 + z_diff) + sign4*(-alpha*beta*P4*1000 + P5*1000 + w_diff)
    #if doing nothing        
    print("Doing nothing: ",x_diff + y_diff + z_diff + w_diff,"\n")
    #添加约束条件
    #单位：km square
    #P = D/S km

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

    # 求解线性规划问题
    problem.solve()

    if(pulp.LpStatus[problem.status] == "Infeasible"):
        with open('output_Jan.txt', 'a') as file:
            sys.exit()
            # print("Failed",file=file)
    else:
        with open('output_Jan.txt', 'a') as file:
        # 使用 print() 函数将数据写入文件
            print(pulp.LpStatus[problem.status],file=file)
            print("Optimal values:",file=file)
            for v in problem.variables():
                print(v.varValue," km",file=file)
            print(pulp.value(problem.objective)," m",file=file)
            print("if doing nothing:",abs(x_diff) + abs(y_diff) + abs(z_diff) + abs(w_diff),file=file)
            print("\n",file=file)
    # 打印结果
    # print("Status:", pulp.LpStatus[problem.status])
    # print("Optimal values:")
    # for v in problem.variables():
    #     print(v.name, "=", v.varValue)
    # print("Optimal objective value:", pulp.value(problem.objective))
loop_value = [1,-1]
#loop
for value1 in loop_value:
    sign1 = value1
    for value2 in loop_value:
        sign2 = value2
        for value3 in loop_value:
            sign3 = value3
            for value4 in loop_value:
                sign4 = value4
                LPfunction()