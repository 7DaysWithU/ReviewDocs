# 数据链路层

## 1 知识点

### 1.1 数据链路层功能

![数据链路层功能](../../resource/image/network/chapter2/data_link_layer_function.png "数据链路层功能")

#### 1.1.1 组帧 (封装成帧)

![组帧](../../resource/image/network/chapter2/framing.png "组帧")

* 帧首、尾主要是一些控制信息，如帧定界信息、校验码、倾类型(数据帧、确认帧等)、帧序号等

![字符计数法](../../resource/image/network/chapter2/framing_char_counting.png "字符计数法")

![字符填充法](../../resource/image/network/chapter2/framing_char_fill.png "字符填充法")

![零比特填充法](../../resource/image/network/chapter2/framing_zero_fill.png "零比特填充法")

![违规编码法](../../resource/image/network/chapter2/framing_illegal_coding.png "违规编码法")

#### 1.1.2 差错控制

* 奇偶校验码

  ![奇偶校验](../../resource/image/network/chapter2/error_odd_even.png "奇偶校验")

* 循环冗余校验码 $\text{CRC}$

  ![CRC](../../resource/image/network/chapter2/error_CRC.png "CRC")
  
  ![构造CRC码](../../resource/image/network/chapter2/error_CRC_build.png "构造CRC码")

  * 模 $2$ 除：最高位是 $1$ 则商 $1$，最高位是 $0$ 则商 $0$
  * 模 $2$ 减：商完后被除数与部分积进行异或操作，异或结果要固定剩 $R$ 位
  
  ![CRC纠错](../../resource/image/network/chapter2/error_CRC_correct.png "CRC纠错")

  * 因为 $R$ 个校验位会有 $R$ 个余数位，且最多表示 $2^R$ 种状态，全 $0$ 固定表示正确，因此剩下 $2^R-1$ 种状态表示某位出错，数据总共 $K+R$ 位。因此 $\text{CRC}$ 只能在 $2^R-1\leq K+R$ 的情况下纠正 $1$ 位错，若数据长度大于 $K+R$，则余数错误码会从头开始，出现一个余数对应多种错误的情况

* 海明码

  ![海明码](../../resource/image/network/chapter2/error_hamming.png "海明码")

  ![构造海明码](../../resource/image/network/chapter2/error_hamming_build.png "构造海明码")

  ![海明码纠错](../../resource/image/network/chapter2/error_hamming_correct.png "海明码纠错")

  * 如果有 $2$ 位错了，则校验方程 $S$ 指出的出错位置是不正确的，因此添加全校验位区分是"错一位在多个方程里体现"还是"错多位"。全校验码就是对整体偶校验，能识别一位错误。如果全校验码错了说明是"错一位在多个方程里体现"，修改即可；反正是"错多位"，只能重传

#### 1.1.3 流量控制与可靠传输

![流量控制欲可靠传输](../../resource/image/network/chapter2/flow_controll.png "流量控制与可靠传输")

![信道利用率](../../resource/image/network/chapter2/flow_controll_channel_usage.png "信道利用率")

* 停止-等待协议 $\text{S-W}$

  ![停止-等待协议](../../resource/image/network/chapter2/flow_controll_SW.png "停止-等待协议")

  ![停止-等待协议示例](../../resource/image/network/chapter2/flow_controll_SW_eg.png "停止-等待协议示例")

  * 正常工作
  
    发送方发送一个数据帧，接收方收到数据帧并确认无误后向发送方发送确认帧，随后接收窗口后移一个。发送方收到确认帧后将发送窗口后移一个，准备发送下一个帧。**因此发送方的窗口是由接收方控制的，实现了流量控制功能**

  * 数据帧丢失
  
    发送方发出一个数据帧后，发送方需要启动计时器，若计时器超时前未收到接收方的确认帧，则自动重传，并重置计时器
  
  * 确认帧丢失
  
    发送方发送一个数据帧，接收方收到数据帧并确认无误后向发送方发送确认帧，随后接收窗口后移一个。但确认帧丢失了。一段时间后发送方计时器超时并自动重传该帧。接收方收到后丢弃该重复帧，并发送针对该帧的确认帧。发送方收到确认帧后将发送窗口后移一个。**因此，必须给帧编号，否则无法识别重复帧**

    停止-等待协议中 $W_t+W_r=1+1\leq 2^n$，即 $n\geq 1$，最少采用 $1\text{bit}$ 对帧进行编号
  
  * 数据帧错误
  
    发送方发送一个数据帧，接收方收到数据帧后发现数据帧错误，则丢弃该帧，且不返回确认帧。等待发送方计时器超时后自动重传

  * 数据帧失序

    停止-等待协议不存在失序问题，因为发送窗口和接受窗口大小都为 $1$

  ![停止-等待协议信道利用率](../../resource/image/network/chapter2/flow_controll_SW_channel_usage.png "停止-等待协议信道利用率")

