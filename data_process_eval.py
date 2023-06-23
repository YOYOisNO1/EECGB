

#初步提取
# import json
# import os
#
# # 输入的JSON文件路径
# input_file = "human-eval-v2-20210705.jsonl"
# # 输出文件夹路径
# output_folder = "output_folder"
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
# output_folder = "output_folder"
#
# # 遍历 output_folder 中的文件
# for filename in os.listdir(output_folder):
#     file_path = os.path.join(output_folder, filename)
#
#     # 仅处理以 .json 结尾的文件
#     if filename.endswith(".json"):
#         with open(file_path, "r") as file:
#             data = json.load(file)
#
#             task_id = str(data["task_id"])  # 将 task_id 转换为字符串类型
#
#             # 创建相应的文件夹
#             folder_path = os.path.join(output_folder, task_id)
#             os.makedirs(folder_path, exist_ok=True)
#
#             # 将当前 JSON 文件移动到相应的文件夹中
#             new_file_path = os.path.join(folder_path, filename)
#             shutil.move(file_path, new_file_path)


#组成完整函数保存到每个文件夹
# import os
# import json
# import re
#
# # 指定包含文件夹的路径
# output_folder = "output_folder"
#
# # 遍历每个文件夹
# for folder_name in os.listdir(output_folder):
#     folder_path = os.path.join(output_folder, folder_name)
#
#     # 仅处理文件夹
#     if os.path.isdir(folder_path):
#         for filename in os.listdir(folder_path):
#             if filename == f"{folder_name}.json":
#                 file_path = os.path.join(folder_path, filename)
#
#             # 仅处理以 .json 结尾的文件
#                 with open(file_path, "r") as file:
#                     data = json.load(file)
#                     prompt = data["prompt"]
#                     function_header1 = re.search(r"def (\w+)", prompt).group(1)
#
#                     canonical_solution = data["canonical_solution"]
#
#                     lines = prompt.strip().split("\n")
#                     function_header = ""
#
#                     # 标志用于判断是否处于选中状态
#                     selecting = False
#
#                     for line in lines:
#                         if line.strip().startswith("def"):
#                             selecting = True
#
#                         if selecting:
#                             function_header += line + "\n"
#                             break
#
#                         # 当遇到空行时，表示函数头部分结束
#
#                     # 合并函数头和实现
#                     function_code = function_header + canonical_solution
#
#                     # 创建新的 JSON 数据
#                     new_data = {
#                         "function_code": function_code
#                     }
#
#                     # 构造新的文件名
#                     new_filename = filename.replace(filename, f"{function_header1}.json")
#                     new_file_path = os.path.join(folder_path, new_filename)
#
#                     # 写入新的 JSON 文件
#                     with open(new_file_path, "w") as new_file:
#                         json.dump(new_data, new_file, indent=4)

#切分每个测试用例
# import os
# import json
# import re
# output_folder = "output_folder"
#
# # 遍历每个文件夹
# for folder_name in os.listdir(output_folder):
#     folder_path = os.path.join(output_folder, folder_name)
#     if os.path.isdir(folder_path):
#         json_file_path = os.path.join(folder_path, folder_name + ".json")  # 构造 JSON 文件名
#
#         # 读取 JSON 文件内容
#         with open(json_file_path, "r") as json_file:
#             data = json.load(json_file)
#
#             # 提取需要的字段，这里以 test 字段为例
#             test = data["test"]
#             prompt = data["prompt"]
#             function_header = re.search(r"def (\w+)", prompt).group(1)
#             # 获取函数名（假设函数名与文件夹名相同）
#             function_name = function_header
#
#             # 按行提取包含 assert 的行，并替换 "candidate" 为函数名
#             assert_lines = [line.strip().replace("candidate", function_name) for line in test.split("\n") if
#                             "assert" in line]
#
#             # 保存每个 assert 行为单独的文件
#             for i, line in enumerate(assert_lines):
#                 assert_data = {
#                     "line": line
#                 }
#
#                 assert_file_path = os.path.join(folder_path, f"assert_line_{i}.json")
#                 with open(assert_file_path, "w") as assert_file:
#                     json.dump(assert_data, assert_file)

