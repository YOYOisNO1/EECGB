import os
import pandas as pd

def extract_integer(value):
    try:
        return int(''.join(filter(str.isdigit, value)))
    except ValueError:
        return None

def process_csv_files(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            # 读取CSV文件
            df = pd.read_csv(file_path)
            
            # 检查是否有足够的列
            if len(df.columns) < 7:
                print(f"文件 {filename} 的列数不足7列，跳过处理。")
                continue
            
            # 将第一列的内容更改为其中的整数值
            df[df.columns[0]] = df[df.columns[0]].apply(extract_integer)
            df[df.columns[1]] = df[df.columns[1]].apply(extract_integer)
            
            # 计算第8列 (SC) 的值
            df['SC'] = df.apply(lambda row: (row[2] - row[3]) / row[2] if row[2] != 0 and pd.notna(row[2]) else None, axis=1)
            
            # 计算第9列 (BC) 的值
            df['BC'] = df.apply(lambda row: (row[4] - row[5]) / row[4] if row[4] != 0 and pd.notna(row[4]) else None, axis=1)
            
            # 删除第3-7列
            columns_to_drop = df.columns[2:7]
            df.drop(columns=columns_to_drop, inplace=True)
            
            # 保存处理后的文件
            df.to_csv(file_path, index=False)
            print(f"文件 {filename} 处理完成并保存。")

if __name__ == '__main__':
    folder_path = '/Se-liuxiangyue/lxy/EECGB/log_results_process/csv - test/humanevalcodegen2b'  # 替换为你的文件夹路径
    process_csv_files(folder_path)