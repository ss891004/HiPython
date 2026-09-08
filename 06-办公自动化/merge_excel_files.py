import os
import glob
import pandas as pd

def merge_excel_files(folder_path, output_file="合并结果.xlsx", skip_rows=1):
    """
    将指定文件夹下所有结构相同的Excel文件合并为一个文件。
    支持跳过表头前的说明行或标题行。
    """
    search_pattern = os.path.join(folder_path, "*.xlsx")
    files = glob.glob(search_pattern)
    
    if not files:
        print(f"错误：在 {folder_path} 目录下未找到任何 .xlsx 文件！")
        return

    print(f"找到 {len(files)} 个文件，开始合并...")
    all_data = []

    for file in files:
        try:
            # 【核心修改】skiprows=skip_rows 表示跳过文件的前 N 行
            # 假设数据从第二行开始，表头在第二行，则 skip_rows=1
            df = pd.read_excel(file, engine='openpyxl', skiprows=skip_rows)
            
            # 添加来源文件列，方便后续数据溯源
            df.insert(0, "来源文件", os.path.basename(file))
            
            all_data.append(df)
            print(f"✅ 成功读取: {os.path.basename(file)} ({len(df)} 行)")
        except Exception as e:
            print(f"❌ 读取失败: {os.path.basename(file)}，原因: {e}")

    if not all_data:
        print("没有成功读取到任何有效数据！")
        return

    # 纵向拼接所有 DataFrame，ignore_index=True 重置行索引
    result = pd.concat(all_data, ignore_index=True)

    # 导出为新的 Excel 文件
    result.to_excel(output_file, index=False, engine='openpyxl')
    print(f"\n🎉 合并完成！共合并 {len(files)} 个文件，总计 {len(result)} 行数据。")
    print(f"📁 结果已保存至: {os.path.abspath(output_file)}")

# ==================== 使用示例 ====================
if __name__ == "__main__":
    merge_excel_files(
        folder_path="你的Excel文件夹路径",
        output_file="年度销售汇总表.xlsx",
        skip_rows=1  # 【关键配置】如果真正的表头在第2行，这里填 1；如果在第3行，填 2
    )