* 后退 $N$ 帧协议 $\text{GBN}$

  ![后退N帧协议](../../resource/image/network/chapter2/flow_controll_GBN.png "后退N帧协议")

  ![后退N帧协议示例](../../resource/image/network/chapter2/flow_controll_GBN_eg.png "后退N帧协议示例")

  * 正常工作
  
    发送方按序连续发送多个数据帧，接收方逐个接收数据帧并确认无误，接收完最后一个帧时向发送方发送确认帧，确认帧帧号为发送窗口中最后一个帧的帧号，意为累计确认该帧及其之前的帧均已正常接受，随后接收窗口后移一个。发送方收到确认帧后将发送窗口开始帧后移到接收窗口当前想要接收的帧处。如图中发送窗口应移动到`3 0 1`处

  * 数据帧丢失 / 错误
  
    发送方每发出一个数据帧后，都启动对应帧的计时器。接收方会丢弃错误帧和超出当前接收窗口的帧，并发送当前已接收的最后一个帧的 $\text{ACK}_i$。当计时器超时或收到 $\text{ACK}_i$ 时，发送方将发送窗口的开始帧移动到第 $i+1$ 帧，并重发从 $i+1$ 帧开始到发送窗口结束的所有帧
  
  * 确认帧丢失
  
    发送方每发出一个数据帧后，都启动对应帧的计时器。但接收方接收后发出的确认帧丢失。当计时器超时后，发送方会重传发送窗口内的所有帧，接收方收到后会丢弃重复帧，并发送当前已接收的最后一个帧的 $\text{ACK}_i$，发送方收到后移动发送窗口

    若帧编号不遵循 $W_t+W_r\leq 2^n$ 的要求，当发生数据帧重传时，接收窗口要求的帧号可能正好对应已经接受的重复帧的编号，导致错误的对应

  * 数据帧失序

    后退N帧协议不存在失序问题，因为接受窗口大小只有 $1$

* 选择重传协议 $\text{SR}$

  ![选择重传协议](../../resource/image/network/chapter2/flow_controll_SR.png "选择重传协议")

  ![选择重传协议示例](../../resource/image/network/chapter2/flow_controll_SR_eg.png "选择重传协议示例")

  * 需要逐帧 $\text{ACK}$
  * 超时会导致重传，若数据帧错误则接收方会发送否认帧 $\text{NAK}$，要求发送方立刻重传该帧
  * 若帧编号不遵循 $W_t+W_r\leq 2^n$，会导致无法分辨重复帧；若不遵循 $W_t\geq W_r$，则接收窗口始终有空闲窗口，浪费资源

  ![GBN与SR信道利用率](../../resource/image/network/chapter2/flow_controll_SR_GBN_channel_usage.png "GBN与SR信道利用率")

#### 1.1.4 介质访问控制 (MAC)

##### 1.1.4.1 信道划分

![信道划分](../../resource/image/network/chapter2/mac_split.png "信道划分")

* 时分复用 $\text{TDM}$

  ![时分复用](../../resource/image/network/chapter2/mac_split_TDM.png "时分复用")

* 统计时分复用 $\text{STDM}$

  ![统计时分复用](../../resource/image/network/chapter2/mac_split_STDM.png "统计时分复用")

* 频分复用 $\text{FDM}$

  ![频分复用](../../resource/image/network/chapter2/mac_split_FDM.png "频分复用")

* 波分复用 $\text{WDM}$

  ![波分复用](../../resource/image/network/chapter2/mac_split_WDM.png "波分复用")

  * 本质上也是频分复用，因为波长与频率是倒数关系，但光信号的带宽更大，能拆出更多子信道

