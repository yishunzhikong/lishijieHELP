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

#### 方式1：环境变量

按以下步骤运行命令：

a. 进入青龙配置文件目录

  - 旧版(青龙v2.12以下)

  ```shell
  cd /ql/config
  ```

  - 新版

  ```shell
  cd /ql/data/config
  ```

b. 写入环境变量到青龙环境变量配置文件

  ```shell
  echo \
  "{\
    "username_1": ["useremail_1", "password_1"],\
    "username_2": ["useremail_2", "password_2"]\
  }"\
  >>env.sh
  ```

#### 方式2：配置文件

按以下步骤运行命令：

a. 进入lishijie签到脚本目录

  - 旧版(青龙v2.12以下)

  ```
  cd /ql/repo/lishijieHELP
  ```

  - 新版

  ```
  cd /ql/data/repo/lishijieHELP
  ```

b. 创建并写入配置文件

  ```shell
  touch config.sh && \
  echo \
  "{ \
    "username_1": ["useremail_1", "password_1"],\
    "username_2": ["useremail_2", "password_2"]\
  }"\
  >> config.json
  ```

### 3.运行签到脚本

- 旧版(青龙v2.12以下)

```shell
cd /ql/repo/lishijieHELP && python3 lishijie_check.py
```

- 新版

```shell
cd /ql/data/repo/lishijieHELP && python3 lishijie_check.py
```

### 34.添加定时执行

按以下步骤运行命令：

a. 进入青龙配置文件目录

  - 旧版(青龙v2.12以下)

  ```shell
  cd /ql/config
  ```

  - 新版

  ```shell
  cd /ql/data/config
  ```

b. 写入环境变量到青龙环境变量配置文件

  ```shell
  echo "0 18 * * * ID=1 task lishijieHELP/lishijie_check.py">>crontab.list
  ```

  注意：ID根据实际情况填写

### 5.通知配置

暂时未添加通知功能

### 5.说明

## 其他

#### 1.关于 json 的语法参考：

* [JSON语法-菜鸟教程](https://www.runoob.com/json/json-syntax.html)
* [JSON-维基百科](https://zh.m.wikipedia.org/zh/JSON)
* [JSON-百度百科](https://baike.baidu.com/item/JSON/2462549)
* [JSON中文](https://www.json.org/json-zh.html)

## 致谢

## 随时间的关注趋势

[![随时间的关注趋势](https://starchart.cc/yishunzhikong/lishijieHELP.svg)](https://starchart.cc/yishunzhikong/lishijieHELP)
