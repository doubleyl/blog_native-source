---
title: virtualMachine
date: 2023-03-16 00:10:04
tags:
categories:
- virtualMachine
---

#### ~桥接模式

主机与虚拟机需要在一个网段，更换后若虚拟机ip不对需要到虚拟机设置中重置ip



#### ~vsc通过ssh连接虚拟机

（自己在桥接模式下实现）

1.虚拟机上安装ssh server

2.开启ssh服务(设为开机启动)

3.(关闭主机，虚拟机防火墙)

4.主机vsc安装ssh插件

配置ssh信息：

(可能需要再扩展设置中手动配置ssh.exe地址，C:\Windows\System32\OpenSSH\ssh.exe)

(可能需要在扩展设置中配置虚拟机ip)

ip即虚拟机ip, hostname一般也为ip, user 用户

5.连接(需要root密码？)

6.安装扩展，主机的扩展好像不能给虚拟机用

