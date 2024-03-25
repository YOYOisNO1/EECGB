import os
import json
import re
import subprocess
from evalplus.data import write_jsonl

#初步提取
# import json
# import os
#
# # 输入的JSON文件路径
# input_file = "mbpp_questions.jsonl"  # 输入的JSONL文件
# output_folder = "MBPP"
#
# # 创建输出文件夹
# os.makedirs(output_folder, exist_ok=True)
# # 读取输入文件
# with open(input_file, "r") as file:
#     # 逐行读取每个字典数据
#     for line in file:
#         # 解析JSON数据
#         data = json.loads(line)
#         # 提取所需的字段
#         program_id = data["id"]
#         solution = data["solution"]
#         test_case = data["testing_code"]
#
#         # 创建新的JSON文件路径
#         output_file = os.path.join(output_folder, f"{program_id}.json")
#
#         # 构建字典数据
#         output_data = {
#             "program_id": program_id,
#             "solution": solution,
#             "test_case": test_case
#         }
#
#         # 将字典数据写入新的JSON文件
#         with open(output_file, "w") as output:
#             json.dump(output_data, output, indent=4)


#每个id一个文件夹
# import os
# import json
# import shutil
#
# # 指定 output_folder 路径
# output_folder = "MBPP"
#
# # 遍历 output_folder 中的文件
# for filename in os.listdir(output_folder):
#     if filename.endswith(".json"):
#         file_path = os.path.join(output_folder, filename)
#         task_id = f"program_{os.path.splitext(filename)[0]}"
#
#         # 创建相应的文件夹
#         folder_path = os.path.join(output_folder, task_id)
#         os.makedirs(folder_path, exist_ok=True)
#
#         # 移动当前 JSON 文件到相应的文件夹中
#         new_file_path = os.path.join(folder_path, filename)
#         shutil.move(file_path, new_file_path)


#组成完整函数保存到每个文件夹
import os
import json
import re

# 指定包含文件夹的路径
output_folder = "MBPP"
program_name = "program_"
# 遍历每个文件夹
for folder_name in os.listdir(output_folder):
    folder_path = os.path.join(output_folder, folder_name)

    # 仅处理文件夹
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            new_filename = folder_name.replace(program_name, "")
            if filename == f"{new_filename}.json":
                file_path = os.path.join(folder_path, filename)

                # 保存为函数py文件
                with open(file_path, "r") as file:
                    data = json.load(file)
                    solution = data["solution"]

                    # 生成Python文件名
                    py_file_name = f"{folder_name}.py"
                    py_file_path = os.path.join(folder_path, py_file_name)

                    # 将函数代码写入Python文件
                    with open(py_file_path, "w",encoding="utf-8") as py_file:
                        py_file.write(solution)

                # 保存为测试用例py文件
                with open(file_path, "r") as file:
                    data = json.load(file)
                    solution = data["solution"]
                    test_case = data["test_case"]

                    # 提取函数名
                    function_names = []
                    lines = solution.split("\n")
                    for line in lines:
                        line = line.strip()
                        if line.startswith("def"):
                            function_name = line.split(" ")[1].split("(")[0]
                            function_names.append(function_name)
                    # 使用正则表达式提取每个 assert 语句
                    assert_statements = re.findall(r'assert (.+)', test_case)

                    # 提取函数名
                    function_name = function_names[-1]

                    # 构建每个 assert 语句对应的 test_ 函数
                    test_functions = []
                    for i, assert_statement in enumerate(assert_statements):
                        test_function = f"def test_{i + 1}():\n    assert {assert_statement}"
                        test_functions.append(test_function)

                    # 生成 Python 文件路径
                    py_file_name = f"test_{folder_name}.py"
                    py_file_path = os.path.join(folder_path, py_file_name)

                    # 写入 Python 文件内容
                    with open(py_file_path, "w",encoding="utf-8") as py_file:
                        # 第一行：from 文件名 import 函数名
                        for i,x in enumerate(function_names):
                            py_file.write(f"from {folder_name} import {function_names[i]}\n")
                        # 第二行：def test_函数名()
                        py_file.write('\n'.join(test_functions))