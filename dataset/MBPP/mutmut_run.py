import os
import torch

#device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


# 子文件夹名称列表
qid_list = []

for entry in os.scandir("./problem"):
    if entry.is_dir():
        qid = entry.name
        qid_list.append(qid)

for qid in qid_list:

    # 命令行命令
    command1 = 'rm -f .mutmut-cache'
    command_mutmut = 'mutmut run --paths-to-mutate ./{source_file} --runner "python -m pytest -x" --tests-dir ./{test_file}'
    command3 = 'mutmut show all | tee data.log'
    command4 = 'pytest'


    # 遍历子文件夹

    subfolder_path = os.path.join("./problem", qid)
    os.chdir(subfolder_path)  # 进入子文件夹的目录
    #torch.cuda.set_device(device)

    source_file = f"program{qid}.py"
    test_file = f"test_program{qid}.py"

    command2 = command_mutmut.format(source_file=source_file, test_file=test_file)
    os.system(command1)  # 运行命令行命令
    os.system(command2)  # 运行命令行命令
    os.system(command3)  # 运行命令行命令
    os.system(command4)  # 运行命令行命令
