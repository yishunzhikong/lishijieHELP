<div align="center"> 
<h1 align="center">lishijie签到青龙版</h1>
</div>

![GitHub stars](https://img.shields.io/github/stars/yishunzhikong/lishijieHELP?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/yishunzhikong/lishijieHELP?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/yishunzhikong/lishijieHELP?style=flat-square)
![GitHub issues](https://img.shields.io/github/languages/code-size/yishunzhikong/lishijieHELP?style=flat-square)

# 一个运行在青龙的签到函数

[青龙](https://github.com/whyour/qinglong.git)

## 特别声明

- 本仓库发布的脚本及其中涉及的任何解锁和解密分析脚本，仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。
- 本项目内所有资源文件，禁止任何公众号、自媒体进行任何形式的转载、发布。
- 本人对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害。
- 间接使用脚本的任何用户，包括但不限于建立VPS或在某些行为违反国家/地区法律或相关法规的情况下进行传播, 本人对于由此引起的任何隐私泄漏或其他后果概不负责。
- 请勿将本仓库的任何内容用于商业或非法目的，否则后果自负。
- 如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
- 任何以任何方式查看此项目的人或直接或间接使用该项目的任何脚本的使用者都应仔细阅读此声明。本人保留随时更改或补充此免责声明的权利。一旦使用并复制了任何相关脚本或Script项目的规则，则视为您已接受此免责声明。

**您必须在下载后的24小时内从计算机或手机中完全删除以上内容**

> ***您使用或者复制了本仓库且本人制作的任何脚本，则视为 `已接受` 此声明，请仔细阅读***

## 环境依赖

脚本用python编写，用到`requests`、`json`、`re`、`os`、`time`几个库，请确认已安装

## 使用方法

**进入容器后运行以下命令**（docker exec -it ql bash）修改ql为你的青龙容器名字

以下命令全部都是**进入容器**后输入

### 1.拉取仓库

```
ql repo https://github.com/yishunzhikong/lishijieHELP.git
```

### 2.添加配置信息

本脚配置采用**环境变量**(优先)和[**json文件**](https://www.runoob.com/json/json-syntax.html)两种方式，两种配置方式内容格式均相同。

配置格式：

```json
{
	"username_1": ["useremail_1", "password_1"],
	"username_2": ["useremail_2", "password_2"]
}
```

其中：
  - `username` ：用户昵称，可自定义，不可重复，若重复，则以最后一个为准
  - `useremail` ：lishijie用户登录邮箱
  - `password` ：lishijie用户登录密码

#### 1.环境变量模式

运行一下命令

旧版(青龙v2.12以下)
```shell
export \
"{ \
	"username_1": ["useremail_1", "password_1"], \
	"username_2": ["useremail_2", "password_2"] \
}" \
>> ql/config/env.sh
```

新版
```shell
export \
"{ \
	"username_1": ["useremail_1", "password_1"], \
	"username_2": ["useremail_2", "password_2"] \
}" \
>> ql/data/config/env.sh
```

#### 2.配置文件模式

### 2.运行以下命令

旧版(青龙v2.12以下)

```shell
cd /ql/repo/lishijieHELP && python3 lishijie_check.py
```

新版

```shell
cd /ql/data/repo/lishijieHELP && python3 lishijie_check.py
```

### 3.说明

1.本仓库在12.21日的更新中同时支持了json和toml两种格式的配置文件，但是推荐使用toml格式配置文件

2.当toml和json配置文件共存时优先使用toml文件

3.为避免未设置的签到项目推送，请禁止该签到任务，或注释掉配置文件中关于这个任务的配置项目

4.在运行修改运行时间后若出现未知错误

**请先确认database.sqlite.back或crontab.db.back是否存在**,然后

```
cd /ql/data/db/ && rm database.sqlite && cp database.sqlite.back database.sqlite #v2.12+
```

```
cd /ql/db/ && rm database.sqlite && cp database.sqlite.back database.sqlite #v2.11+
```

```
cd /ql/db/ && rm crontab.db && cp crontab.db.back crontab.db #v2.11-
```

### 4.**更新支持了多账号**

toml配置方式

```toml
[[ACFUN]]
password = "Sitoi"
phone = "188xxxxxxxx"

[[ACFUN]]
password = "123456"
phone = "135xxxxxxxx"
```

json配置方式

```json
  "ACFUN" : [
    {
    "password": "Sitoi",
    "phone": "18888xxxxxx"
    },
{
"password": "多账号 密码填写，请参考上面",
"phone": "多账号 手机号填写，请参考上面"
}
],
```

### 5.通知配置

来自于青龙的config.sh

**在2022.4.10更新接入消息推送APP**

环境变量为设置别名的内容

```shell
export MI_PUSH_ALIAS="********"
```

## 其他

#### 1.关于 toml 的语法参考：

* [toml-lang/toml](https://github.com/toml-lang/toml)
* [中文知乎介绍](https://zhuanlan.zhihu.com/p/50412485)
* [TOML 教程中文版](https://toml.io/cn/v1.0.0)

#### 2.排错指引

1.在sitoi/dailycheckin的某次更新中修改了键名，请尽量删除原配置文件后重新配置

2.本库找配置文件时使用了正则表达式,在最外层配置时可以不区分大小写，且只要包含字段就可以，甚至可以写中文(强烈不建议这么写,貌似toml不支持)

3.很多脚本并没有测试

## 致谢

[@Wenmoux](https://github.com/Wenmoux/)

[@Sitoi](https://github.com/Sitoi)

[@Oreomeow](https://github.com/Oreomeow)

## Stargazers over time

[![Stargazers over time](https://starchart.cc/yuxian158/check.svg)](https://starchart.cc/yuxian158/check)
