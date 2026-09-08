import os
import glob
import pandas as pd

def merge_to_multiple_sheets(folder_path, output_file="合并结果.xlsx", skip_rows=0):
    """
    将指定文件夹下所有Excel文件合并为一个文件，每个源文件对应一个独立的工作表(Sheet)。
    """
    search_pattern = os.path.join(folder_path, "*.xlsx")
    files = glob.glob(search_pattern)
    
    if not files:
        print(f"错误：在 {folder_path} 目录下未找到任何 .xlsx 文件！")
        return

    print(f"找到 {len(files)} 个文件，开始合并...")

    # 【核心】使用 ExcelWriter 作为上下文管理器，确保所有Sheet写入同一个文件
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        success_count = 0
        for file in files:
            try:
                # 读取Excel，支持跳过前N行
                df = pd.read_excel(file, engine='openpyxl', skiprows=skip_rows)
                
                # 提取文件名（不含后缀）作为 Sheet 名称
                # Excel 对 Sheet 名称有长度和字符限制，这里做简单的截断处理
                sheet_name = os.path.basename(file).replace(".xlsx", "")[:31] 
                
                # 将数据写入到指定的 Sheet 中，index=False 表示不写入行索引
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                
                success_count += 1
                print(f"✅ 成功写入 Sheet: {sheet_name} ({len(df)} 行)")
            except Exception as e:
                print(f"❌ 处理失败: {os.path.basename(file)}，原因: {e}")

    print(f"\n🎉 合并完成！共成功写入 {success_count} 个工作表。")
    print(f"📁 结果已保存至: {os.path.abspath(output_file)}")

# ==================== 使用示例 ====================
if __name__ == "__main__":
    merge_to_multiple_sheets(
        folder_path="你的Excel文件夹路径",  # 替换为你的文件夹路径
        output_file="年度多表汇总.xlsx",   # 替换为你想要的输出文件名
        skip_rows=1                        # 如果数据从第二行开始，这里填 1
    )