# 导入库
# -*- coding: utf-8 -*-
'''
new Env('lishijie自动签到');
cron "0 18 * * *" script-path=lishijie_check.py
'''

import requests
import json
import re
import os
import time

#test
# URL常量
website = "https://www.lishijie.me"
coinPath = "/user/coin"
loginPath = "/wp-admin/admin-ajax.php"
loginAction = "user_login"
checkAction = "user_qiandao"
UserAgent = {
                'User-Agent':
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/99.0.4844.84 Safari/537.36'
             }

# 配置文件
configPath = 'config.json'  # 用户登录信息文件
configEncod = 'utf-8'  # 用户登录信息文件字符集
# 日志文件
logsPath = 'logs.txt'

# 日志常量
loginOkFlag = "wordpress"
log_ER = "error"
log_WARN = "warning"
log_INFO = "info"
logsFileStatus = 0  # 日志文件状态


# 创建日志文件
# file:日志文件路径
def createLogsFile(file):
    if not os.access(file, os.F_OK) or os.access(file, os.W_OK):
        open(file, 'w').close()
        logsFileStatus = 1
    else:
        logsFileStatus = 0


# 打印信息并写入日志
# filename:日志文件名
# infotype:信息类类型
# data:信息内容
def printLogsInfo(filename, infotype, data):
    errorInfo = "--错误--:"
    warningInfo = "--注意--:"
    # 打开日志文件
    file = open(filename, 'a')
    if infotype == "info":  # 普通日志
        print(data)  # 打印到终端
        logsInfo = data + "\n"  # 写入日志
    elif infotype == "error":  # 错误
        print(errorInfo + data)
        logsInfo = errorInfo + data + "\n"
    elif infotype == "warning":  # 注意
        print(warningInfo + data)
        logsInfo = warningInfo + data + "\n"
    else:  # 空
        print("\n")
        logsInfo = "\n"
    file.write(logsInfo)  # 写入日志
    file.close()  # 关闭日志文件


# 读取并检查json
# file:json文件
# encoding:字符编码
# dictInfo:字典
def Json2Dict(file, encoding):
    with open(file, encoding=encoding) as jsonFile:
        try:  # 尝试读取文件
            dictInfo = json.load(jsonFile)
        except Exception:  # 如果解析异常
            printLogsInfo(logsPath, log_ER, "配置文件格式有误，请检查配置文件！")
            time.sleep(2)
            exit(1)
        else:
            return dictInfo


# 获取登录后数据
# url:登录php链接
# data:post传输的用户信息
# s:登陆后页面数据
def getLogin(url, data, head):
    s = requests.session()
    rs = s.post(url, data=data, headers=head)
    return s


# 读取我的余额
# html:登陆后网页源码
# return:搜索到的余额数据
def getCoin(html):
    # 搜索我的余额标签
    return re.search('<p class="small m-0">当前余额：(.*?)</p>', html, re.S).group(1)


# 主函数
if __name__ == '__main__':
    # 创建日志文件
    createLogsFile(logsPath)
    # 读取签到时间
    localTime = str(time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime()))
    # 写入基本信息到日志
    printLogsInfo(logsPath, log_INFO, "签到时间：" + localTime)
    printLogsInfo(logsPath, log_INFO, "签到中，请稍候......")

    # 读取用户登录信息,优先环境变量，其次配置文件
    #读取环境变量，若变量不存在则返回 默认值 'null'
    userInfoEnv = os.getenv( "LISHIJIE_USER", 'null')
    if userInfoEnv == 'null':
        printLogsInfo(logsPath, log_INFO, "未读取到环境变量'LISHIJIE_USER',使用配置文件")
        userInfo = Json2Dict(configPath, configEncod)
    else:
        userInfo = eval(userInfoEnv)
    # 读取登录和金币url
    loginUrl = website + loginPath
    coinUrl = website + coinPath

    for nickname, values in userInfo.items():
        # 分割线
        printLogsInfo(logsPath, log_INFO, "------------------------------")
        printLogsInfo(logsPath, log_INFO, nickname + "：")
        # 读取信息
        username = values[0]
        password = values[1]
        # 组合信息
        postData = {'username': username,
                    'password': password,
                    'action': loginAction}
        # 登录
        lishijie = getLogin(loginUrl, postData, UserAgent)
        if str(lishijie.cookies).find(loginOkFlag) == -1:  # 搜索返回信息，是否存在登陆成功的关键词
            printLogsInfo(logsPath, log_ER, "登录失败！请检查" + nickname + "用户名密码是否正确！")
            continue
        # 签到
        checkInfo = lishijie.post(loginUrl, data={"action": checkAction}, headers=UserAgent).json()
        if checkInfo["status"] == "0":  # 签到失败
            printLogsInfo(logsPath, log_ER, checkInfo["msg"])
        elif checkInfo["status"] == "1":  # 签到成功
            printLogsInfo(logsPath, log_INFO, checkInfo["msg"])
        # 读取我的余额
        myCoin = getCoin(lishijie.get(coinUrl).text)
        lishijie.close()
        printLogsInfo(logsPath, log_INFO, "余额：" + myCoin + "金币")
    printLogsInfo(logsPath, log_INFO, "\n签到完成！")
