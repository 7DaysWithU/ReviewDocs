# 文件管理

## 1 知识点

### 1.1 文件

* 概念

  ![文件概念](../../resource/image/os/chapter3/file_manage.png "文件概念")

* 逻辑结构

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

* 操作

* 文件共享

* 文件保护

### 1.2 目录

* 概念

* 结构

### 1.3 文件系统

* 系统结构

* 系统布局

* 存储空间管理

* 虚拟文件系统

* 文件系统挂载

## 2 题目

* 4.1习题
* 4.2习题
* 4.3习题
