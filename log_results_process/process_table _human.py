import os
import pandas as pd

def read_excel_first_column(excel_path):
    # 读取Excel文件的第一列
    excel_df = pd.read_excel(excel_path)
    return excel_df.iloc[:, 0].tolist()

def process_csv_files(folder_path, excel_first_column):
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
            
            # 创建一个新的DataFrame来存储处理后的数据
            new_df = pd.DataFrame()
            new_df[df.columns[0]] = excel_first_column  # 替换第一列
            
            # 初始化第2列和第3列（如果有第3列）
            if len(df.columns) >= 3:
                new_df[df.columns[1]] = None
                new_df[df.columns[2]] = None
            else:
                new_df[df.columns[1]] = None
            
            # 处理第2列和第3列（如果有第3列）
            for i, row in df.iterrows():
                if row[0] in excel_first_column:
                    index = excel_first_column.index(row[0])
                    new_df.at[index, df.columns[1]] = row[1]
                    if len(df.columns) >= 3:
                        new_df.at[index, df.columns[2]] = row[2]
            
            # 保存处理后的文件
            new_df.to_csv(file_path, index=False)
            print(f"文件 {filename} 处理完成并保存。")

if __name__ == '__main__':
    folder_path = '/Se-liuxiangyue/lxy/EECGB/swaptestcaselog/human-swap'  # 替换为你的文件夹路径
    excel_path = './humanpluscc.xlsx'  # 替换为你的Excel文件路径
    excel_first_column = read_excel_first_column(excel_path)
    process_csv_files(folder_path, excel_first_column)