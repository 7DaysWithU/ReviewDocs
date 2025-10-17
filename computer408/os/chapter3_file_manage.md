# 文件管理

## 1 知识点

### 1.1 文件

* 概念

  ![文件概念](../../resource/image/os/chapter3/file_manage.png "文件概念")

* 逻辑结构

  逻辑结构可以由 **用户** 确定
  
  ![逻辑结构](../../resource/image/os/chapter3/logical_structure.png "逻辑结构")

  ![有结构文件](../../resource/image/os/chapter3/logical_structure_structured.png "有结构文件")

  * 无结构文件

    无结构内部的数据就是一系列二进制流或字符流组成。又称流式文件。如 $\text{Windows}$ 操作系统中的`.txt`文件

  * 有结构文件

    有结构文件由一组相似的记录组成，又称记录式文件。每条记录又若干个数据项组成。如数据库表文件。一般来说，每条记录有一个数据项可作为**关键字**。根据各条记录的长度(占用的存储空间)是否相等，又可分为**定长记录**和**可变长记录**两种。按物理结构可分为**顺序文件、索引文件、索引顺序文件**

    ![顺序文件](../../resource/image/os/chapter3/logical_structure_structured_sequence.png "顺序文件")

    * 定长记录顺序存储支持随机存取

    ![索引文件](../../resource/image/os/chapter3/logical_structure_structured_index.png "索引文件")

    * 支持在可变长场景下的随机存取，但索引表本身较为庞大

    ![索引顺序文件](../../resource/image/os/chapter3/logical_structure_structured_index_sequence.png "索引顺序文件")

    ![多级索引顺序文件](../../resource/image/os/chapter3/logical_structure_structured_index_sequence_multi.png "多级索引顺序文件")

    * 通过多级分表解决了单个索引表过大的问题，同时多级顺序索引文件的查询效率依然良好

* 物理结构

  物理结构说明的是文件在 **外存** 中的存储形式，即如何管理 **非空闲磁盘块**。物理结构是由 **操作系统** 确定的

  ![物理结构](../../resource/image/os/chapter3/physical_structure.png "物理结构")

  ![磁盘块](../../resource/image/os/chapter3/physical_structure_block.png "磁盘块")

  * 连续分配

    ![连续分配](../../resource/image/os/chapter3/physical_structure_sequence.png "连续分配")

  * 链接分配

    ![链接分配隐式链接](../../resource/image/os/chapter3/physical_structure_list_implicit.png "链接分配隐式链接")

    * 读入`i`号块需要访存 $i+1$ 次，找到`i`号块需要访存 $i$ 次
    * 链接分配未说明具体链接形式时，默认为隐式链接

    ![链接分配显式链接](../../resource/image/os/chapter3/physical_structure_list_explicit.png "链接分配显式链接")

    * 想访问`i`号逻辑块时不需要访问(访存)之前的块，逻辑地址转物理地址时不需要访存

  * 索引分配

    ![索引分配](../../resource/image/os/chapter3/physical_structure_index.png "索引分配")

    ![索引分配链接方案](../../resource/image/os/chapter3/physical_structure_index_link.png "索引分配链接方案")

    ![索引分配多级索引方案](../../resource/image/os/chapter3/physical_structure_index_index.png "索引分配多级索引方案")

    ![索引分配混合索引方案](../../resource/image/os/chapter3/physical_structure_index_mix.png "索引分配混合索引方案")

    ![索引分配总结](../../resource/image/os/chapter3/physical_structure_index_summary.png "索引分配总结")

    * **一个文件索引结点就对应一个文件。索引结点里具体的分配方式(如一级二级索引)是用来索引块或簇的，而这些块或簇是组成文件的一部分**

* 操作

  ![文件操作](../../resource/image/os/chapter3/file_operate.png "文件操作")

* 文件共享

  ![文件共享](../../resource/image/os/chapter3/file_share.png "文件共享")

  ![文件共享硬链接](../../resource/image/os/chapter3/file_share_hard_link.png "文件共享硬链接")

  * 每有一个用户查看则`count`就加一，只有一个用户时`count = 1`
  * 所有使用索引节点硬链接的文件共享同一个`count`值
  
  ![文件共享软链接](../../resource/image/os/chapter3/file_share_soft_link.png "文件共享软链接")

  * 软链接的`count`值不受被链接文件的影响，无论被链接文件存不存在，软链接计数始终为 $1$

* 文件保护

  ![文件保护](../../resource/image/os/chapter3/file_protect.png "文件保护")

  ![口令保护](../../resource/image/os/chapter3/file_protect_password.png "口令保护")

  ![加密保护](../../resource/image/os/chapter3/file_protect_encryption.png "加密保护")

  ![访问控制](../../resource/image/os/chapter3/file_protect_access.png "访问控制")

