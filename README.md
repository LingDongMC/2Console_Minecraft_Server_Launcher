# 2Console_Minecraft_Server_Launcher
‘’'JSON
注意：本启动器不适合新手服主使用
'''

如果你是新手服主，请上b站搜索更方便的开服方法 如灵工艺开服器 MCSM MCSL2 WeMC , etc.
[点此](https://search.bilibili.com/all?keyword=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C%E5%BC%80%E6%9C%8D%E5%99%A8)
# 服务器内管理员可以有很多个，但至高无上的Console权限只有一个
## 现在不是了！

在要开服的电脑上运行MainConsole.py
在要开第二控制台的电脑上运行ExtraConsole.py

在config.ini里修改配置
java_path = java 此处填写指定Java路径 如:C:\Program Files\BellSoft\jdk-17.0.5-lite\bin\java.exe 注意不要加引号 填写java则是使用系统默认JAVA_HOME环境变量的那个java

server_core_dir = ./server/paper-1.20.1-196.jar 此处填写服务器核心路径 记得改成自己的！

address = 127.0.0.1 第二控制台的ip地址 默认是本机 即同一台电脑 如果不在局域网中 您可能需要内网穿透软件

port = 5000 第二控制台的端口号

‘’‘JSON
不得将上述内容用于商业或非法用途，否则一切后果请用户自行承担
'''

建议先启动ExtraConsole，再启动MainConsole 否则可能会连不上(这是2022年初期版本测试时的问题 现在似乎不限顺序)