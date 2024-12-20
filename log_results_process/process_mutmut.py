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
            if len(df.columns) < 5:
                print(f"文件 {filename} 的列数不足5列，跳过处理。")
                continue
            
            # 计算新列mutatest的值
            df['mutmut'] = df.apply(lambda row: row[3] / row[4] if row[4] != 0 and pd.notna(row[4]) else None, axis=1)
            
            # 删除第2, 3, 4, 5列
            df.drop(columns=[ df.columns[2], df.columns[3], df.columns[4]], inplace=True)
            
            # 保存处理后的文件
            df.to_csv(file_path, index=False)
            print(f"文件 {filename} 处理完成并保存。")

if __name__ == '__main__':
    folder_path = '/Se-liuxiangyue/lxy/EECGB/log_results_process/csv - test/mutmut'  # 替换为你的文件夹路径
    process_csv_files(folder_path)