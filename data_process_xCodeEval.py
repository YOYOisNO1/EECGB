#刘欣炜
import json
import os
import ast
import re

# 读取unittest_db.json文件
with open('unittest_db.json', 'r') as file:
    unittest_db = json.load(file)

# 读取python.jsonl文件
with open('./code_compilation/test/python.jsonl', 'r') as file:
    data = file.readlines()

# 遍历每个字典，并生成相应的子文件夹、Python文件和测试文件
for i, entry in enumerate(data):
    entry_dict = json.loads(entry)

    # 创建子文件夹
    folder_name = os.path.join('./code_compilation', 'programme', f'problem{i}').replace('\\', '/')
    os.makedirs(folder_name, exist_ok=True)

    # 生成Python文件
    python_file_name = f'program{i}.py'
    with open(os.path.join(folder_name, python_file_name), 'w', encoding='utf-8') as python_file:
        code = entry_dict['source_code'].replace('raw_input', 'input')
        # 替换 print "YES" 为 print("YES")
        code = code.replace('print "YES"', 'print("YES")')
        # 替换 print "NO" 为 print("NO")
        code = code.replace('print "NO"', 'print("NO")')
        if not re.search(r'\bdef\b', code):
            python_file.write(f'def program{i}():\n')
        indented_code = '\n'.join(
            ['    ' + line if not re.search(r'\bdef\b', line) else line for line in code.splitlines()])
        python_file.write(indented_code)

        # 根据 src_uid 查找对应的输入和输出
    src_uid = entry_dict['src_uid']
    if src_uid in unittest_db:
        # 获取对应的输入和输出
        test_cases = unittest_db[src_uid]

        # 生成子文件夹中的测试数据文件路径
        test_data_file_path = f'{folder_name}/test.json'
        proram_data=f'{folder_name}/program{i}.py'
        # 构造输入和输出列表
        input_list = [case['input'].strip() for case in test_cases]
        output_list = [case['output'] for case in test_cases]

        # 将输入和输出保存到测试数据文件中
        # with open(test_data_file_path, 'w', encoding='utf-8') as test_data_file:
        #     json.dump({'input': input_list, 'output': output_list}, test_data_file)
        #
        #     with open(proram_data, 'r') as program_file:
        #         program_code = program_file.read()
        #         ast_tree = ast.parse(program_code)
        #         for node in ast_tree.body:
        #             if isinstance(node, ast.FunctionDef):
        #                 function_name = node.name
        #                 break
            # 创建 test 子文件夹
        test_folder = f'{folder_name}/test'
        os.makedirs(test_folder, exist_ok=True)

            # 遍历测试用例，生成对应的测试文件
        for j, test_case in enumerate(test_cases):
            test_file_path = f'{test_folder}/test{j}.py'
            function_name = f'program{i}'
            # 写入测试文件内容
            with open(test_file_path, 'w', encoding='utf-8') as test_file:
                test_file.write(f'from ..program{i} import {function_name}\n')
                test_file.write(f'def test{j}():\n')
                test_file.write(
                    f'    assert {function_name}({test_case["input"].strip()}) == {test_case["output"]}')

