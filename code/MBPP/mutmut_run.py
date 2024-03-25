import os

# 获取测试文件位置
current_dir = os.path.dirname(os.path.abspath(__file__))

# 子文件夹名称列表
folders = [f"program_{i}" for i in range(1,975)]

# 命令行命令
command1 = 'rm -f .mutmut-cache'
command_mutmut = 'mutmut run --paths-to-mutate ./{source_file} --runner "python -m pytest -x" --tests-dir ./{test_file}'
command3 = 'mutmut show all | tee mutmut_data.log'
command4 = 'pytest'


# 遍历子文件夹
for folder in folders:
    subfolder_path = os.path.join(current_dir, folder)
    os.chdir(subfolder_path)  # 进入子文件夹的目录

    source_file = f"{folder}.py"
    test_file = f"test_{folder}.py"
    command2 = command_mutmut.format(source_file=source_file, test_file=test_file)
    os.system(command1)  # 运行命令行命令
    os.system(command2)  # 运行命令行命令
    os.system(command3)  # 运行命令行命令
    os.system(command4)  # 运行命令行命令
