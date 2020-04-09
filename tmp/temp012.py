# 13.15 启动一个WEB浏览器
import webbrowser

webbrowser.open_new_tab('www.piyas.com')
c = webbrowser.get('chrome')
c.open_new_tab('www.baidu.com')
