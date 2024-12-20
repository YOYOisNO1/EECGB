import os
import torch
import subprocess

# 获取当前文件夹路径
current_dir = "/Se-liuxiangyue/lxy/EECGB/plus-swap-eval"

# 子文件夹名称列表
folders = [f"program_{i}" for i in range(164)]

# 命令行命令

# command_coverage = 'coverage run {test_file}'
# command3 = 'coverage report -m '
command_coverage = 'pytest --cov --cov-branch'


# 遍历子文件夹
for i,folder in enumerate(folders): # 进入子文件夹的目录
    subfolder_path = os.path.join(current_dir, folder)
    os.chdir(subfolder_path)
    # source_file = f"HumanEval_{i}"
    # test_file = f"test_{folder}.py"
    # command2 = command_coverage.format(test_file=test_file)
    # os.system(command2)  # 运行命令行命令
    # os.system(command3)
    source_file = f"program_{i}"
    # test_file = f"test_{folder}.py"
    # command2 = command_coverage.format(test_file=test_file)
    os.system(command_coverage)  # 运行命令行命令
    # os.system(command3)
    command = "ps -ef|grep pytest|grep -v grep|cut -c 9-15|xargs kill -9"
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)