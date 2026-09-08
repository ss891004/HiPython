import os
import pandas as pd

# 读取总表 -> 按指定列分组 (groupby) -> 遍历每个分组并导出为独立的 Excel 文件 (to_excel)。
def split_excel_by_column(input_file, split_column, output_dir="拆分结果"):
    """
    按指定列的值将 Excel 总表拆分为多个独立文件，并以该列的值命名。
    """
    # 1. 检查文件是否存在
    if not os.path.exists(input_file):
        print(f"错误：文件 {input_file} 不存在！")
        return

    # 2. 读取 Excel 文件
    df = pd.read_excel(input_file, engine='openpyxl')
    print(f"成功读取总表，共 {len(df)} 行数据。")

    # 3. 检查拆分列是否存在
    if split_column not in df.columns:
        print(f"错误：列名 '{split_column}' 不存在！可用的列有：{list(df.columns)}")
        return

    # 4. 创建输出文件夹（如果不存在）
    os.makedirs(output_dir, exist_ok=True)

    # 5. 按指定列分组并遍历导出
    grouped = df.groupby(split_column)

    # 将两列拼接成一个新的组合键
    # df['组合键'] = df['部门'] + '_' + df['城市']
    # grouped = df.groupby('组合键')


    for group_name, group_df in grouped:
        # 清理文件名中的非法字符（Windows 文件名不允许 \ / : * ? " < > |）
        safe_name = str(group_name).replace('/', '_').replace('\\', '_') \
                                   .replace(':', '_').replace('*', '') \
                                   .replace('?', '').replace('"', '') \
                                   .replace('<', '').replace('>', '').replace('|', '_')
        
        # 拼接输出文件路径
        output_file = os.path.join(output_dir, f"{safe_name}.xlsx")
        
        # 导出为 Excel 文件，index=False 表示不写入行索引
        group_df.to_excel(output_file, index=False, engine='openpyxl')
        print(f"已拆分并保存: {safe_name}.xlsx (共 {len(group_df)} 行)")

    print(f"\n拆分完成！所有文件已保存在: {os.path.abspath(output_dir)}")

# ==================== 使用示例 ====================
if __name__ == "__main__":
    split_excel_by_column(
        input_file="员工花名册总表.xlsx",  # 你的原始 Excel 文件名
        split_column="部门",               # 你想按照哪一列进行拆分
        output_dir="按部门拆分结果"         # 拆分后文件保存的文件夹名称
    )