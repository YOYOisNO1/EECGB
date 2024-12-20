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
            
            # 尝试不同的编码格式读取CSV文件
            encodings = ['utf-8', 'gbk', 'iso-8859-1']
            for encoding in encodings:
                try:
                    df = pd.read_csv(file_path, encoding=encoding)
                    break
                except UnicodeDecodeError:
                    continue
            else:
                print(f"无法读取文件 {filename}，请检查文件编码。")
                continue
            
            # 检查是否有足够的列
            if len(df.columns) < 5:
                print(f"文件 {filename} 的列数不足5列，跳过处理。")
                continue
            
            # 将第一列和第二列的内容更改为其中的整数值
            df[df.columns[0]] = df[df.columns[0]].apply(extract_integer)
            df[df.columns[1]] = df[df.columns[1]].apply(extract_integer)
            
            # 将第四列的列名改为 pass_code
            df.rename(columns={df.columns[3]: 'pass_code'}, inplace=True)
            
            # 将第五列的列名改为 pass_tc
            df.rename(columns={df.columns[4]: 'pass_tc'}, inplace=True)
            
            # 删除第三列
            df.drop(columns=[df.columns[2]], inplace=True)
            
            # 保存处理后的文件
            df.to_csv(file_path, index=False, encoding='utf-8')
            print(f"文件 {filename} 处理完成并保存。")

if __name__ == '__main__':
    folder_path = '/Se-liuxiangyue/lxy/EECGB/log_results_process/csv - test/humanevalcodegen2b1'  # 替换为你的文件夹路径
    process_csv_files(folder_path)