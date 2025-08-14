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

  ![IO软件层次结构](../../resource/image/os/chapter4/io_software_architecture_1.png "IO软件层次结构")

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

* 假脱机技术 $\text{SPOOLing}$

  ![SPOOLing](../../resource/image/os/chapter4/SPOOLing.png "SPOOLing")

  ![SPOOLing结构](../../resource/image/os/chapter4/SPOOLing_structure.png "SPOOLing结构")

  * $\text{SPOOLing}$ 由**预输入程序、井管理程序、缓输出程序**组成
  * 采用 $\text{SPOOLing}$ 技术的计算机不需要专门的外围控制机，因为 $\text{SPOOLing}$ 中的输入进程、输出进程采用软件模拟实现了外围控制机

  ![共享打印机](../../resource/image/os/chapter4/SPOOLing_eg.png "共享打印机")

* 设备分配与回收

  ![设备分配与回收](../../resource/image/os/chapter4/device_allocate_reclaim.png "设备分配与回收")

  ![考虑因素](../../resource/image/os/chapter4/device_allocate_reclaim_factor.png "考虑因素")

  * 设备分配算法：先来先服务、优先级高者优先、短任务优先等。详见[操作系统-cpu管理-调度算法](./chapter1_cpu_manage.md#12-cpu调度)
  * 静态分配与动态分配——详见[操作系统-cpu管理-死锁预防](./chapter1_cpu_manage.md#14-死锁)
    * 静态分配：进程运行前为其分配全部所需资源，运行结束后归还资源破坏了“请求和保持”条件，不会发生死锁
    * 动态分配：进程运行过程中动态申请设备资源
    * 独占设备一般采用静态分配方式，共享设备一般采用动态分配方式

  ![设备数据结构](../../resource/image/os/chapter4/device_allocate_reclaim_data_structure.png "设备数据结构")

  ![设备分配](../../resource/image/os/chapter4/device_allocate_algorithm.png "设备分配")

  ![设备分配改进](../../resource/image/os/chapter4/device_allocate_algorithm_enhanced.png "设备分配改进")

  * 使用逻辑设备名请求设备。第一次请求随机分一个要求类型的空闲设备，并将其物理设备名与请求中的逻辑设备名进行映射绑定，将映射项添加到 $\text{LUT}$ 中，下次使再用这个逻辑设备名请求就固定分配此设备

* 缓冲区

  ![缓冲](../../resource/image/os/chapter4/buffer.png "缓冲")

  * 分类

    ![单缓冲](../../resource/image/os/chapter4/buffer_single.png "单缓冲")

    * $T>C$：$\text{CPU}$ 处理完数据后暂时不能将下一块数据传送到工作区，必须等待缓冲区中冲满数据
    * $T<C$：缓冲区中冲满数据后暂时不能继续冲入下一块数据，必须等待 $\text{CPU}$ 处理结束后再将数据从缓冲区传送到工作区，因为 $\text{CPU}$ 运行需要使用工作区的数据
    * 两台主机通信，若使用单缓冲，则同一时刻只能单向传递信息，因为一方必须接收到数据后腾空缓冲区才能准备回复信息

    ![双缓冲](../../resource/image/os/chapter4/buffer_double.png "双缓冲")

    * 两个相互通信的机器设置双缓冲区，一对缓冲区用于发送数据，一对缓冲区用于接收数据，则同一时刻可以实现双向的数据传输

    ![循环缓冲](../../resource/image/os/chapter4/buffer_circle.png "循环缓冲")

    ![缓冲池](../../resource/image/os/chapter4/buffer_pool.png "缓冲池")

    * **输入进程** 请求输入数据：从 **空缓冲队列** 队首取出一块作为 **收容输入( $\text{hin}$ )** 数据的工作缓冲区，冲满数据后将缓冲区挂到 **输入队列** 队尾
    * **计算进程** 想要取得一块输入数据：从 **输入队列** 队首取得一块冲满输入数据的缓冲区作为 **提取输入( $\text{sin}$ )** 数据的工作缓冲区，缓冲区读空后挂到 **空缓冲队列** 队尾
    * **计算进程** 想要将准备好的数据冲入缓冲区：从 **空缓冲队列** 队首取出一块作为 **收容输出( $\text{hout}$ )** 数据的工作缓冲区，数据冲满后将缓冲区挂到 **输出队列** 队尾
    * **输出进程** 请求输出数据：从 **输出队列** 队首取得一块冲满输出数据的缓冲区作为 **提取输出( $\text{sout}$ )** 数据的工作缓冲区，缓冲区读空后挂到 **空缓冲队列** 队尾

  * 总结
    * 单缓冲、双缓冲、循环缓冲都是专用缓冲，需要指明使用者；缓冲池是共用缓冲，适合多个进程同时 $\text{I/O}$
    * 缓冲区既可用于块设备，也能用于字符设备

### 1.3 磁盘与固态硬盘

* 磁盘

  详见[组成原理-存储-外部存储器](../organization/chapter2_memory.md#13-外部存储器)

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
  * 01(设备独立性定义)
  * 18(提高单机资源利用率关键技术是多道程序设计技术)
  * ***22(SPOOLing外围控制机是软件实现的)***
  * ***31(设备独立性软件功能)***
  * ***32(设备驱动程序负责处理与设备相关的中的处理过程)***
  * ***34(设备驱动程序处理流程)***
  * ***45(内核缓冲区)***
* 5.3习题
