打包

`pyrcc4 -py3 resources.qrc -o resources.py`

---

`Pyinstaller` 的使用方法

`pyinstaller main.py -y --windowed --additional-hooks-dir pyi_hooks/ `可以生成分离的应用

`pyinstaller -F main.py`

目标程序都会被默认生成在dist/里

这样可以生成单一应用程序，但生成出来的Gui程序会默认带黑框，(修改Console=False可关闭)
但是可以在黑框中看到console输出信息或错误信息，方便测试。

`pyinstaller xxx.spec` 直接打包spec文件

**pyi-makespec file.py** 似乎可以直接生成spec文件