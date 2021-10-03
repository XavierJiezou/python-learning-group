<h1>【Python】王者荣耀全英雄头像下载</h1>
<h2>文章目录</h2>

[toc]

## 项目需求
#### 基本需求
编写 Python 爬虫脚本实现王者荣耀全英雄头像批量下载。
- 请在 `wz.py` 中书写你的所有代码
- 英雄头像的命名方式为：`英雄名.jpg`，如：`赵云.jpg`
- 将下载的所有英雄头像保存在一个名为 `heros` 的文件夹

**温馨提示**：所有英雄头像均可从王者荣耀官网 [https://pvp.qq.com/](https://pvp.qq.com/) 获取
#### 进阶需求
你能用多线程方式实现吗？（多线程下载可以极大地提高下载速度）
## 环境配置
#### 软件环境
- Python（运行环境：[点击下载](http://npm.taobao.org/mirrors/python/3.9.7/python-3.9.7-amd64.exe)）
- Vscode（代码编辑：[点击下载](https://vscode.cdn.azure.cn/stable/b4c1bd0a9b03c749ea011b06c6d2676c8091a70c/VSCodeUserSetup-x64-1.57.0.exe)）

**温馨提示**：Python 安装时请务必勾选 `Add Python 3.9.7 to PATH` 选项。（该选项将 Python 添加进环境变量，方便调用）；Vscode 中可安装 Python 拓展插件，该插件提供代码联想。
#### 依赖模块
项目开发所需 Python 依赖包如下：

- [os](https://docs.python.org/3/library/os.html)：用于文件或目录操作，执行系统命令等。
- [tqdm](https://tqdm.github.io/)：实现进度条打印。
- [requests](https://docs.python-requests.org/en/master/index.html)：向目标服务器或网址发起请求，并接收响应。
- [beautifulsoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)：网页元素定位和解析。
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)：实现多进程和多线程。

**温馨提示**：`os` 和 `concurrent.futures` 是 Python 内置标准库，无需安装。其它库可打开 `cmd` 或 终端，输入命令 `pip install 库名` 安装。此外，上述提到的库并非所有的都需要用上。
## 预备知识
Python 语言程序设计基础（可观看北理工嵩天教授的教学视频：[点击跳转](https://www.bilibili.com/video/BV1q7411v7HP)）
## 成果展示
![demo](demo.gif)