import re
import csv


def parse_log_for_coverage(log_text):
    # 正则表达式用于提取文件名和覆盖率信息
    pattern = re.compile(r'(\S+\.py)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+%)')

    coverage_info = {}
    in_coverage_section = False

    for line in log_text.splitlines():
        if '---------- coverage:' in line:
            in_coverage_section = True
            continue
        if in_coverage_section and line.strip() == '':
            in_coverage_section = False
            continue
        if in_coverage_section:
            match = pattern.match(line)
            if match:
                file, stmts, miss, branch, brpart, cover = match.groups()
                coverage_info[file] = {
                    'Statements': stmts,
                    'Miss': miss,
                    'Branch': branch,
                    'BrPart': brpart,
                    'Cover': cover
                }

    return coverage_info


def read_log_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_coverage_to_csv(coverage_info, csv_file_path):
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['File', 'Statements', 'Miss', 'Branch', 'BrPart', 'Cover']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for file, info in coverage_info.items():
            row = {'File': file}
            row.update(info)
            writer.writerow(row)


def main():
    # 文件路径
    log_file_path = 'coverage.log'  # 修改为实际的日志文件路径
    csv_file_path = 'coverage.csv'  # 修改为要保存的CSV文件路径

    # 读取日志文件
    log_text = read_log_file(log_file_path)

    # 解析日志中的覆盖率信息
    coverage_info = parse_log_for_coverage(log_text)

    # 将覆盖率信息写入CSV文件
    write_coverage_to_csv(coverage_info, csv_file_path)


if __name__ == "__main__":
    main()