#生成函数py
# import os
# import json
# import re
# # 指定存储生成的Python文件的目录
# output_directory = "output_folder"
#
# # 遍历文件夹
# for folder_name in os.listdir(output_directory):
#     folder_path = os.path.join(output_directory, folder_name)
#     if not os.path.isdir(folder_path):
#         continue
#
#     # 生成modified.json文件名
#     json_file_name = f"{folder_name}_modified.json"
#     json_file_path = os.path.join(folder_path, json_file_name)
#
#
#     # 读取modified.json文件内容
#     with open(json_file_path, "r") as json_file:
#         data = json.load(json_file)
#
#
#     # 提取函数代码
#     function_code = data["function_code"]
#     function_header = re.search(r"def (\w+)", function_code).group(1)
#
#     # 生成Python文件名
#     py_file_name = f"{function_header}.py"
#     py_file_path = os.path.join(folder_path, py_file_name)
#
#     # 将函数代码写入Python文件
#     with open(py_file_path, "w") as py_file:
#         py_file.write(function_code)


#生成测试用例py
# import os
# import json
# import re
#
# output_folder = "output_folder"
#
# # 遍历文件夹
# for folder_name in os.listdir(output_folder):
#     folder_path = os.path.join(output_folder, folder_name)
#     if not os.path.isdir(folder_path):
#         continue
#
#     # 获取对应的测试文件夹路径
#     test_folder_path = os.path.join("test_folder", f"test_{folder_name}")
#     os.makedirs(test_folder_path, exist_ok=True)
#
#     # 保存对应的数字
#     file_numbers = {}
#
#     # 遍历文件夹中的所有文件
#     for file_name in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, file_name)
#
#         # 读取 modified 文件
#         modified_file_name = f"{folder_name}_modified.json"
#         modified_file_path = os.path.join(folder_path, modified_file_name)
#
#         if os.path.exists(modified_file_path):
#             # 读取 modified JSON 文件内容
#             with open(modified_file_path, "r") as modified_file:
#                 modified_json_data = json.load(modified_file)
#
#         # 提取函数名和对应的 JSON 内容
#         function_name = modified_json_data["function_code"]
#         function_header = re.search(r"def (\w+)", function_name).group(1)
#
#         # 判断文件是否为 assert_line_x.json
#         if not file_name.startswith("assert_line") or not file_name.endswith(".json"):
#             continue
#
#         # 提取数字并保存到字典中
#         file_number = int(file_name.replace("assert_line_", "").replace(".json", ""))
#         file_numbers[file_number] = file_path
#
#
#     # 遍历数字，生成对应的测试文件
#     for file_number, file_path in file_numbers.items():
#         # 读取 JSON 文件内容
#         with open(file_path, "r") as json_file:
#             json_data = json.load(json_file)
#
#         # 提取函数名和对应的 JSON 内容
#         py_file_name = f"test_{function_header}_{file_number}.py"
#
#         # 生成对应的 test_taskid 文件夹路径
#         #test_taskid_folder_path = os.path.join(test_folder_path, f"test_{folder_name}")
#         #os.makedirs(test_taskid_folder_path, exist_ok=True)
#
#         # 生成 Python 文件路径
#         py_file_path = os.path.join(test_folder_path, py_file_name)
#
#         # 提取 assert 行的内容
#         assert_line = json_data["line"]
#
#         # 写入 Python 文件内容
#         with open(py_file_path, "w") as py_file:
#             # 第一行：from 文件名 import 函数名
#             py_file.write(f"from {folder_name} import {function_header}\n")
#             # 第二行：def test_函数名()
#             py_file.write(f"def test_{function_header}():\n")
#             # 第三行：写入 assert 行的内容
#             py_file.write(f"    {assert_line}\n")


