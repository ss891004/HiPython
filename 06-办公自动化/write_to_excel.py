import os
import pandas as pd
from shutil import copyfile
from openpyxl import load_workbook

# ========== 配置参数 ==========
INPUT_EXCEL = 'data.xlsx'          # 原始数据文件路径
TEMPLATE_FILE = 'template.xlsx'    # 模板文件路径（必须存在）
OUTPUT_DIR = 'output'              # 输出目录
GROUP_COLUMN = '部门'               # 用于分组的列名
SHEET_NAME = 'Sheet1'              # 模板中要写入的工作表名
START_ROW = 2                      # 数据从第几行开始写入（1为标题行）
START_COL = 1                      # 从第几列开始写入（A列为1）

# ========== 创建输出目录 ==========
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ========== 读取原始数据 ==========
df = pd.read_excel(INPUT_EXCEL)

if GROUP_COLUMN not in df.columns:
    raise ValueError(f"错误：原始数据中不存在列 '{GROUP_COLUMN}'")

# 确保列顺序固定（可选）
columns_to_write = df.columns.tolist()

# ========== 按指定列分组处理 ==========
for group_value, group_df in df.groupby(GROUP_COLUMN):
    # 安全化文件名（避免非法字符）
    safe_group = str(group_value).strip()
    safe_name = "".join(c if c.isalnum() or c in (' ', '-', '_', '.') else '_' for c in safe_group)
    output_path = os.path.join(OUTPUT_DIR, f"{safe_name}_output.xlsx")
    
    # 复制模板（保留所有格式）
    copyfile(TEMPLATE_FILE, output_path)
    
    # 加载副本进行写入
    wb = load_workbook(output_path)
    if SHEET_NAME not in wb.sheetnames:
        raise ValueError(f"模板中不存在工作表 '{SHEET_NAME}'")
    ws = wb[SHEET_NAME]
    
    # 可选：清空原有数据区域（从 START_ROW 开始往下）
    # 如果你希望追加而不是覆盖，可跳过此步；这里默认覆盖写入区域
    max_row = ws.max_row
    if max_row >= START_ROW:
        for row in range(START_ROW, max_row + 1):
            for col in range(START_COL, len(columns_to_write) + START_COL):
                ws.cell(row=row, column=col).value = None
    
    # 写入新数据
    current_row = START_ROW
    for _, row_data in group_df.iterrows():
        for col_offset, col_name in enumerate(columns_to_write):
            cell_value = row_data[col_name]
            # 处理 NaN（pandas 中的空值）
            if pd.isna(cell_value):
                cell_value = None
            ws.cell(row=current_row, column=START_COL + col_offset, value=cell_value)
        current_row += 1
    
    # 保存文件
    wb.save(output_path)
    wb.close()
    
    print(f"✅ 已生成: {output_path}")

print("🎉 所有文件处理完成！")