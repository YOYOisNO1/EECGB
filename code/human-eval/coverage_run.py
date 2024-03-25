import os

# 获取测试文件位置
current_dir = "/Se-zhaozhiwei/hyf/example/human-eval"

# 子文件夹名称列表
folders = [f"program_{i}" for i in range(164)]

# 命令行命令
command_coverage = 'pytest --cov --cov-branch'

# 遍历子文件夹
for i,folder in enumerate(folders):
    # 进入子文件夹的目录
    subfolder_path = os.path.join(current_dir, folder)
    os.chdir(subfolder_path)

    test_file = f"test_{folder}.py"
    # command2 = command_coverage.format(test_file=test_file)
    os.system(command_coverage)  # 运行命令行命令

