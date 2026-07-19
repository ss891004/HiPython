import os
import time
import win32com.client

def batch_print_word(folder_path):
    """
    批量打印指定文件夹下的所有 Word 文档
    """
    # 确保路径存在
    if not os.path.exists(folder_path):
        print(f"❌ 错误：找不到文件夹 {folder_path}")
        return

    # 1. 在后台启动 Word 应用程序
    # 注意：这里使用 Dispatch 启动 Word
    word = win32com.client.Dispatch("Word.Application")
    
    # 核心设置：让 Word 在后台静默运行，不弹窗
    word.Visible = False
    # 关闭所有警告和提示弹窗，防止打印时卡住
    word.DisplayAlerts = False 
    # 将 ActivePrinter 设置为你电脑里实际的打印机名称
    word.ActivePrinter = "HP LaserJet Pro M404n"

    print("🚀 Word 后台已启动，开始扫描文件...")
    
    # 2. 获取文件夹下所有的 .docx 文件
    # 如果需要处理旧版的 .doc 文件，可以在这里加上
    files = [f for f in os.listdir(folder_path) if f.lower().endswith('.docx','.doc')]
    
    if not files:
        print("⚠️ 文件夹中没有找到 .docx 文件。")
        word.Quit()
        return

    print(f"📂 共找到 {len(files)} 个文件，开始打印任务：")

    # 3. 遍历文件并打印
    for i, filename in enumerate(files, 1):
        file_path = os.path.join(folder_path, filename)
        print(f"[{i}/{len(files)}] 正在处理：{filename} ...")
        
        try:
            # 打开文档
            doc = word.Documents.Open(file_path)
            
            # 执行打印操作（发送到系统默认打印机）
            #doc.PrintOut()

            doc.PrintOut(Copies=2) # 打印2份
            
            # 打印指令发出后，关闭文档且不保存任何修改
            doc.Close(SaveChanges=0)
            
            print(f"   ✅ {filename} 已发送至打印机")
            
            # 稍微停顿一下（比如 1 秒），防止文件太多导致打印队列堵塞或 Word 崩溃
            time.sleep(1)
            
        except Exception as e:
            print(f"   ❌ 打印 {filename} 时出错：{e}")

    # 4. 全部处理完毕后，彻底退出 Word 程序
    word.Quit()
    print("🎉 批量打印任务全部完成！")

# ================= 运行配置 =================
if __name__ == "__main__":
    # 把这里的路径换成你存放 Word 文件的实际文件夹路径
    # 注意：路径中的斜杠最好用双反斜杠 \\ 或者在字符串前面加 r
    target_folder = r"D:\你的文件夹路径\Word文件" 

    # pip install win32
    
    batch_print_word(target_folder)