import os
import shutil

def delete_folder_contents(folder_path):
    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        print(f"指定的文件夹 {folder_path} 不存在。")
        return
    
    # 遍历文件夹中的所有内容
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        
        # 如果是文件，删除文件
        if os.path.isfile(item_path):
            os.remove(item_path)
            print(f"已删除文件: {item_path}")
        
        # 如果是文件夹，递归删除文件夹及其内容
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f"已删除文件夹: {item_path}")

# 使用示例
folder_path = "./示例文件夹"  # 替换为你的文件夹路径
delete_folder_contents(folder_path)
