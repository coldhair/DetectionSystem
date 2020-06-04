import tkinter as tk
import time

# 本程序自动完成文本整理
# 复制文本粘贴后，自动进入到剪贴板


root = tk.Tk()  # 窗口
root.title("获取内容")



# text = tk.Text(root, width=30, height=10)  # 创建text组件
# text.pack()


def getData():

    # # 获取text全部内容并去除内容中的空格,用split将内容以每一行末尾的\n分割成一个列表
    # text_content = (text.get("0.0", "end").replace(" ", "")).split("\n")
    # text_content.pop()  # 列表最后一个元素是空删除它
    # print(text_content)

    while True:
        t1=root.clipboard_get()
        time.sleep(0.5)
        t2=root.clipboard_get()
        if t2 != t1:
            # 获取剪切板中的内容
            txt=t2
            if isinstance(txt,str):
                txt.replace(',','，')
                # 更新 到剪贴板中
                root.clipboard_clear()
                root.clipboard_append(txt)
                root.update()  # now it stays on the clipboard after the window is closed
                print(root.clipboard_get())



button = tk.Button(root, text='确定', command=getData)
button.pack()
text_content = []  # 用来储存每一行内容的列表

# root.withdraw()


root.mainloop()