* 码分复用 $\text{CDM}$

  ![码分复用](../../resource/image/network/chapter2/mac_split_CDM.png "码分复用")

  * 各站点码片序列相互正交，且各站点知道其他站点的码片序列
  * 码片序列为 $m$ 维向量，元素值为 $\set{1,-1}$
  * 从叠加信号中分辨是哪个站发的信号，使用下式计算。其中 $\eta_i$ 为 $i$ 站的码片序列，$\xi$ 为收到的混合码片序列，$m$ 为码片序列长度
  
    $$
    \dfrac{1}{m}\eta_i\cdot\xi=
    \begin{cases}
      1,&i站发送的1 \\
      -1,&i站发送的0 \\
      0,&i站没有发送
    \end{cases}
    $$

##### 1.1.4.2 随机访问

![随机访问](../../resource/image/network/chapter2/mac_random_0.png "随机访问")

* $\text{ALOHA}$ 协议

  ![ALOHA协议](../../resource/image/network/chapter2/mac_random_ALOHA.png "ALOHA协议")

  ![纯ALOHA](../../resource/image/network/chapter2/mac_random_ALOHA_pure.png "纯ALOHA")

  ![时隙ALOHA](../../resource/image/network/chapter2/mac_random_ALOHA_time.png "时隙ALOHA")

* $\text{CSMA}$ 协议

  ![1坚持CSMA](../../resource/image/network/chapter2/mac_random_CSMA_1_hold.png "1坚持CSMA")

  * 因为坚持监听，所以信道刚空闲时可能有多个节点同时发数据造成冲突

  ![非坚持CSMA](../../resource/image/network/chapter2/mac_random_CSMA_non_hold.png "非坚持CSMA")

  * 非坚持通过等待监听改进了 1 坚持可能冲突的特点，但导致信道利用率低

  ![p坚持CSMA](../../resource/image/network/chapter2/mac_random_CSMA_p_hold.png "p坚持CSMA")

* $\text{CSMA/CD}$ 协议

  ![CSMACD](../../resource/image/network/chapter2/mac_random_CSMACD.png "CSMACD")

  ![CSMACD发送流程图](../../resource/image/network/chapter2/mac_random_CSMACD_flowchart_send.png "CSMACD发送流程图")

  ![CSMACD接收流程图](../../resource/image/network/chapter2/mac_random_CSMACD_flowchart_reveive.png "CSMACD接收流程图")

  ![CSMACD争用期](../../resource/image/network/chapter2/mac_random_CSMACD_contention.png "CSMACD争用期")

  * 单倍最大单向传播时延能使一个节点发出的比特流占满整个信道，其他节点监听到信道忙时就不会再发帧
  * 两倍最大单向传播时延是最大可能的冲突时间。以图中数据为例，假设 $A$ 给 $B$ 发送一个帧，在第 $29\mu\text{s}$ 时，$B$ 还认为信道是空的，遂发送一个帧，但马上与 $A$ 发送的帧冲突了。再经过 $30\mu\text{s}$ 冲突信息才能被 $A$ 接收到，从 $A$ 发出信息到收到碰撞信息，总共过去两倍的单向最大传播时延。
  * 如果能度过争用期，则后续都是安全不会被打扰的

  ![CSMACD最短帧](../../resource/image/network/chapter2/mac_random_CSMACD_shortest_frame.png "CSMACD最短帧")

  * 如果帧太短，在极限情况，也就是争用期马上要满的情况下发生冲突，但此前因为帧太短导致已经发送完毕，且发送完毕前都未冲突，发送方因此认为发送成功，但实际出现冲突发送失败了。因此最短帧长不能低于关于争用期的时延带宽积。**以太网规定最小帧长为 $64\text{B}$**
  * 最大帧长也应该被限制，否则发送方会持续霸占信道导致其他节点无法收发信息，但最大帧长的限制由不同技术有不同的方案。**以太网规定最大帧长为 $1518\text{B}$**

* $\text{CSMA/CA}$ 协议

##### 1.1.4.3 轮询访问

### 1.2 局域网

### 1.3 广域网

### 1.4 数据链路层设备

## 2 题目

* 3.1习题
  * ***06(流量控制是限制发送方的发送速率，以免超出接收方的承受能力)***
* 3.2习题
* 3.3习题
* 3.4习题
  * ***24(帧动态大小要求信道利用率恒100%，应以短帧计算，这样短的满足长的也满足，反正不成立)***
  * ⭐***26(滑动窗口协议帧序号比特数)***
* 3.5习题
* 3.6习题
* 3.7习题
* 3.8习题
