import datetime
import subprocess
import sys
import time
import configparser
from socket import *
from threading import Thread

server = ''
server_url = ''
server_stopped = True

s1 = "0"
buffsize = 512

config = configparser.ConfigParser()
config.read('config.ini')

java_path = config['Paths']['java_path']
server_core_dir = config['Paths']['server_core_dir']
address = config['Paths']['address']
port = int(config['Paths']['port'])

if not java_path:
    raise FileNotFoundError(f"在{java_path}中找不到java")

if not server_core_dir:
    raise FileNotFoundError(f"在{server_core_dir}中找不到服务器核心")

print('即将启动服务器')


def m(message):
    print('[' + datetime.datetime.now().strftime('%H:%M:%S') + '] : ' + message)


# 向服务器传指令
def c(command):
    global server

    server.stdin.write((command + '\n').encode())
    server.stdin.flush()


def start_server():
    global server
    global server_stopped

    if server_stopped:
        m('Starting server...')
        server = subprocess.Popen(
            'java -jar ./server/paper-1.20.1-196.jar',
            stdin=subprocess.PIPE, shell=True)
        server_stopped = False


def stop_server():
    global server
    global server_stopped

    m('正在关闭服务器...')
    c('stop')
    time.sleep(10)
    server.kill()
    server_stopped = True
    time.sleep(10)


# 执行指令
def execute(s):
    m('连接成功')
    s1 = "1"
    while True:
        try:
            recvdata = s.recv(buffsize).decode('utf-8')
            if recvdata.split('=')[0] == '/msg':
                rec_cut = recvdata.split('=')[1]
                if rec_cut.startswith('/'):
                    c(rec_cut)
                else:
                    c('/say debuging...')
                    time.sleep(2)
                    c("/say Done.")
        except:
            m('出问题了断开客户端')
            time.sleep(1)
            connect()
            return


# 建立连接
def connect():
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((address, port))
        execute(s)
    except:
        m('连接失败 将在一秒后重连')
        time.sleep(1)
        connect()


def task1():
    try:
        while True:
            try:
                text = input()
                text = text.lower()
                if text.startswith('/'):
                    c(text)
                else:
                    c('/say ' + text)
            except:
                return
    except:
        text = ""


##################


while True:
    try:
        m("准备开始!")
        start_server()
        t1 = Thread(target=task1)
        t1.start()
        if s1 == "0":
            connect()
    except KeyboardInterrupt:
        stop_server()
        m('Exiting...')
        sys.exit(0)

# ===============================
