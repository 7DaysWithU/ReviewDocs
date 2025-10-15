# 行列式

## 1 知识点

### 1.1 定义与性质

* 定义
  * 本质定义(第一种定义)
  
    $n(n>3)$ 阶行列式是由 $n$ 个 $n$ 维向量 $a_1=[a_{11},a_{12},\cdots,a_{1n}],a_2=[a_{21},a_{22},\cdots,a_{2n}],\cdots,a_n=[a_{n1},a_{n2},\cdots,a_{nn}]$ 组成的，其结果是以这 $n$ 个向量为临边的 $n$ 维图形的体积。当 $n=2$ 时，行列式的结果为二维的平行四边形的面积。**特别地，由 $n(n>1)$ 阶行列式计算得到的面积或体积可以为负**

    $$
    D_n=
    \begin{vmatrix}
      a_{11} & \cdots & a_{1n} \\
      \vdots & \ddots & \vdots \\
      a_{n1} & \cdots & a_{nn}
    \end{vmatrix}=
    \begin{cases}
        0,&组成行列式的向量线性相关\\\\
        \neq0,&组成行列式的向量线性无关
    \end{cases}
    $$

  * 逆序数法定义(第二种定义)
  
    由 $n$ 个数 $1,2,\cdots,n$ 组成的一个有序数组称为一个 $n$ 级排列。$n$ 级排列共有 $n!$ 个。在一个 $n$ 级排列 $i_1i_2\cdots i_a\cdots i_b\cdots i_n$ 中，若 $i_a>i_b$ 且 $i_a$ 拍在 $i_b$ 前面，则这两个数构成一个逆序。一个排列中逆序的总数为该排列的逆序数，记作 $\tau(i_1i_2\cdots i_n)$。则 $n(n\geq2)$ 阶行列式

    $$
    \begin{vmatrix}
      a_{11} & a_{12} & \cdots & a_{1n} \\
      a_{21} & a_{22} & \cdots & a_{2n} \\
      \vdots & \vdots & \ddots & \vdots \\
      a_{n1} & a_{n2} & \cdots & a_{nn}
    \end{vmatrix}
    =
    \sum_{j_1, j_2, \cdots, j_n}{(-1)^{\tau(j_1 j_2 \cdots j_n)} a_{1j_1} a_{2j_2} \cdots a_{nj_n}}
    $$

    **$n$ 阶行列式的展开式共有 $n!$ 项，每项的 $j_1 j_2 \cdots j_n$ 为 $n$ 阶全排列中的一个。当项的行号依次为 $1,2,\cdots,n$ 时，可以由此展开式确定一项的正负**

  * 展开定理(第三种定义)

    在 $n$ 阶行列式中，去掉元素 $a_{i,j}$ 所在的第 $i$ 行、第 $j$ 列的元素，由剩下的元素按照原来的位置与顺序组成的 $n-1$ 阶行列式称为元素 $a_{ij}$ 的余子式，记作 $M_{ij}$ ，即

    $$
    M_{ij} =
    \begin{vmatrix}
    a_{11} & \cdots & a_{1,j-1} & a_{1,j+1} & \cdots & a_{1n} \\
    \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
    a_{i-1,1} & \cdots & a_{i-1,j-1} & a_{i-1,j+1} & \cdots & a_{i-1,n} \\
    a_{i+1,1} & \cdots & a_{i+1,j-1} & a_{i+1,j+1} & \cdots & a_{i+1,n} \\
    \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & \cdots & a_{n,j-1} & a_{n,j+1} & \cdots & a_{nn}
    \end{vmatrix}
    $$

    元素 $a_{i,j}$ 的代数余子式记作 $A_{ij}=(-1)^{i+j}M_{ij}$。两边同乘 $(-1)^{i+j}$，有 $M_{ij}=(-1)^{i+j}A_{ij}$。行列式 $\begin{vmatrix}A\end{vmatrix}$ 的值为

    $$
    \begin{vmatrix}A\end{vmatrix}=
    \begin{cases}
      \displaystyle \sum_{j=1}^{n} a_{ij} A_{ij} & (i = 1, 2, \ldots, n)，&按行展开\\
      \displaystyle \sum_{i=1}^{n} a_{ij} A_{ij} & (j = 1, 2, \ldots, n)，&按列展开
    \end{cases}
    $$

