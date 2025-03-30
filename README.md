# 🚀 超级启动器 (SuperStart)

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2F11-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

一个简单实用的Windows应用程序管理工具，专门用于以管理员权限启动应用程序。

## 🖥️ 界面预览
![界面预览](https://github.com/user-attachments/assets/f1839a1c-beed-4d27-8bd0-6ac6c5355428)

## ⚙️ 系统要求

- Windows 10/11
- Python 3.7+
- 管理员权限

## 📦 安装要求

需要安装以下Python包：
```bash
pip install winshell
```

## 📥 安装和运行

### 1. 下载并安装Python
- 访问 [Python官网](https://www.python.org/downloads/) 下载Python 3.7+
- 安装时请勾选"Add Python to PATH"选项

### 2. 安装依赖包
创建requirements.txt并安装依赖：
```bash
pip install -r requirements.txt
```

### 3. 启动程序
方式一：直接运行
```bash
python SuperStart.py
```

方式二：创建快捷方式
- 右键SuperStart.py
- 发送到桌面快捷方式
- 在快捷方式属性中设置"以管理员身份运行"

### 4. 程序依赖
requirements.txt内容：
```
winshell>=0.6
pywin32>=223
```

## ✨ 主要功能

- 将常用需要管理员权限的程序添加为APP
- 支持拖放文件直接以管理员权限运行
- 可以为APP创建桌面或开始菜单快捷方式
- 双击即可运行已添加的APP
- 支持右键菜单快捷操作

### 🎯 高级功能

1. **智能路径处理**：
   - 自动转换正斜杠(/)为反斜杠(\)
   - 支持包含空格的文件路径

2. **配置文件管理**：
   - 自动创建并维护配置文件
   - 支持自定义APP存储位置

3. **界面特性**：
   - 支持拖放操作
   - 右键菜单快捷操作
   - 双击快速启动
   - 美观的GUI界面

## 📖 使用方法

### 🔰 基本操作

1. **生成APP**：
   - 点击"生成APP"按钮
   - 选择需要管理员权限运行的程序
   - 输入APP名称
   - APP将被保存到apps目录

2. **免生成打开APP**：
   - 点击"免生成打开APP"按钮
   - 选择程序直接以管理员权限运行

3. **运行APP**：
   - 双击列表中的APP即可运行
   - 或右键选择"运行"

### 🔗 快捷方式管理

右键点击APP可以：
- 创建桌面快捷方式
- 创建开始菜单快捷方式
- 删除APP

### 🖱️ 拖放功能

直接将文件拖放到程序图标上，即可以管理员权限运行该文件。

## ⚡ 配置说明

程序会自动创建以下文件：
- `config.info`: 存储APP保存位置
- `apps`文件夹: 默认的APP存储目录

## 🎨 美化说明

### 🖼️ 程序图标
可以替换 `icon.ico` 文件来自定义程序图标。推荐图标尺寸：
- 32x32 像素
- 48x48 像素
- 256x256 像素

### 🌈 按钮图标
在生成的快捷方式中，程序会自动使用目标程序的图标。

### 🎯 推荐图标资源
- [Icons8](https://icons8.com/) - 免费图标库
- [Flaticon](https://www.flaticon.com/) - 高质量图标
- [Material Design Icons](https://materialdesignicons.com/) - Google风格图标

## ⚠️ 注意事项

1. **安全提示**：
   - 请确保只为受信任的程序创建管理员权限快捷方式
   - 不建议为未知来源的程序创建快捷方式

2. **路径限制**：
   - 避免在路径中使用特殊字符
   - 建议使用英文路径

3. **快捷方式管理**：
   - 删除APP时不会自动删除已创建的快捷方式
   - 建议手动管理不再使用的快捷方式

## 🔧 故障排除

1. **程序无法启动**：
   - 检查Python环境是否正确安装
   - 确认是否已安装所需的依赖包
   - 验证是否具有管理员权限

2. **快捷方式创建失败**：
   - 确保目标程序路径有效
   - 检查是否有写入权限
   - 确认快捷方式名称不与现有文件冲突

3. **配置文件问题**：
   - 如遇配置文件损坏，可删除`config.info`文件
   - 程序将自动创建新的配置文件

## 💻 开发说明

### 📁 项目结构
```
SuperStart/
│  SuperStart.py    # 主程序
│  config.info      # 配置文件
│  icon.ico         # 程序图标
│  README.md        # 说明文档
└─apps/            # APP存储目录
```

### 📚 主要模块依赖
- tkinter: GUI界面
- winshell: 快捷方式管理
- subprocess: 进程控制
- argparse: 命令行参数处理

### 🤝 贡献指南
1. Fork 项目
2. 创建新的分支
3. 提交更改
4. 发起 Pull Request

## 📄 License

MIT License
