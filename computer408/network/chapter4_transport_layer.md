# 传输层

## 1 知识点

### 1.1 传输层功能

![传输层功能](../../resource/image/network/chapter4/transport_layer.png "传输层功能")

| 互联网应用 | $\text{TCP/IP}$ 应用层协议 | $\text{TCP/IP}$ 传输层协议 | 端口号 |
| :-: | :-: | :-: | :-: |
| 域名解析 | 域名系统 $(\text{DNS})$ | $\text{UDP}$ | $53$ |
| 文件传送 | 简单文件传送协议 $(\text{TFTP})$ | $\text{UDP}$ | $69$ |
| 路由选择 | 路由信息协议 $(\text{RIP})$ | $\text{UDP}$ | $520$ |
| $\text{IP}$ 地址分配 | 动态主机配置协议 $(\text{DHCP})$ | $\text{UDP}$ | $68$ |
| 网络管理 | 简单网络管理协议 $(\text{SNMP})$ | $\text{UDP}$ | $161$ |
| 电子邮件 | 简单邮件传送协议 $(\text{SMTP})$ | $\text{TCP}$ | $25$ |
| 远程终端接入 | 远程终端协议 $(\text{TELNET})$ | $\text{TCP}$ | $23$ |
| 万维网 | 超文本传送协议 $(\text{HTTP})$ | $\text{TCP}$ | $80$ |
| 文件传送 | 文件传送协议 $(\text{FTP})$ | $\text{TCP}$ | $21$ |

* $\text{TCP}$ 和 $\text{UDP}$ 的端口互相独立，即两个协议可以使用同一个端口号，以套接字中的协议作区分
* $\text{TCP}$ 的面向连接可以保证可靠与顺序交付
* 套接字可以唯一确定一个在互联网上通信的进程

### 1.2 UDP

![UDP](../../resource/image/network/chapter4/UDP.png "UDP")

* $\text{UDP}$ 只在 $\text{IP}$ 的基础上增加了端口(复用分用功能)
* $\text{UDP}$ 数据报的理论最大长度为 $65515\text{B}$，因为封装为 $\text{IP}$ 数据报后 $\text{IP}$ 首部至少 $20\text{B}$。实际长度依赖链路的 $\text{MTU}$

![UDP检验](../../resource/image/network/chapter4/UDP_check.png "UDP检验")

* 若检验和的计算结果正好为全 $0$，则设置检验和的内容为全 $1$，因为全 $0$ 表示不启用检验和

![校验算法](../../resource/image/network/chapter4/UDP_check_algorithm.png "校验算法")

* 该算法适用于 $\text{IP}$ 数据报和 $\text{UDP}$ 数据报的首部检验和。 $\text{IP}$ 数据报只需要将首部按每 $16\text{bit}$ 计算取反即得到首部检验和。$\text{UDP}$ 数据报检验和则要额外增加伪首部再计算

![UDP检验发送方](../../resource/image/network/chapter4/UDP_check_send.png "UDP检验发送方")

![UDP检验接收方](../../resource/image/network/chapter4/UDP_check_receive.png "UDP检验接收方")

### 1.3 TCP

* 概念

  ![TCP概念](../../resource/image/network/chapter4/TCP_term.png "TCP概念")

* $\text{TCP}$ 报文段

  ![TCP报文段](../../resource/image/network/chapter4/TCP_message_0.png "TCP报文段")

  * 确认号不包括当前序号，例如已发送 $0,1,2,3$ 报文段，收到确认号 $2$，表明 $0,1$ 已被正确接收。确认号既可以解读为对之前序号的累计确认，也可以解读为接下来想要接收的序号

  ![TCP报文段](../../resource/image/network/chapter4/TCP_message_1.png "TCP报文段")

  * $\text{TCP}$ 报文段数据部分长度 $=\text{IP}$ 数据报总长度 $-\text{IP}$ 首部长度 $-\text{TCP}$ 首部长度

  ![TCP报文段](../../resource/image/network/chapter4/TCP_message_2.png "TCP报文段")

  * 紧急指针本质上也是序号，但与序号拥有不同的号码

  ![TCP报文段](../../resource/image/network/chapter4/TCP_message_3.png "TCP报文段")

  ![TCP报文段](../../resource/image/network/chapter4/TCP_message_4.png "TCP报文段")

  ![TCP报文段](../../resource/image/network/chapter4/TCP_message_5.png "TCP报文段")

  ![TCP报文段](../../resource/image/network/chapter4/TCP_message_6.png "TCP报文段")

  * 双方各自设置的 $\text{MSS}$ 可以不相同。协商 $\text{MSS}$ 的目的是预留收发缓冲区，以便更好地通信

* 连接管理

  ![TCP连接管理](../../resource/image/network/chapter4/TCP_build_release.png "TCP连接管理")

  ![TCP连接与释放](../../resource/image/network/chapter4/TCP_build_release_flowchart.png "TCP连接与释放")

  * 建立连接

    ![建立连接标志位](../../resource/image/network/chapter4/TCP_build_tag.png "建立连接标志位")

    ![建立连接状态和最短时间](../../resource/image/network/chapter4/TCP_build_state_time.png "建立连接状态和最短时间")

  * 释放连接

    ![释放连接标志位](../../resource/image/network/chapter4/TCP_release_tag.png "释放连接标志位")

    ![释放连接状态](../../resource/image/network/chapter4/TCP_release_state.png "释放连接状态")

    * 断开连接可以是客户端先挥手，也可以是服务器先挥手。因此图左为先挥手的一方，图右为被动接受的一方
    * 先挥手的一方在收到挥手 $3$ 后要等待 $2\text{MSL}$，用以确认另一方先关闭连接。在 $\text{TIME-WAIT}$ 期间如果再次收到挥手 $3$ 需要重置计时器

    ![释放连接最短时间](../../resource/image/network/chapter4/TCP_release_time.png "释放连接最短时间")

* 可靠传输与流量控制

* 拥塞控制

## 2 题目

* 5.1习题
  * 03(面向连接的服务可以确保数据的顺序交付)
* 5.2习题
  * 08(全0检验和)
* 5.3习题