* 性质
  * 矩阵 $A$ 转置前后行列式不变 $\begin{vmatrix}A\end{vmatrix}=\begin{vmatrix}A^T\end{vmatrix}$
  * 对任意 $n$ 阶方阵，$\begin{vmatrix}AB\end{vmatrix}=\begin{vmatrix}A\end{vmatrix}\begin{vmatrix}B\end{vmatrix}$
  * 若行列式中某行(列)元素全为 $0$，则行列式为 $0$。因为 $n$ 维空间有一维退化成原点了，缺少了一个观测维度
  * 倍乘：若行列式中某行(列)元素有公因子 $k(k\neq0)$，则 $k$ 可以提到行列式外

    $$
    \begin{equation*}
    \begin{vmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} \\
    \vdots & \vdots & \ddots & \vdots \\
    k a_{i1} & k a_{i2} & \cdots & k a_{in} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & \cdots & a_{nn}
    \end{vmatrix}
    = k \cdot
    \begin{vmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{i1} & a_{i2} & \cdots & a_{in} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & \cdots & a_{nn}
    \end{vmatrix}
    \end{equation*}
    $$

  * 行列式某行(列)元素均为两数之和，则可拆成两个行列式之和；反之两个行列式除对应行(列)不相同外，其他行(列)全部相同时，行列式可加

    $$
    \begin{vmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} \\
    \vdots & \vdots & \ddots & \vdots \\
    b_{i1} + c_{i1} & b_{i2} + c_{i2} & \cdots & b_{in} + c_{in} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & \cdots & a_{nn}
    \end{vmatrix}
    =
    \begin{vmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} \\
    \vdots & \vdots & \ddots & \vdots \\
    b_{i1} & b_{i2} & \cdots & b_{in} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & \cdots & a_{nn}
    \end{vmatrix}
    +
    \begin{vmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} \\
    \vdots & \vdots & \ddots & \vdots \\
    c_{i1} & c_{i2} & \cdots & c_{in} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & \cdots & a_{nn}
    \end{vmatrix}
    $$

  * 行列式两行(列)互换，行列式变号
  * 行列式两行(列)元素相等或对应成比例(即线性相关)，则行列式为 $0$
  * 倍加：行列式某行(列)元素的 $k$ 倍加到另一行(列)，行列式不变

    $$
    \begin{align*}
      \begin{vmatrix}
      a_{11} & a_{12} \\
      ka_{11} + a_{21} & ka_{12} + a_{22}
      \end{vmatrix}

      &\xlongequal{\text{可加可拆}}
      \begin{vmatrix}
      a_{11} & a_{12} \\
      ka_{11} & ka_{12}
      \end{vmatrix}
      +
      \begin{vmatrix}
      a_{11} & a_{12} \\
      a_{21} & a_{22}
      \end{vmatrix}\\\\

      &\xlongequal{\text{提单行系数}}
      k
      \begin{vmatrix}
      a_{11} & a_{12} \\
      a_{11} & a_{12}
      \end{vmatrix}
      +
      \begin{vmatrix}
      a_{11} & a_{12} \\
      a_{21} & a_{22}
      \end{vmatrix}\\\\

      &\xlongequal{\text{线性相关}}
      0+
      \begin{vmatrix}
      a_{11} & a_{12} \\
      a_{21} & a_{22}
      \end{vmatrix}
      =
      \begin{vmatrix}
      a_{11} & a_{12} \\
      a_{21} & a_{22}
      \end{vmatrix}
    \end{align*}
    $$

* 重要行列式
  * 主对角线行列式(上下三角行列式)

    $$
    \begin{vmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} \\
    0 & a_{22} & \cdots & a_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & a_{nn}
    \end{vmatrix}
    =
    \begin{vmatrix}
    a_{11} & 0 & \cdots & 0 \\
    a_{21} & a_{22} & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & \cdots & a_{nn}
    \end{vmatrix}
    =
    \begin{vmatrix}
    a_{11} & 0 & \cdots & 0 \\
    0 & a_{22} & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & a_{nn}
    \end{vmatrix}
    =
    \prod_{i=1}^{n} a_{ii}
    $$

  * 副对角线行列式
  
    $$
    \begin{vmatrix}
    a_{11} & \cdots & a_{1,n-1} & a_{1n} \\
    a_{21} & \cdots & a_{2,n-1} & 0 \\
    \vdots & \ddots & \vdots & \vdots \\
    a_{n1} & \cdots & 0 & 0
    \end{vmatrix}
    =
    \begin{vmatrix}
    0 & \cdots & 0 & a_{1n} \\
    0 & \cdots & a_{2,n-1} & a_{2n} \\
    \vdots & \ddots & \vdots & \vdots \\
    a_{n1} & \cdots & a_{n,n-1} & a_{nn}
    \end{vmatrix}
    =
    \begin{vmatrix}
    0 & \cdots & 0 & a_{1n} \\
    0 & \cdots & a_{2,n-1} & 0 \\
    \vdots & \ddots & \vdots & \vdots \\
    a_{n1} & \cdots & 0 & 0
    \end{vmatrix}
    =
    (-1)^{\frac{n(n-1)}{2}} a_{1n} a_{2,n-1} \cdots a_{n1}
    $$

  * 拉普拉斯展开式
  
    设 $A$ 为 $m$ 阶矩阵，$B$ 为 $n$ 阶矩阵，则

    $$
    \begin{align*}
      \begin{vmatrix}
      A_{m\times m} & O \\
      O & B_{n\times n}
      \end{vmatrix}
      =
      \begin{vmatrix}
      A_{m\times m} & C \\
      O & B_{n\times n}
      \end{vmatrix}
      =
      \begin{vmatrix}
      A_{m\times m} & O \\
      C & B_{n\times n}
      \end{vmatrix}
      &=
      \begin{vmatrix}A\end{vmatrix}
      \begin{vmatrix}B\end{vmatrix}\\\\

      \begin{vmatrix}
      O & A_{m\times m} \\
      B_{n\times n} & O
      \end{vmatrix}
      =
      \begin{vmatrix}
      C & A_{m\times m} \\
      B_{n\times n} & O
      \end{vmatrix}
      =
      \begin{vmatrix}
      O & A_{m\times m} \\
      B_{n\times n} & C
      \end{vmatrix}
      &=
      (-1)^{mn}
      \begin{vmatrix}A\end{vmatrix}
      \begin{vmatrix}B\end{vmatrix}
    \end{align*}
    $$

    其中 $O$ 为元素全为 $0$ 的矩阵，但不同的子矩阵 $O$ 形状可能不相同

  * 范德蒙德行列式

    $$
    \begin{vmatrix}
      1 & 1 & \cdots & 1 \\
      x_1 & x_2 & \cdots & x_n \\
      x_1^2 & x_2^2 & \cdots & x_n^2 \\
      \vdots & \vdots & \ddots & \vdots \\
      x_1^{n-1} & x_2^{n-1} & \cdots & x_n^{n-1}
    \end{vmatrix}
    =
    \prod_{1 \leq i < j \leq n} (x_j - x_i)
    $$

    由于 $\begin{vmatrix}A\end{vmatrix}=\begin{vmatrix}A^T\end{vmatrix}$，所以列样式的范德蒙德行列式计算同上

### 1.2 计算

* 具体型
  * 化成基本型

    用性质化出更多的 $0$，找差别不大的行(列)作差，找规律(行和相等行列式)

  * 加边法

    $$
    D_n = \begin{vmatrix}
      a_{11} & a_{12} & \cdots & a_{1n} \\
      a_{21} & a_{22} & \cdots & a_{2n} \\
      \vdots & \vdots & \ddots & \vdots \\
      a_{n1} & a_{n2} & \cdots & a_{nn}
    \end{vmatrix}
    =
    \begin{vmatrix}
      \textcolor{Cyan}{1} & \textcolor{Cyan}{*} & \textcolor{Cyan}{*} & \textcolor{Cyan}{\cdots} & \textcolor{Cyan}{*} \\
      \textcolor{Cyan}{0} & a_{11} & a_{12} & \cdots & a_{1n} \\
      \textcolor{Cyan}{0} & a_{21} & a_{22} & \cdots & a_{2n} \\
      \textcolor{Cyan}{\vdots} & \vdots & \vdots & \ddots & \vdots \\
      \textcolor{Cyan}{0} & a_{n1} & a_{n2} & \cdots & a_{nn}
    \end{vmatrix}
    $$

    加边后用第一列展开行列式不变，可以利用 $(*)$ 来使整个行列式更容易化简

  * 递推法

    $$
    验设证三步走
    \begin{cases}
      F(D_n,D_{n-1})=0,&第一数归法\,(验n=1)\\
      F(D_n,D_{n-1},D_{n-2})=0,&第二数归法\,(验n=1,n=2)
    \end{cases}
    $$

    **递推过程中不要破坏"队形"，也就是确保每降一阶仍然是原先的结构**

  * 行列式表示的函数与方程

    含未知数，按性质计算行列式

* 抽象型

  向量或矩阵缩写为一个变量，由变量组成大矩阵，按行列式性质求解即可

* 余子式与代数余子式的线性组合运算

  $$
  \begin{align*}
    a_{i1}A_{i1} + a_{i2}A_{i2} + \cdots + a_{in}A_{in} &=
    \begin{vmatrix}
       & * &  \\
      a_{i1} & \cdots & a_{in} \\
       & * &
    \end{vmatrix} \\\\

    k_{1}A_{i1} + k_{2}A_{i2} + \cdots + k_{n}A_{in} &=
    \begin{vmatrix}
       & * &  \\
      k_{1} & \cdots & k_{n} \\
       & * &
    \end{vmatrix}
  \end{align*}
  $$

  其中 $*$ 处与原行列式元素相同，当系数为 $a$ 时直接使用原行列式即可；当系数 $k\neq a$ 时，直接将该行元素替换为 $k$，其余行不变即可。**大 $A$ 配小 $a$，逆用展开式；大 $A$ 配小 $k$，$k$ 把小 $a$ 吃**

* 克拉默法则

  对 $n$ 个方程 $n$ 个未知数的非齐次线性方程组

  $$
  \begin{cases}
  a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n &= b_1 \\
  a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n &= b_2 \\
  &\vdots \\
  a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{nn}x_n &= b_n
  \end{cases}
  $$

  若系数行列式
  
  $$
  D=\begin{vmatrix}
  a_{11} & a_{12} & \cdots & a_{1n} \\
  a_{21} & a_{22} & \cdots & a_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  a_{n1} & a_{n2} & \cdots & a_{nn}
  \end{vmatrix}\neq 0
  $$

  则方程组有唯一解，且解为

  $$
  x_i = \frac{D_i}{D}, \quad i=1, 2, \ldots, n
  $$

  其中，$D_i$ 是由常数项 $b_1, b_2, \cdots, b_n$ 替换 $D$ 中第 $i$ 列元素得到的行列式。当 $b_1, b_2, \cdots, b_n$ 全为 $0$ 且 $D\neq 0$ 时，齐次方程组只有零解；当 $b_1, b_2, \cdots, b_n$ 全为 $0$ 且 $D=0$ 时，齐次方程组有非零解；

## 2 进阶

### 2.1 计算行列式 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

* 具体型 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式)}$

  $12+1$ 基本型、加边法、递推法、配合秩(矩阵、方程组、等价、相似、合同等)求解

