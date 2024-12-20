import pandas as pd

def extract_integer(value):
    try:
        return int(''.join(filter(str.isdigit, value)))
    except ValueError:
        return None

def process_excel_file(file_path):
    # 读取Excel文件
    df = pd.read_excel(file_path)
    
    # 检查是否有足够的列
    if len(df.columns) < 1:
        print("文件的列数不足1列，无法处理。")
        return
    
    # 将第一列的内容更改为其中的整数值
    df[df.columns[0]] = df[df.columns[0]].apply(extract_integer)
    
    # 保存处理后的文件
    df.to_excel(file_path, index=False)
    print(f"文件 {file_path} 处理完成并保存。")

if __name__ == '__main__':
    file_path = './mbpppluscc.xlsx'  # 替换为你的文件路径
    process_excel_file(file_path)