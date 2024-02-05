with open('test_file.txt', 'r') as file:
    # 读取文件中的一行数据，并使用 split() 方法将其分割成一个列表
    data_list = file.readline().split()

# 将列表中的字符串转换为整数
data_list = [float(x) for x in data_list]

# 打印数据列表
print(data_list)