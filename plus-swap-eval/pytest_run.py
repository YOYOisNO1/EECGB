import os
import torch


# 获取当前文件夹路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 子文件夹名称列表
folders = [f"program_{i}" for i in range(164)]

# 命令行命令
command_pytest = 'pytest ./{test_file}'



# 遍历子文件夹
for i,folder in enumerate(folders):
    subfolder_path = os.path.join(current_dir, folder)
    os.chdir(subfolder_path)  # 进入子文件夹的目录

    test_file = f"test_{folder}.py"
    command = command_pytest.format(test_file=test_file)
    os.system(command)  # 运行命令行命令
