# longriver

## 项目简介

高寻真源(山东)教育科技有限公司在2020开发了基于k8s的大数据与人工智能科研平台.其中带有拖拽式的可视化编程模块, 该部分代码即为该模块的核心代码.目前包括代码生成与前台的渲染模板.

## 授权说明

本产品相关所有的知识产权归高寻真源（山东）教育科技有限公司所有，本产品不允许任何商业化使用，仅允许科研、个人学习与教育使用，但需保留署名权。

以下为完整软件版权说明：

长河算法可视化开发平台（英文名为“longriver")，系本高寻真源（山东）教育科技有限公司独立开发软件，依法独立享有该软件之所有权利，此软件为商业软件提供免费下载。但该软件使用者(含个人、法人或其它组织):

非经授权许可，不得将之用于除个人学习，大学授课以外的盈利或非盈利性的任何用途。

为适应实际的计算机应用环境，对其功能、性能、界面，可以进行必要的修改 ，但不得去除 Version 版本标示;未经书面 授权许可，不得向任何第三方提供修改后的软件。

使用该软件必须保留版权声明，将该软件从原有自然语言文 字转换成另一自然语言文字的，仍应注明出处，并不得向任何第三方提供修改后的软件。

不得有其他侵犯软件版权之行为。

凡有上述侵权行为的个人、法人或其它组织，必须立 即停止侵权并对其侵权造成的一切不良后果承担全部责任。对此前，尤其是此后侵犯版权的行为，将依据《著作权法》、《计算机软件保护条例》 等相关法律、法规追究其经济责任和法律责任。

## 安装依赖

具体详见requirements.txt文件，建议使用Python3.8版本(推荐在清华源下载anaconda，网址：https://mirror.tuna.tsinghua.edu.cn/help/anaconda/）

Python安装后，利用pip安装命令进行安装

```shell
pip install -r requirements.txt
# 国内可使用国内镜像源
# 清华源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
# 阿里云镜像源
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

## 启动

（1）启动程序

```shell
python app.py
```

（2）在浏览器中访问本机端口

http://127.0.0.1:9703

（3）进入登录界面，登录

默认账户密码root/root

## 适用的操作系统

Windows10

Windows11

Ubuntu20.04

Ubuntu22.04

以上版本为软件测试版本，其他Windows或Linux系统理论上兼容，但未经过实际测试

## 重要更新日志

- 2020/08/27:正式发布v0.1版本，该版本科研平台内部发布的第一版所使用的版本，可用于生产。
- 2021/01/29:正式发布0.2.0版本：包含0.1与0.2版本混合代码，基于单个dockerfile的全自动镜像更新。
- 2021/03/4:添加Paddle模块，确立新格式json模板(0.3版本)。
- 2021/04/17:python_ml模块更新为json(0.3版本),正式发布0.3.0版本。
- 2023/02:基于0.3.3分支，创建单体版分支，开发版本号为0.3.4与0.4.0版本。
- 2023/05:0.4.0版本，用于中国大学生软件设计大赛发布的比赛版本
- 2024/4:0.4.1版本，修复依赖库的问题，添加大模型的模块，添加了基于ollama的llama3的webui功能。
- 2024/8:0.4.2版本，添加开发工具模块，添加了两种默认自带的开发工具
- 2024/10/29:0.4.3版本，优化大量底层代码，添加了大量注释，以增强可读性；修复了一处代码生成的bug；完成了python机器学习中import优化；优化了类库依赖；去除了过时的jupyter-tensorboard插件。

## 源代码地址

github(目前为私有）：[https://github.com/FontTian/longriver](https://github.com/FontTian/longriver)
gitlab(部署公司115集群的k8s上)：[http://192.168.1.117:9099/tianfengshou/longriver](http://192.168.1.117:9099/tianfengshou/longriver)

后续代码开源地址：

GIthub：https://github.com/Gaoxunzhenyuan

Gitee：https://gitee.com/gao-xunyuan-shandong-education

高寻真源官网：http://www.gxzy-edu.com/

## 代码规范化工具
本工具代码生成后，会自动使用代码格式化工具对代码进行格式化，格式化工具为autoflake与autopep8，首先使用autoflake去除多余引用，然后使用autopep8进行格式化。
注意：单机发行版（0.3.3之后）镜像生成文件没有更新。

```shell
# autoflake
autoflake --remove-all-unused-imports --in-place --expand-star-imports  automatically_generated_code_by_longriver_for_xxxx.py

# autopep8
autopep8 --in-place --aggressive --aggressive automatically_generated_code_by_longriver_for_xxxx.py
```

## 联系我们

高寻真源（山东）教育科技有限公司： 400-801-9680  