### 1.2 目录

![目录概念](../../resource/image/os/chapter3/directory.png "目录概念")

* 文件控制块 $\text{FCB}$ 与索引节点

  ![FCB](../../resource/image/os/chapter3/directory_FCB.png "FCB")

  * 文件目录项就是 $\text{FCB}$，因为目录就是 $\text{FCB}$ 的集合

  ![索引结点](../../resource/image/os/chapter3/directory_index_node.png "索引结点")

* 目录结构

  ![单级目录](../../resource/image/os/chapter3/directory_structure_1.png "单级目录")

  ![二级目录](../../resource/image/os/chapter3/directory_structure_2.png "二级目录")

  ![多级目录](../../resource/image/os/chapter3/directory_structure_multi.png "多级目录")

  ![无环图目录](../../resource/image/os/chapter3/directory_structure_DAG.png "无环图目录")

* 目录检索
  * 散列法
    * 使用哈希函数将逻辑地址映射成物理地址，需要较大的存储空间
  
  * 顺序检索法
    * 对给出的绝对地址或相对地址，在树形目录中查找。若使用绝对地址，则从根目录开始查找；若使用相对地址，则从相对地址的开头目录查找
    * 只要路径中有一个目录未找到，则停止检索
    * 检索完成后，可能得到文件的物理地址，也可能得到文件的`inode`。具体看文件使用的物理存储方法

### 1.3 文件系统

* 文件系统层次结构

  ![文件系统层次结构](../../resource/image/os/chapter3/file_system_architecture.png "文件系统层次结构")

* 文件系统布局

  ![文件系统外存结构](../../resource/image/os/chapter3/file_system_out_memory.png "文件系统外存结构")

  * 引导块用于开机引导
  * 超级块用于快速获取空闲块；位示图用于快速检索指定块是否空闲
  * i 结点区存放文件的索引结点

  ![文件系统内存结构](../../resource/image/os/chapter3/file_system_in_memory.png "文件系统内存结构")

  * 打开文件只需要将文件索引结点装入内存一次即可；共享文件时不同进程可以通过系统打开文件表或目录缓存直接获得文件的文件索引结点，因此也只需要将文件索引结点装入内存一次即可
  * **进程读取文件只需要文件描述符，不需要其他任何参数(比如路径、文件名等)**

* 存储空间管理

  存储空间管理主要说明 **外存** 中没有存储文件的磁盘块该如何管理，即如何管理 **空闲磁盘块**

  ![存储空间管理](../../resource/image/os/chapter3/memory_manage.png "存储空间管理")
  
  ![文件卷](../../resource/image/os/chapter3/memory_manage_volumn.png "文件卷")

  磁盘分为若干个文件卷，每个文件夹分为目录区和文件区；一个文件卷一般对应一个磁盘，也可以是多个磁盘

  * 空闲表法

    ![空闲表法](../../resource/image/os/chapter3/memory_manage_algorithm_sequence.png "空闲表法")

    * 分配与回收适用内存连续分配—动态分区法的分配回收算法
    * 适用于连续分配方式

  * 空闲链表法

    ![空闲链表法](../../resource/image/os/chapter3/memory_manage_algorithm_list.png "空闲链表法")

    * 空闲盘块链适用于离散分配，连续分配需要多次IO操作效率低
    * 空闲盘区链离散、连续都适用。连续分配时直接分配盘区一整区，效率高
    * 空闲盘区连续分配时，若每个盘区都不满足要求，可以跨区合并分配

  * 位示图法

    ![位示图法](../../resource/image/os/chapter3/memory_manage_algorithm_bitmap.png "位示图法")

    * 连续、离散分配都适用

  * 成组链接法

    ![成组链接法](../../resource/image/os/chapter3/memory_manage_algorithm_group_link.png "成组链接法")

    * 成组链接法将所有空闲盘块分成若干组，每组的第一个盘块记录下一组的空闲盘块总数和空闲盘块号。第一组的空闲盘块总数和空闲盘块号存放在内存的专用栈中，称为 **空闲盘块号栈**

    ![成组链接法分配](../../resource/image/os/chapter3/memory_manage_algorithm_group_link_allocate.png "成组链接法分配")

    * 在前一张图的基础上，需要100个块，因此将第一组的201~300全部分配出去，但300记录了信息，因此让超级块的记录变为300的内容，300清空内容作为空闲块分配出去
    * 分配
      * 若第一组足够分配，则直接在第一组中分配，并修改剩余空闲块数量
      * 若第一组不够分配，则将第一组全部分配出去，不够的部分使用下一组补充。超级块保存下一组记录信息的块的内容，建立新的链接

    ![成组链接法回收](../../resource/image/os/chapter3/memory_manage_algorithm_group_link_reclaim.png "成组链接法回收")

    * 在前一张图的基础上，回收块300，但第一组已满，因此将超级块的内容复制到300，用300建立连接，并更新超级块指向300
    * 回收
      * 若第一组未满，则回收块直接挂载到第一组中
      * 若第一组已满，则将超级块内容复制到回收块中，回收块建立与其他组的链接，更新超级块指向回收快