* 抽象型 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式)}$
  
  利用行列式性质、利用矩阵性质($A^{-1}$、$A^{*}$ 等)、配合相似等理论中有关秩和特征值的操作

  > ⚠️ ***$\det{A}=0$ 的几种可能情况***
  >
  > * $\det{A}=k\det{A},k\neq 0$。常见 $\det{A}=(-1)^n\det{A}$，$n$ 为奇数
  > * $A$ 有特征值为 $0$
  > * $A$ 不满秩，方程组有非零解
  > * 反证法去证 $\det{A}\neq 0$，推出矛盾

### 2.1 计算余子式和代数余子式 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

* 用行列式算 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{21} (观察研究对象)}$

  代数余子式的线性组合

* 用矩阵和特征值算 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{22} (转换等价表述)}$

  利用特征值计算，主要考察矩阵 $A$ 的变化导致的特征值的变化，如 $A^{*},f(A),A^{-1}$ 等。特别注意 $A^{*}$，因为其本身的元素就是 $A$ 的代数余子式，所以求代数余子式之和就是求 $A^{*}$ 的元素和，可以巧妙结合行和相等即为特征值的特点，结合特征值变化方式计算

## 3 题目

* 基础30讲
  * 例1.2(爪型行列式)
  * 例1.3(相似行用-1倍加)
  * ***例1.4(行和相等行列式)***
  * 例1.5(X型行列式)
  * 例1.6(倍加、倍乘、范德蒙德行列式)
  * 例1.7(递推法)
  * 例1.8(可加可拆、倍加)
  * 例1.9(倍加、分析根)
  * 例1.10(倍加、可加可拆)
  * ***例1.11(矩阵系数、行列式乘积)***
  * 例1.12(k吃小a)
  * 例1.13(齐次方程组有非零解、反证法)
