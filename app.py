import subprocess
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, ttk
import os

def handle_filepath(filepath):
    """处理文件路径中的斜杠，统一转换为反斜杠"""
    if "/" in filepath:
        filepath = filepath.replace("/", "\\")
    return filepath

def cmd_filepath(filepath):
    """生成以管理员权限运行文件的PowerShell命令"""
    filepath = handle_filepath(filepath)
    command = f'powershell -Command "Start-Process \'{filepath}\' -Verb runAs"'
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

def get_app_list():
    """获取apps文件夹下的所有批处理文件"""
    apps_dir = load_config()
    if not os.path.exists(apps_dir):
        return []
    
    app_files = [f for f in os.listdir(apps_dir) if f.endswith('.bat')]
    return app_files

def create_main_window():
    """创建主窗口"""
    root = tk.Tk()
    root.title("快捷方式生成器")
    root.geometry("500x400")
    
    try:
        root.iconbitmap('icon.ico')
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
    filename = os.path.join(savepath, filename + ".bat")
    filename = handle_filepath(filename)
    
    try:
        with open(filename, "w") as f:
            f.write(command)
        messagebox.showinfo("成功", f"命令已保存到:\n{filename}")
        refresh_app_list()  # 刷新列表
    except Exception as e:
        messagebox.showerror("错误", f"保存文件失败:\n{str(e)}")

def run_selected_app(event=None):
    """运行选中的APP"""
    selected_item = app_listbox.selection()  # 使用selection()而不是focus()
    if not selected_item:
        messagebox.showwarning("警告", "请先选择一个APP")
        return
    
    item_text = app_listbox.item(selected_item)['values'][0]
    apps_dir = load_config()
    app_path = os.path.join(apps_dir, item_text)
    
    try:
        subprocess.run(app_path, shell=True)
    except Exception as e:
        messagebox.showerror("错误", f"运行APP失败:\n{str(e)}")

def delete_selected_app(event=None):
    """删除选中的APP"""
    selected_item = app_listbox.selection()  # 使用selection()而不是focus()
    if not selected_item:
        messagebox.showwarning("警告", "请先选择一个APP")
        return
    
    item_text = app_listbox.item(selected_item)['values'][0]
    apps_dir = load_config()
    app_path = os.path.join(apps_dir, item_text)
    
    try:
        os.remove(app_path)
        refresh_app_list()  # 刷新列表
        messagebox.showinfo("成功", f"已删除: {item_text}")
    except Exception as e:
        messagebox.showerror("错误", f"删除APP失败:\n{str(e)}")

def show_context_menu(event):
    """显示右键菜单"""
    # 获取鼠标位置下的项目
    item = app_listbox.identify_row(event.y)
    if item:
        # 选中该项目
        app_listbox.selection_set(item)
        
        # 创建菜单
        menu = tk.Menu(root, tearoff=0)
        menu.add_command(label="运行", command=run_selected_app)
        menu.add_command(label="删除", command=delete_selected_app)
        
        # 显示菜单
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()

def refresh_app_list():
    """刷新APP列表"""
    # 清空现有列表
    for item in app_listbox.get_children():
        app_listbox.delete(item)
    
    # 重新加载APP列表
    app_files = get_app_list()
    for i, app in enumerate(app_files, 1):
        app_listbox.insert("", "end", values=(app,), tags=(f'row{i}',))

def main():
    """主函数，创建GUI界面"""
    global app_listbox, root
    
    root = create_main_window()
    
    # 主框架
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # 按钮框架
    button_frame = tk.Frame(main_frame)
    button_frame.pack(fill=tk.X, pady=5)
    
    # 创建按钮
    generate_button = tk.Button(
        button_frame, 
        text="生成APP", 
        command=generate_app,
        width=15,
        height=1,
        bg="#2196F3",
        fg="white"
    )
    generate_button.pack(side=tk.LEFT, padx=5)


    open_button = tk.Button(
        button_frame, 
        text="免生成打开APP", 
        command=open_app,
        width=15,
        height=1,
        bg="#4CAF50",
        fg="white"
    )
    open_button.pack(side=tk.LEFT, padx=5)
    
    # APP列表框架
    list_frame = tk.Frame(main_frame)
    list_frame.pack(fill=tk.BOTH, expand=True, pady=10)
    
    # 列表标题
    list_label = tk.Label(list_frame, text="Apps:", font=("Arial", 10, "bold"))
    list_label.pack(anchor=tk.W)
    
    # 创建Treeview列表
    app_listbox = ttk.Treeview(list_frame, columns=("app",), show="headings", height=10)
    # app_listbox.heading("app", text="AppName")
    # app_listbox.column("app", width=450, anchor=tk.W)
    
    # 添加滚动条
    scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=app_listbox.yview)
    app_listbox.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    app_listbox.pack(fill=tk.BOTH, expand=True)
    
    # 绑定右键菜单事件
    app_listbox.bind("<Button-3>", show_context_menu)
    
    # 绑定双击事件运行APP
    app_listbox.bind("<Double-1>", run_selected_app)
    
    # 初始化列表
    refresh_app_list()
    
    root.mainloop()

if __name__ == "__main__":
    main()