* 虚拟文件系统 $\text{VFS}$

  ![虚拟文件系统](../../resource/image/os/chapter3/virture_file_system.png "虚拟文件系统")

  * 特点
    * $\text{VFS}$ 向上层用户进程提供统一标准的系统调用接口，屏蔽底层具体文件系统的实现差异
    * $\text{VFS}$ 要求下层的文件系统必须实现某些规定的函数功能，如`open()`、`read()`、`write()`等。一个新的文件系统想要在某操作系统上被使用，就必须满足该操作系统 $\text{VFS}$ 的要求
    * 每打开一个文件，$\text{VFS}$ 就在主存中新建一个`vnode`，用统一的数据结构表示文件，无论该文件存储在哪个文件系统。`vnode`中存储对应文件系统的操作函数地址列表
  * 对象类型
    * 索引结点对象`inode`：表示一个单独的文件
    * 文件对象`file`：表示一个已打开的文件
    * 超级块对象`superblock`：表示整个文件系统
    * 目录项对象`dentry`：表示单个目录项

* 文件系统挂载

  ![文件系统挂载](../../resource/image/os/chapter3/file_system_mounting.png "文件系统挂载")

  * 将新文件系统的对应系统信息提交注册，包括文件系统类型、文件大小等
  * 提供对应的操作函数地址列表，如`open()`、`read()`等系统内操作函数地址组成的列表
  * 操作系统将新文件系统加到挂载点处，一般是某个父目录下。如 $\text{Windows}$ 系统将 $\text{U}$ 盘文件系统挂载到根目录下

## 2 题目

### 2.1 选择

* 4.1习题
  * 09(文件目录项)
  * 14(进入系统注册是系统级安全管理)
  * 15(磁盘调度算法可以提升文件系统性能)
  * 28(存储文件时采用的物理形式与存储介质有关)
  * 30(记录成组分解技术、写文件也需要启动磁盘1次)
  * ***33(FAT表块号大小)***
  * ***35(索引分配修改信息时，只要索引结点在内存就不需要IO)***
  * 40(文件分配表必须数组实现)
  * 44(睡眠就是阻塞、read只要文件描述符)
  * ***49(索引分配访存次数)***
  * ***51(按簇分配必须是簇的整数倍)***
  * ***52(文件按索引结点算)***
* 4.2习题
  * 01(目录检索)
  * 03(多级目录主要目的是解决命名冲突)
  * ***05(存取控制矩阵用于标识用户对文件的操作权限)***
  * ***13(读入与找到的访存次数)***
* 4.3习题
  * 04(Unix的索引结构存在索引节点(也称 i 结点))
  * ***06(外存文件区以提高存储空间利用率为主要目标)***
  * 12(数据对象不是VFS定义的对象)
  * ***14(位示图法块号)***
  * ***15(FAT也能用于空闲链表法的数据结构)***

### 2.2 大题

* 4.1习题
  * 06(文件的物理结构及其数据结构、文件的FCB最好集中存放)
  * 07(索引项长度、单个文件最大长度、带预留空间的分配方法)
  
    > * 带预留空间时，单个文件的最大长度=预留空间大小+索引空间的大小
    > * **带预留空间的分配方法不是基础的三种分配方法，要根据题目灵活应变**

  * ⭐***08(顺序存储插入记录的最少移动次数、文件系统支持的最大文件长度、链表查找次数)***
  
    > * 如果文件的前后都有空闲区，则顺序存储时插入或删除导致的移动方向应该选记录数少的那个方向。本质还是顺序表的移动次数

  * ***09(写链式分配表项、文件系统支持的最大文件长度、FAT表长度、取文件某个字节的数据需要读入几个簇)***
  
    > 使用 $\text{FAT}$ 表查找文件某个字节的数据只需要将其所有父目录所在的簇和这个字节所在的簇读入内存。文件的物理地址可以通过计算并使用 $\text{FAT}$ 表转化，不需要像显式链接把目标块之前的所有块都读入内存

  * ⭐***10(文件系统支持的最大文件长度、文件索引结点与文件数量的关系、混合索引分配的查找时间)***
  
    > 一个文件索引结点就对应一个文件。索引结点里面分配的一级二级索引是用来索引块或簇的

  * ***11(写索引分配表项、文件读入块数、判断文件需要启用几级索引)***
* 4.3习题
  * ⭐***01(除模转换)***
