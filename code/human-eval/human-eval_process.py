

#初步提取
# import json
# import os
#
# # 输入的JSON文件路径
# input_file = "human-eval-v2-20210705.jsonl"
# # 输出文件夹路径
# output_folder = "human-eval"
#
# # 创建输出文件夹
# os.makedirs(output_folder, exist_ok=True)
# count=0
# # 读取输入文件
# with open(input_file, "r") as file:
#     # 逐行读取每个字典数据
#     for line in file:
#         # 解析JSON数据
#         data = json.loads(line)
#         data["task_id"]=count
#         count+=1
#         # 提取所需的字段
#         task_id = data["task_id"]
#         prompt = data["prompt"]
#         canonical_solution = data["canonical_solution"]
#         test = data["test"]
#
#         # 创建新的JSON文件路径
#         output_file = os.path.join(output_folder, f"{task_id}.json")
#
#         # 构建字典数据
#         output_data = {
#             "task_id": task_id,
#             "prompt": prompt,
#             "canonical_solution": canonical_solution,
#             "test": test
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
# output_folder = "human-eval"
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
# import os
# import json
# import re
#
# # 指定包含文件夹的路径
# output_folder = "human-eval"
# program_name = "program_"
# # 遍历每个文件夹
# for folder_name in os.listdir(output_folder):
#     folder_path = os.path.join(output_folder, folder_name)
#
#     # 仅处理文件夹
#     if os.path.isdir(folder_path):
#         for filename in os.listdir(folder_path):
#             new_filename = folder_name.replace(program_name, "")
#             if filename == f"{new_filename}.json":
#                 file_path = os.path.join(folder_path, filename)
#
#             # 仅处理以 .json 结尾的文件
#                 with open(file_path, "r") as file:
#                     data = json.load(file)
#                     prompt = data["prompt"]
#                     canonical_solution = data["canonical_solution"]
#
#                     # 合并函数头和实现
#                     function_code = prompt + canonical_solution
#                     cleaned_code = re.sub(r'\"\"\"(.+?)\"\"\"', '', function_code, flags=re.DOTALL)
#
#
#                     # 生成Python文件名
#                     py_file_name = f"{folder_name}.py"
#                     py_file_path = os.path.join(folder_path, py_file_name)
#
#                     # 将函数代码写入Python文件
#                     with open(py_file_path, "w",encoding="utf-8") as py_file:
#                         py_file.write(cleaned_code)




# 切分每个测试用例
import os
import json
import re

# 指定包含文件夹的路径
output_folder = "human-eval"
program_name = "Humaneval_"
# 遍历每个文件夹
for folder_name in os.listdir(output_folder):
    folder_path = os.path.join(output_folder, folder_name)

    # 仅处理文件夹
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            new_filename = folder_name.replace(program_name, "")
            if filename == f"{new_filename}.json":
                file_path = os.path.join(folder_path, filename)
                if filename.endswith(".json"):
                    # 仅处理以 .json 结尾的文件
                    with open(file_path, "r") as file:
                        data = json.load(file)
                        test = data["test"]
                        prompt = data["prompt"]

                        # 提取函数名
                        function_names = []
                        lines = prompt.split("\n")
                        for line in lines:
                            line = line.strip()
                            if line.startswith("def"):
                                function_name = line.split(" ")[1].split("(")[0]
                                function_names.append(function_name)
                        # 使用正则表达式提取每个 assert 语句
                        assert_statements = re.findall(r'assert (.+)', test)

                        # 提取函数名
                        function_name = function_names[-1]

                        # 构建每个 assert 语句对应的 test_ 函数
                        test_functions = []
                        for i, assert_statement in enumerate(assert_statements):
                            test_function = f"def test_{i + 1}():\n    assert {assert_statement.replace('candidate', function_name)}"
                            test_functions.append(test_function)

                        # 生成 Python 文件路径
                        py_file_name = f"test_{folder_name}.py"
                        py_file_path = os.path.join(folder_path, py_file_name)

                        # 写入 Python 文件内容
                        with open(py_file_path, "w",encoding="utf-8") as py_file:
                            py_file.write(f"import sys\n")
                            py_file.write(f"sys.path.append('../')\n")
                            # 第一行：from 文件名 import 函数名
                            for i,x in enumerate(function_names):
                                py_file.write(f"from {folder_name} import {function_names[i]}\n")
                            # 第二行：def test_函数名()
                            py_file.write('\n'.join(test_functions))


