<h1>【Python】使用蒙特卡罗方法计算圆周率 π 的值</h1>
<h2>文章目录</h2>

[toc]

## 项目需求
#### 基本需求
编写 Python 代码实现蒙特卡罗方法计算圆周率 π 的值。
- 请在 `pi.py` 中书写你的所有代码
- 限定蒙特卡罗方法的总试验次数为 $10^6$

#### 进阶需求
你能用多进程方式实现吗？（多进程可以极大地提高计算速度）
## 环境配置
#### 软件环境
- Python（运行环境：[点击下载](http://npm.taobao.org/mirrors/python/3.9.7/python-3.9.7-amd64.exe)）
- Vscode（代码编辑：[点击下载](https://vscode.cdn.azure.cn/stable/b4c1bd0a9b03c749ea011b06c6d2676c8091a70c/VSCodeUserSetup-x64-1.57.0.exe)）

**温馨提示**：Python 安装时请务必勾选 `Add Python 3.9.7 to PATH` 选项。（该选项将 Python 添加进环境变量，方便调用）；Vscode 中可安装 Python 拓展插件，该插件提供代码联想。
#### 依赖模块
项目开发所需 Python 依赖包如下：

- [tqdm](https://tqdm.github.io/)：实现进度条打印。
- [random](https://docs.python.org/3/library/random.html)：生成随机数。
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)：实现多进程和多线程。

**温馨提示**：`random` 和 `concurrent.futures` 是 Python 内置标准库，无需安装。其它库可打开 `cmd` 或 终端，输入命令 `pip install 库名` 安装。
## 预备知识
Python 语言程序设计基础（可观看北理工嵩天教授的教学视频：[点击跳转](https://www.bilibili.com/video/BV1q7411v7HP)）
## 蒙特卡罗
![在这里插入图片描述](https://img-blog.csdnimg.cn/0d9f5653a3304371915897f1d0df63fa.png?x-oss-process=image,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyOTUxNTYw,size_16,color_FFFFFF,t_70#pic_center)
1×1 的正方形里面有一个内切圆。向该正方形区域内随机散点（散点总数记为 S），对于每一个点，其落在圆内的概率是：$\frac {\pi \cdot 0.5^2}{1×1}=0.25\pi$，散点结束后，统计其落在圆内的点数，并记为 N。

一般来说，随着实验次数的增多，频率会接近于概率。当实验次数趋向于无穷时，频率的极限就是概率。

因此，当 S 足够大时，我们可以简单认为：$0.25\pi=\frac{N}{S}$，即$\pi=\frac{4N}{S}$

**温馨提示**：如何判断点在圆内？计算点到圆心的欧式距离，比半径小就在圆内，比半径大就在圆外。