import os
import torch

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# 获取当前文件夹路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 子文件夹名称列表
folders = [f"program_{i}" for i in range(164)]

# 命令行命令

command_mutatest = 'mutatest -s ./{source_file} -t "python -m pytest -x" -e ./{test_file} -o mutatest_data.log'



# 遍历子文件夹
for folder in folders:
    subfolder_path = os.path.join(current_dir, folder)
    os.chdir(subfolder_path)  # 进入子文件夹的目录
    torch.cuda.set_device(device)

    source_file = f"{folder}.py"
    test_file = f"test_{folder}.py"
    command = command_mutatest.format(source_file=source_file, test_file=test_file)

    os.system(command)  # 运行命令行命令


