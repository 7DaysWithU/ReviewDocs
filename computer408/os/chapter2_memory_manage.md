# 内存管理

## 1 知识点

### 1.1 基础内存管理

#### 1.1.1 概念

![内存基础](../../resource/image/os/chapter2/memory_basis.png "内存基础")

![地址类型](../../resource/image/os/chapter2/addressing.png "地址类型")

![内存管理](../../resource/image/os/chapter2/memory_manage.png "内存管理")

* 内存保护
  * 方法一：在CPU中设置一对上、下限寄存器，存放进程的上、下限地址。进程的指令要访问某个地址时，CPU检查是否越界
  * 方法二：采用重定位寄存器(又称基址寄存器 $\text{BR}$ )和界地址寄存器(又称限长寄存器)进行越界检查。重定位寄存器中存放的是进程的起始物理地址。界地址寄存器中存放的是进程的最大逻辑地址
  * 内存保护需要操作系统和硬件(各种寄存器)一同完成

![进程映像](../../resource/image/os/chapter2/memory_manage_process_image.png "进程映像")

* 低地址的 $1\text{G}$ 空间包含堆区、读写数据区、只读区，其中高地址部分为堆区的扩展预留空间
* 中间的 $1\text{G}$ 空间保护栈区、共享库，其中中部区域为二者的扩展预留空间
* 宏定义数在编译时会变成立即数包含在只读区中
* 进程线程资源分配详见[资源分配](./chapter1_cpu_manage.md#112-线程)

#### 1.1.2 连续分配管理

![连续分配管理](../../resource/image/os/chapter2/memory_successive_allocation.png "连续分配管理")
  
内存分配有连续分配和非连续分配方式两种。连续分配为系统给用户进程分配的是一个连续的内存空间

* 单一连续分配

  ![单一连续分配](../../resource/image/os/chapter2/memory_successive_allocation_single.png "单一连续分配")

  * 属于静态重定位，不需要硬件地址变换机构

* 固定分区分配

  ![固定分区分配](../../resource/image/os/chapter2/memory_successive_allocation_constant.png "固定分区分配")

  * 属于静态重定位，不需要硬件地址变换机构

* 动态分区分配
  * 定义
  
    ![动态分区分配](../../resource/image/os/chapter2/memory_successive_allocation_dynamic.png "动态分区分配")

    * 分配与回收都遵循合并周围空闲区域的原则，若进程映像的大小正好等于一个空闲区的大小，则在分区表中对应删除或增加该分区
    * 碎片与紧凑
      * 内部碎片，分配给某进程的内存区域中，如果有些部分没有用上
      * 外部碎片，是指内存中的某些空闲分区由于太小而难以利用
      * 紧凑：如果内存中空闲空间的总和本来可以满足某进程的要求，但由于进程需要的是一整块连续的内存空间，因此这些碎片不能满足进程的需求，可以通过紧凑技术将已有的进程映像排列好(挪动内存中的进程映像，修改空闲区表)，将外部碎片规整为一块连续的大空闲区
      * 动态分区只有外部碎片
    * 属于动态重定位，需要硬件地址变化机构
  
  * 动态分配算法
    * 基于顺序搜索

      | 算法 | 算法思想 | 分区排列顺序 | 优点 | 缺点  |
      |--|----|----|----|---|
      | 首次适应 | 从头到尾找适合的分区 | 空闲分区以地址递增次序排列 | 综合看性能最好。**算法开销小**，回收分区后一般不需要对空闲分区队列重新排序 | / |
      | 邻近适应 | 由首次适应演变而来，每次从上次查找结束位置开始查找 | 空闲分区以地址递增次序排列（可排列成循环链表） | 不用每次都从低地址的小分区开始检索。**算法开销小**（原因同首次适应算法） | 会使高地址的大分区也被用完|
      | 最佳适应 | 优先使用更小的分区，以保留更多大分区 | 空闲分区以容量递增次序排列 | 会有更多的大分区被保留下来，更能满足大进程需求  | 会产生很多太小的、难以利用的碎片；**算法开销大**，回收分区后可能需要对空闲分区队列重新排序 |
      | 最坏适应 | 优先使用更大的分区，以防止产生太小的不可用的碎片 | 空闲分区以容量递减次序排列 | 可以减少难以利用的小碎片  | 大分区容易被用完，不利于大进程；**算法开销大**（原因同上） |

    * 基于索引搜索

      当系统很大时，空闲分区链可能很长，此时采用顺序分配算法可能很慢。因此，在大、中型系统中往往采用索引分配算法。索引分配算法的思想是，根据其大小对空闲分区分类，对于每类(大小相同)空闲分区，单独设立一个**空闲分区链**，并设置一张**索引表**来管理这些空闲分区链。当为进程分配空间时，在索引表中查找所需空间大小对应的表项，并从中得到对应的空闲分区链的头指针，从而获得一个空闲分区。索引分配算法有以下三种

      | 算法       | 算法思想   |   分区排列顺序  | 优点     | 缺点     |
      |--|--|------|--------|--------|
      |  快速适应   | 空闲分区分类依据进程常用空间大小划分；分配分两步：①在索引表中找到最小容纳空间链表；②取下第一块分配 | 根据进程长度在索引表中查找对应空闲分区链      | 查找效率高、不产生内存碎片 | 回收分区时需合并分区，算法复杂，系统开销大  |
      | 伙伴系统   | 所有分区大小为 $2$ 的 $k$ 次幂；按需分配时，在相应大小空闲分区链中查找；若当前分区空闲区用完，则将更大分区的一个空闲区一分为二进行分配 | 按 $2$ 的幂次递增查找空闲分区链   | 高效利用内存，易于管理   | 回收时需合并相邻伙伴分区 |
      | 哈希算法   | 根据空闲分区链表分布规律建立哈希函数，构建以空闲分区大小为关键字的哈希表    | 通过哈希函数计算得到哈希表位置| 分配速度快，查找效率高   | 哈希冲突可能导致额外处理 |

#### 1.1.3 非连续分配管理

* 基本分页存储管理
  * 概念

    ![基本分页存储管理](../../resource/image/os/chapter2/memory_unsuccessive_allocation_page_basis.png "基本分页存储管理")

    ![基本分页存储管理定义](../../resource/image/os/chapter2/memory_unsuccessive_allocation_page_basis_definition.png "基本分页存储管理定义")

    ![页表](../../resource/image/os/chapter2/memory_unsuccessive_allocation_page_basis_page_table.png "页表")

    * 页表实际上只存储进程页面在内存中的页框号，即`page_table: list[int]`存储逻辑为`page_table[page_id]=page_frame_id`。因此，页表项的实际大小由内存中的页框数决定
    * 何时分页是装入作业时决定的

    ![逻辑地址结构](../../resource/image/os/chapter2/memory_unsuccessive_allocation_page_basis_logical_address.png "逻辑地址结构")

  * 基本地址变换机构

    ![基本地址变换机构](../../resource/image/os/chapter2/memory_unsuccessive_allocation_page_basis_address_translation.png "基本地址变换机构")

    * 页表项长度使用最小长度可能导致内存中存储页表项的页面存在内部碎片，使得下一个页表项在下一页，产生计算上的麻烦，因此常会让一个页表项占更多的字节，使得每个页面恰好可以装得下整数个页表项
    * 需要 $2$ 次访存，第一次查页表，第二次访问对应存储单元

    ![基本地址变换算法](../../resource/image/os/chapter2/memory_unsuccessive_allocation_page_basis_address_translation_algorithm.png "基本地址变换算法")

    ![基本地址变换算法示例](../../resource/image/os/chapter2/memory_unsuccessive_allocation_page_basis_address_translation_algorithm_eg.png "基本地址变换算法示例")

    * 页表长度`M = len(page_table)`，表示页表项的数量。仅当要访问的页号`P`小于`M`时才不会溢出，即`page_id in range(len(page_table))`
    * 根据逻辑地址查找页表的过程由硬件(页表寄存器、内存管理单元)实现

  * 具有快表的地址变换机构

    ![具有快表的地址变换机构](../../resource/image/os/chapter2/memory_unsuccessive_allocation_page_basis_address_translation_compare.png "具有快表的地址变换机构")

    ![具有页表的基本地址变换算法](../../resource/image/os/chapter2/memory_unsuccessive_allocation_page_basis_address_translation_TLB_algorithm.png "具有页表的基本地址变换算法")

  * 两级页表

    ![多级页表](../../resource/image/os/chapter2/memory_unsuccessive_allocation_page_basis_multi_page_table.png "多级页表")

    ![多级页表结构](../../resource/image/os/chapter2/memory_unsuccessive_allocation_page_basis_multi_page_table_structure.png "多级页表结构")

    ![多级页表结构示例](../../resource/image/os/chapter2/memory_unsuccessive_allocation_page_basis_multi_page_table_eg.png "多级页表结构示例")

    * 高级页表中存储低级页表的内存块号，最低级页表存储页面的内存块号。$n$ 级页表查询时需要访存 $n+1$ 次
    * 各级页表的大小不能超过一个页面

* 基本分段存储管理

  ![基本分段存储管理](../../resource/image/os/chapter2/memory_unsuccessive_allocation_segment.png "基本分段存储管理")

  ![分段结构](../../resource/image/os/chapter2/memory_unsuccessive_allocation_segment_structure.png "分段结构")

  ![段表](../../resource/image/os/chapter2/memory_unsuccessive_allocation_segment_table.png "段表")

  * 在段式存储管理中，若有些段可被多个进程共享，则可用一个单独的共享段表来描述这些段，而不需要在每个进程的段表中都保存一份。共享段表的作用是实现多个进程共享同一段代码或数据，这样既能节省内存空间，又能便于实现对共享段的更新和维护
  * 多个进程共享同一段物理内存空间并不需要用到共享段表，只需在各自的段表中指向相同的物理地址即可
  * 多个进程共享同一段逻辑地址空间是不可能的，因为每个进程的逻辑地址空间都是相互独立的
  * 何时分段是在编程时决定的

  ![基本地址变换机构](../../resource/image/os/chapter2/memory_unsuccessive_allocation_segment_address_translation.png "基本地址变换机构")

  ![分段分页对比](../../resource/image/os/chapter2/memory_unsuccessive_allocation_segment_page_compare.png "分段分页对比")

* 段页式存储管理

  ![段页式存储管理](../../resource/image/os/chapter2/memory_unsuccessive_allocation_segment_page.png "段页式存储管理")

  ![段页结构](../../resource/image/os/chapter2/memory_unsuccessive_allocation_segment_page_structure.png "段页结构")

  ![段页表](../../resource/image/os/chapter2/memory_unsuccessive_allocation_segment_page_table.png "段页表")

  ![基本地址变换机构](../../resource/image/os/chapter2/memory_unsuccessive_allocation_segment_page_address_translation.png "基本地址变换机构")

### 1.2 虚拟内存管理

* 概念

  ![虚拟内存概念](../../resource/image/os/chapter2/virtual_memory.png "虚拟内存概念")

* 请求分页管理方式

  ![请求分页管理方式](../../resource/image/os/chapter2/virtual_memory_page_request.png "请求分页管理方式")

  ![页表](../../resource/image/os/chapter2/virtual_memory_page_request_table.png "页表")

  ![缺页中断机构](../../resource/image/os/chapter2/virtual_memory_page_request_interrupt.png "缺页中断机构")

  * 中断类型属于内中断—故障，可被修复

  ![地址变换机构](../../resource/image/os/chapter2/virtual_memory_page_request_address_translation.png "地址变换机构")

* 页面置换算法
  * 最佳置换算法 $\text{OPT}$

    ![OPT](../../resource/image/os/chapter2/virtual_memory_page_request_algorithm_OPT.png "OPT")

    * 性能理论上最好，但不能预知未来的页面访问序列，因此无法实现

  * 先进先出 $\text{FIFO}$
  
    ![FIFO](../../resource/image/os/chapter2/virtual_memory_page_request_algorithm_FIFO.png "FIFO")

  * 最近最久未使用 $\text{LRU}$
  
    ![LRU](../../resource/image/os/chapter2/virtual_memory_page_request_algorithm_LRU.png "LRU")

    * 性能最接近 $\text{OPT}$，但开销大

  * 时钟置换算法 $\text{CLOCK}\,/$ 最近未使用算法 $\text{NRU}$

    ![CLOCK](../../resource/image/os/chapter2/virtual_memory_page_request_algorithm_CLOCK.png "CLOCK")

    * 初始访问位为`1`
    * 需要淘淘时，从队首开始扫描，访问位为`1`的变成`0`，访问位为`0`的淘汰

    ![改进型CLOCK](../../resource/image/os/chapter2/virtual_memory_page_request_algorithm_CLOCK_enhanced.png "改进型CLOCK")

  * 总结

    ![对比](../../resource/image/os/chapter2/virtual_memory_page_request_algorithm_compare.png "对比")

    * 需要页面置换时，淘汰的是当前内存中接下来在访问序列最后出现的页面
    * 缺页中断是要调入的页不在内存中；页面置换则是在内存满的情况下需要换页。因此刚开始内存未满时的缺页中断不算页面置换
    * 缺页率 = 缺页中断次数 / 访问序列长度

* 页框分配策略

  ![页框分配策略](../../resource/image/os/chapter2/virtual_memory_allocation.png "页框分配策略")

  ![分配置换策略](../../resource/image/os/chapter2/virtual_memory_allocation_replacement.png "分配置换策略")
  
  ![调入时机](../../resource/image/os/chapter2/virtual_memory_allocation_time.png "调入时机")

  ![调入路径](../../resource/image/os/chapter2/virtual_memory_allocation_route.png "调入路径")

  ![工作集](../../resource/image/os/chapter2/virtual_memory_allocation_work_set.png "工作集")

* 页框回收策略

* 内存映射文件

* 虚拟存储器性能影响因素

* 地址翻译

## 2 题目

* 3.1习题
  * ***05(硬件地址变换机构)***
  * 12(动态重定位不依赖目标程序)
  * 16(拼接技术是回收进程空间后合并空闲区，区别于紧凑技术)
  * 26(页表是程序装入时由操作系统建立的)
  * ***27(共享段表)***
  * 29(分段和分页提供的物理地址空间大小关系不确定)
  * ***30(页面只被操作系统感知)***
  * 33(分段是编程序时决定的)
  * 34(分段利于动态链接)
  * ***36(可重入代码)***
  * 42(主存访问以字/字节为单位)
  * ***58(多级页表)***
  * ***62(最佳适应要排序)***
  * ***70(动态分配算法碎片)***
  * ***71(页表基址寄存器存的是页表的物理始址)***
* 3.2习题