* 基础30讲课后题
  * 1.3(计算)
* 1000题基础
  * ***01(行和相等行列式、多项式按根化简)***
  * ***02(拉普拉斯展开式至少存在一个0矩阵)***
  * 04(倍加、可加可拆、根的个数)
* 强化36讲
  * 例1.1(化简求行列式)
  * ***例1.2(利用方程组解的性质求行列式)***
  
    > 硬算效率低，先观察再解题

  * ⭐***例1.3(加边法、秩 $1$ 矩阵)***
  * ***例1.4(第一数归法)***
  * ***例1.5(第二数归法)***
  * 例1.6(行列式性质、正交矩阵、矩阵提系数)
  * ⭐***例1.7(不同变化的特征值、$n$ 阶主子式就是行列式)***
  * ***例1.8(特征值、行和相等行列式)***
  
    > 行和相等行列式：所有列加到统一的一列，然后提列系数，然后行之间倍加相消

  * ***例2.1(代数余子式的线性组合)***
  * ⭐***例2.2-4(代数余子式之和)***
* 1000题强化
  * ⭐***1.5(矩阵分解、E配合可逆)***
  
    > 若 $A$ 可逆，则 $AA^{-1}=E=AEA^{-1}$，紧扣 $AA^{-1}=E$ 来按需扩展单项的 $E$

  * ⭐***1.6(证明向量组线性无关、相似矩阵的特征值相同、用特征值算行列式)***
  
    > 设 $A$ 的特征值为 $\lambda_A$，特征向量为 $\xi$，则 $B=A-kE$ 的特征值为
    $$
    (A-kE)\xi=\lambda_B\xi\Rightarrow A\xi-kE\xi=\lambda_A\xi-kE\xi=(\lambda_A-k)\xi
    $$

  * ***1.7(求特征值多项式)***
  * ***1.8(实对称矩阵一定能相似对角化、相似矩阵秩相等、多项式的特征值)***
  * ***2.2(列出代数余子式方程)***
  
    > 含参情况下可能使用线性组合也不能直接求出来，这时可以制造线性组合的方程组直接求 $A_{ij}$。可以选一个与已知的行线性相关的线性组合使行列式为 $0$，这样就手动制造了一个线性组合的方程，再与已知的线性组合联立求解即可

  * ***2.3($A^{*}$ 的性质)***
