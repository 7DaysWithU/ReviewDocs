# I/O 管理

## 1 知识点

### 1.1 概念

* 定义与分类

  ![IO设备定义及分类](../../resource/image/os/chapter4/io_classification.png "IO设备定义及分类")

  * 低速设备例如键盘、鼠标；高速设备例如磁盘；中速设备例如打印机
  * 虚拟设备不会死锁。例如 $\text{SPOOLing}$ 技术改造打印机
  * **共享设备必须是可寻址且可随机访问的设备**

* $\text{I/O}$ 控制方式

  本节内容( $\text{I/O}$ 控制器、 $\text{I/O}$ 控制方式)详见[计算机组成原理-io](../organization/chapter6_io.md#)
  
  ![IO控制器](../../resource/image/os/chapter4/io_controller.png "IO控制器")

  ![IO控制器组成](../../resource/image/os/chapter4/io_controller_component.png "IO控制器组成")
  
  * $\text{I/O}$ 端口可以独立编址，也可与内存统一编址

* $\text{I/O}$ 软件层次结构

  ![IO软件层次结构](../../resource/image/os/chapter4/io_software_architecture.png "IO软件层次结构")

  * 操作系统可以采用两种方式管理设备独立性软件用到的逻辑设备表 $\text{LUT}$
    * 整个系统只设置一张 $\text{LUT}$，这就意味着所有用户不能使用相同的逻辑设备名，因此这种方式只适用于单用户操作系统
    * 为每个用户设置一张 $\text{LUT}$，各个用户使用的逻辑设备名可以重复，适用于多用户操作系统。系统会在用户登录时为其建立一个用户管理进程，而 $\text{LUT}$ 就存放在用户管理进程的 $\text{PCB}$ 中
    * 这两种方法类似单级目录与两级目录，主要为了解决不同用户的设备从逻辑名到物理名映射混乱的问题
  * 设备驱动程序负责将上层软件发来的抽象 $\text{I/O}$ 要求转换为具体要求，发送给设备控制器，控制设备工作。设备驱动程序需要向设备寄存器写入命令，以控制设备的工作状态和数据传输方式

* 接口

  ![接口](../../resource/image/os/chapter4/interface.png "接口")

  ![应用程序接口](../../resource/image/os/chapter4/interface_application.png "应用程序接口")
  
  ![驱动程序接口](../../resource/image/os/chapter4/interface_driver.png "驱动程序接口")

### 1.2 设备独立性软件

* 概念

* 缓冲

* 设备分配与回收

* 假脱机技术 $\text{SPOOLing}$

### 1.3 磁盘与固态硬盘

* 磁盘

* 磁盘管理

* 磁盘调度

* 固态硬盘 $\text{SSD}$

## 2 题目

* 5.1习题
  * 01(共享设备)
  * 05(IO逻辑用于实现设备控制器的控制功能、接口只负责传数据)
  * ***11(DMA预处理后处理细节)***
  * 13(绝对号)
  * 19(主机获得设备输入是中断服务程序(软件)操作的)
* 5.2习题
* 5.3习题
