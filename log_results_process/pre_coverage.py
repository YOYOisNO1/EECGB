import os
import pandas as pd

def process_csv_files(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            # 读取CSV文件
            df = pd.read_csv(file_path)
            
            # 检查是否有足够的列
            if len(df.columns) < 2:
                print(f"文件 {filename} 的列数不足2列，跳过处理。")
                continue
            
            # 去重，保留第一个读取到的行
            df = df.drop_duplicates(subset=[df.columns[0], df.columns[1]], keep='first')
            
            # 保存处理后的文件
            df.to_csv(file_path, index=False)
            print(f"文件 {filename} 处理完成并保存。")

if __name__ == '__main__':
    folder_path = '/Se-liuxiangyue/lxy/EECGB/log_results_process/csv - test/humanevalcodegen2b'  # 替换为你的文件夹路径
    process_csv_files(folder_path)