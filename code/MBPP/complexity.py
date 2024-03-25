import ast
import re
import os
import astor
import openpyxl


def calculate_cyclomatic_complexity(code):
    # 将代码转换为AST
    tree = ast.parse(code)

    # 统计圈复杂度的计数器
    complexity = 1

    # 遍历AST节点
    for node in ast.walk(tree):
        if isinstance(node, (ast.While, ast.For, ast.With, ast.Try,ast.ExceptHandler, ast.FunctionDef,ast.Break,ast.Continue)):
            complexity += 1
        if isinstance(node, ast.If):
            complexity += 1
            if isinstance(node.test, ast.BoolOp):
                if isinstance(node.test.op, (ast.And,ast.Or)):
                    complexity += (1 if not node.test.values else len(node.test.values)-1)
            if node.orelse:#判断是否存在else
                complexity += 1
            if node.orelse and isinstance(node.orelse[0], ast.If):#判断是否存在elif
                complexity += 1
                if isinstance(node.orelse[0].test, ast.BoolOp):
                    if isinstance(node.orelse[0].test.op, (ast.And, ast.Or)):
                        complexity += (1 if not node.orelse[0].test.values else len(node.orelse[0].test.values) - 1)


    # 获取列表中的内容的圈复杂度
    list_count = count_list(code)
    complexity += list_count

    return complexity


def count_list(code):
    # 将代码字符串转换为AST树
    ast_tree = ast.parse(code)
    # 在AST树中查找列表推导式
    list_comprehensions = [node for node in ast.walk(ast_tree) if isinstance(node, ast.ListComp)]

    if len(list_comprehensions) > 0:
        # 提取第一个列表推导式并返回其中的代码部分
        list_comp_node = list_comprehensions[0]
        list_comp_code = astor.to_source(list_comp_node)
        list_content = list_comp_code.strip()[1:-1]
    else:
        list_content = ""
    # 使用split方法将字符串按空格拆分为单词列表
    words = list_content.split()

    complexity = 0

    count_for = words.count('for')
    count_if = words.count('if')
    count_and_or = words.count('and') + words.count('or')

    # 更新圈复杂度，每个if语句增加一个路径，每个and/or增加一个路径
    complexity += count_if + count_and_or + count_for

    return complexity


def read_code_file(file_path):
    with open(file_path, "r") as file:
        code = file.read()
    return code

def complexity(file_path):

    code = read_code_file(file_path)
    # 计算圈复杂度
    complexity = calculate_cyclomatic_complexity(code)

    return complexity


# 创建一个新的工作簿
workbook = openpyxl.Workbook()
worksheet = workbook.active

# 获取当前文件夹路径
current_dir = os.path.dirname(os.path.abspath(__file__))

father_dir = ["human-eval","human-evalplus","MBPP"]

# 子文件夹名称列表
folders = [f"program_{i}" for i in range(1,975)]

# 遍历子文件夹
for folder in folders:
    subfolder_path = os.path.join(current_dir,folder)
    os.chdir(subfolder_path)  # 进入子文件夹的目录
    source_file = f"{folder}.py"
    try:
        count = complexity(source_file)
        print("{}/{}:complexity = {}".format(father_dir[2], source_file,count))
        worksheet.append([father_dir[2]+"/"+source_file, count])
    except:
        print("{}/{}:complexity = EOR".format(father_dir[2], source_file))
        worksheet.append([father_dir[2] + "/" + source_file, 0])
        continue

# 保存工作簿到文件
workbook.save("result.xlsx")

# 平均值
# for folder in folders:
#     subfolder_path = os.path.join(current_dir,"humanEvalPlus","chatgpt_temp_0.8",folder)
#     os.chdir(subfolder_path)  # 进入子文件夹的目录
#     sum = 0.0
#
#     for i in range(200):
#
#         source_file = f"{i}.py"
#         try:
#             count = complexity(source_file)
#             print("{}/{}:complexity = {}".format(folder, source_file,count))
#             # 将结果保存到工作表中
#             # worksheet.append([folder+"/"+source_file, count])
#             sum+=count
#         except:
#             print("{}/{}:complexity = EOR".format(folder, source_file))
#             sum += 0
#             continue
#     ave_count = sum/200
#     worksheet.append([folder, ave_count])
#
# # 保存工作簿到文件
# workbook.save("ave.xlsx")