import subprocess
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os

def handle_filepath(filepath):
    """处理文件路径中的斜杠，统一转换为反斜杠"""
    if "/" in filepath:
        filepath = filepath.replace("/", "\\")
        print(filepath)
    return filepath

def cmd_filepath(filepath):
    """生成以管理员权限运行文件的PowerShell命令"""
    filepath = handle_filepath(filepath)
    command = f'powershell -Command "Start-Process \'{filepath}\' -Verb runAs"'
    print(command)
    return command

def run_command(command):
    """执行系统命令"""
    subprocess.run(command, shell=True, capture_output=True, text=True)

def load_config():
    """加载配置文件，如果不存在则创建默认配置"""
    if not os.path.exists('config.info'):
        with open('config.info', 'w') as f:
            f.write('path="apps"')
            os.makedirs("apps", exist_ok=True)
            return "apps"
    else:
        with open('config.info', 'r') as f:
            config_info = f.read()
            path = config_info.split('=')[1].strip().replace('"', '')
            return path

def create_main_window():
    """创建主窗口"""
    root = tk.Tk()
    root.title("SuperStart")
    root.geometry("300x150")
    
    # 设置窗口图标（如果有的话）
    try:
        root.iconbitmap('icon.ico')  # 请确保有icon.ico文件
    except:
        pass
    
    return root

def open_app():
    """打开APP按钮的功能"""
    file_path = filedialog.askopenfilename(title="选择要打开的应用程序")
    if not file_path:
        return
    
    command = cmd_filepath(file_path)
    run_command(command)

def generate_app():
    """生成APP按钮的功能"""
    savepath = load_config()
    
    file_path = filedialog.askopenfilename(title="选择要创建快捷方式的文件")
    if not file_path:
        return
    
    filename = simpledialog.askstring("文件名", "输入快捷方式名称(不要扩展名):")
    if not filename:
        return
    
    command = cmd_filepath(file_path)
    filename = savepath + "/" + filename + ".bat"
    filename = handle_filepath(filename)
    filepath = os.path.join(os.getcwd(), filename)
    
    try:
        with open(filepath, "w") as f:
            f.write(command)
        messagebox.showinfo("成功", f"命令已保存到:\n{filepath}")
    except Exception as e:
        messagebox.showerror("错误", f"保存文件失败:\n{str(e)}")

def main():
    """主函数，创建GUI界面"""
    root = create_main_window()
    
    # 创建按钮框架
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)
    
    # 创建打开APP按钮
    open_button = tk.Button(
        button_frame, 
        text="打开APP", 
        command=open_app,
        width=15,
        height=2,
        bg="#4CAF50",
        fg="white"
    )
    open_button.pack(side=tk.LEFT, padx=10)
    
    # 创建生成APP按钮
    generate_button = tk.Button(
        button_frame, 
        text="生成APP", 
        command=generate_app,
        width=15,
        height=2,
        bg="#2196F3",
        fg="white"
    )
    generate_button.pack(side=tk.LEFT, padx=10)
    
    # 添加说明标签
    info_label = tk.Label(
        root, 
        text="选择功能: 直接打开应用或生成快捷方式",
        font=("Arial", 10)
    )
    info_label.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()