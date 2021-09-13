# pynorm

希望可以用这个工具去发现代码中的一些低级语法错误。

# 快速开始

## 安装依赖

```
sudo pip3 install -r requirements.txt
```

## 寻找程序中行末多余的空格

#从文件夹中打印可视化输出多余的空格


```
cd pynorm
python3 pynorm.py $FILE_DIR
```
#批量下载使用率较高的openstack项目
#批量获取openstack项目中多余的空格

```
cd /pynorm/openstack/
python3 clone_openstack.py
项目代码默认下载位置：/tmp/openstack

python3 ./pynorm/pynorm_openstack.py
扫描结果默认输出位置；/tmp/openstack_report
```