#文件夹合并
# import os
# import shutil
#
# output_folder = "output_folder"
# test_folder = "test_folder"
#
#        # 遍历 test 文件夹
# for folder_name in os.listdir(test_folder):
#     test_folder_path = os.path.join(test_folder, folder_name)
#     if not os.path.isdir(test_folder_path):
#         continue
#
#     # 提取文件夹名称中的数字
#     folder_id = folder_name.split("_")[1]
#
#     # 获取对应的输出文件夹路径
#     output_folder_path = os.path.join(output_folder, folder_id)
#     os.makedirs(output_folder_path, exist_ok=True)
#
#     # 遍历文件夹中的文件
#     for file_name in os.listdir(test_folder_path):
#         file_path = os.path.join(test_folder_path, file_name)
#
#         # 复制文件到输出文件夹中
#         shutil.copy(file_path, output_folder_path)


#名称统一
# import os
# import re
#
# output_folder = "output_folder"
#
# # 遍历 output 文件夹
# for folder_name in os.listdir(output_folder):
#     folder_path = os.path.join(output_folder, folder_name)
#     if not os.path.isdir(folder_path):
#         continue
#
#     # 查找对应的 modified 文件
#     modified_file_name = None
#     for file_name in os.listdir(folder_path):
#         if file_name.endswith("_modified.json"):
#             modified_file_name = file_name
#             break
#
#     if modified_file_name:
#         # 提取函数名
#         function_name = modified_file_name[:-13]  # 去除 "_modified.json" 部分
#
#         # 构建新的文件名
#         new_modified_file_name = f"{function_name}.json"
#         modified_file_path = os.path.join(folder_path, modified_file_name)
#         new_modified_file_path = os.path.join(folder_path, new_modified_file_name)
#
#         # 重命名 modified 文件
#         os.rename(modified_file_path, new_modified_file_path)



#批量测试用例py

import os
import json
import re

# 指定包含文件夹的路径
output_folder = "output_folder"

# 遍历每个文件夹
for folder_name in os.listdir(output_folder):
    folder_path = os.path.join(output_folder, folder_name)

    # 仅处理文件夹
    if os.path.isdir(folder_path):
        # 构造子文件夹中的 id.json 文件路径
        json_file_path = os.path.join(folder_path, f"{folder_name}.json")

        # 检查文件是否存在
        if os.path.isfile(json_file_path):
            # 打开 id.json 文件
            with open(json_file_path, "r") as json_file:
                json_data = json.load(json_file)
                # 提取函数名和对应的 JSON 内容
                test = json_data["test"]
                function_name = json_data["prompt"]

                # 提取函数名
                function_header = re.search(r"def (\w+)", function_name).group(1)
                function_info = {
                    "function_name": function_header,
                    "assertions": []
                }
                test = test.replace("candidate", function_header)

                # 匹配多行 assert 语句
                assert_matches = re.findall(r"assert.*?(?=\n\n|\n$)", test, re.DOTALL)
                separate_asserts = []
                for assert_match in assert_matches:
                    if "assert" in assert_match:
                        # 提取每个 assert 语句
                        asserts = re.findall(r"assert.*?(?=\n|$)", assert_match)
                        separate_asserts.extend(asserts)

                # 生成测试文件路径
                py_file_name = f"test_{function_header}.py"
                py_file_path = os.path.join(folder_path, py_file_name)

                # 写入测试文件内容
                with open(py_file_path, "w") as py_file:
                    py_file.write(f"from has import {function_header}\n\n")

                    # 生成对应的测试函数
                    for i, separate_assert in enumerate(separate_asserts):
                        py_file.write(f"def test_{function_header}_{i}():\n")
                        py_file.write(f"    {separate_assert}\n\n")


