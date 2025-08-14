# 二次型

## 1 知识点

### 1.1 定义

* 二次型

  $n$ 元变量 $x_1, x_2, \cdots, x_n$ 的二次齐次多项式
  
  $$
  \begin{align*}
    f(x_1, x_2, \cdots, x_n) =
    a_{11}x_1^2 + 2a_{12}x_1x_2 + \cdots &+ 2a_{1n}x_1x_n \\
    + a_{22}x_2^2 + \cdots &+ 2a_{2n}x_2x_n \\
    + \cdots & \\
    &+ a_{nn}x_n^2
  \end{align*}
  $$
  
  称为 $n$ 元二次型，简称二次型。令 $a_{ij}=a_{ji}$，有
  
  $$
  \begin{align*}
    A^T=A=\begin{bmatrix}
      a_{11} & a_{12} & \cdots & a_{1n} \\
      a_{21} & a_{22} & \cdots & a_{2n} \\
      \vdots & \vdots & \ddots & \vdots \\
      a_{n1} & a_{n2} & \cdots & a_{nn} \\
    \end{bmatrix}\qquad
    x=\begin{bmatrix}
      x_1 \\
      x_2 \\
      \vdots \\
      x_n
    \end{bmatrix}\\\\
  
    f(x_1,x_2,\cdots,x_n)=\sum^n_{i=1}{\sum^n_{j=1}{a_{ij} x_i x_j}}=x^T A x
  \end{align*}
  $$

  因二次型本身不唯一，因此为了方便研究，令 $A^T=A$，即 $a_{ij}=a_{ji}$。自此二次型具有唯一表示。**特别地，系数矩阵 $A$ 的秩即为二次型 $f(x)$ 的秩**

* 线性变换与合同

  若对二次型换元，令 $x=Cy$，称为**线性变换**；若方阵 $C$ 可逆，则称为**可逆线性变化**。则有
  
  $$
  \begin{align*}
    f(x)=&x^T A x \\
    =&(Cy)^T A (Cy) \\
    =&y^T C^T A C y \\
    =&y^T (C^T A C) y \\
    =&y^T B y=g(y)
  \end{align*}
  $$

  此时，二次型 $f(x)=x^T A x$ 通过线性变换 $x=Cy$ 得到了新二次型 $g(y)=y^T B y$。设 $A,B$ 均为 $n$ 阶矩阵，若存在可逆矩阵 $C$，使得
  
  $$
  C^T A C=B
  $$
  
  则称 $A$ 与 $B$ **合同**，记作 $A\simeq B$，并称其对应的二次型 $f(x),g(y)$ 为**合同二次型**

  > ***合同有如下性质***
  * 若 $A\simeq B$，则 $r(A)=r(B)$。因为 $C$ 可逆，初等变换不改变秩
  * 若 $A\simeq B$，则 $A,B$ 均为对称矩阵。因为 $B^T=\left(C^T A C\right)^T=C^T A^T (C^T)^T=C^T A C=B$

### 1.2 标准形与规范形

* 定义

  若二次型中只含平方项，交叉项系数全为 $0$，形如 $d_1 x^2_1+d_2 x^2_2+\cdots+d_n x^2_n$ 的二次型称为**标准形**
  
  若标准型中系数 $d_i\,(i=1,2,\cdots,n)$ 的取值范围为 $\set{1,-1,0}$，则称为**规范形**

* 定理
  * 任何二次型 $f(x)=x^T A x$ 均能通过 **配方法(作可逆线性变换 $x=Cy$ )** 化成标准形和规范形。即对任意实对称矩阵 $A$，必存在可逆矩阵 $C$，使得 $C^T A C=\Lambda$，其中

    $$
    \underbrace{
      \Lambda=\begin{bmatrix}
        d_1 & & & \\
        & d_2 & & \\
        & & \ddots & \\
        & & & d_n
      \end{bmatrix}
    }_{\textcolor{cyan}{标准型}}
    \quad或\quad
    \underbrace{
      \Lambda=\begin{bmatrix}
        1 & & & & & & & & \\
        & \ddots & & & & & & & \\
        & & 1 & & & & & & \\
        & & & -1 & & & & & \\
        & & & & \ddots & & & & \\
        & & & & & -1 & & & \\
        & & & & & & 0 & & \\
        & & & & & & & \ddots & \\
        & & & & & & & & 0
      \end{bmatrix}
    }_{\textcolor{cyan}{规范形}}
    $$

    仅当 $C^T=C^{-1}$，即 $C$ 是正交矩阵时 $\Lambda$ 才是特征值矩阵
  
  * 任何二次型 $f(x)=x^T A x$ 均能通过 **正交变换( $x=Qy$ )** 化成标准形。即对任意实对称矩阵 $A$，必存在正交矩阵 $Q$，使得 $Q^T A Q=Q^{-1} A Q=\Lambda$，其中
  
    $$
    \Lambda=\begin{bmatrix}
        \lambda_1 & & & \\
        & \lambda_2 & & \\
        & & \ddots & \\
        & & & \lambda_n
    \end{bmatrix}
    $$

    此时 $\Lambda\sim A\simeq\Lambda$，二次型系数矩阵就是特征值正交矩阵

  * **惯性定理**：无论选取什么可逆线性变换将二次型化成标准形或规范形，**标准形或规范形的**正项个数 $p$、负项个数 $q$ 均保持不变。$p$ 称为正惯性指数，$q$ 称为负惯性指数。则二次型的秩 $r(A)=p+q$。两个二次型合同的充要条件为

   $$
   A\simeq B
   \Leftrightarrow\begin{cases}p_A=p_B \\ q_A=q_B\end{cases}
   \Leftrightarrow\begin{cases}r(A)=r(B) \\ p_A=p_B \\ q_A=q_B\end{cases}
   \Leftrightarrow\begin{cases}正特征值个数相同 \\ 负特征值个数相同\end{cases}
   $$

* 化简
  * 配方法
    * 若原式无平方项，则直接进行一次线性变换，利用平方差公式创造出新变量的平方项
    * 从第一个变量开始，将所有带它的项凑成一个平方项。直到所有变量凑完。$n$ 个变量凑完仍然应该是 $n$ 个变量，缺项补 $0$
    * 使用新变量进行线性变换，则新二次型只剩平方项。作反变换得到 $x=Cy$，$C$ 即为所用的可逆线性变换。若刚开始因为没有平方项已经做了一次线性变换，则 $x=C_1 C_2 z$
  
  * 正交变换
    * 写出二次型对应的矩阵 $A$
    * 求正交矩阵 $Q$，使得 $Q^{-1}AQ=\Lambda$(特征值、特征向量、施密特正交化)
    * 令 $x=Qy$，$Q$ 即为所做的正交变换，$f=x^T A x=y^T \Lambda y=\displaystyle\sum^n_{i-1}{\lambda_i y^2_i}$ 即为标准形

* 总结
  * 矩阵等价秩不变；矩阵相似特征多项式相同(即所有 $k$ 阶主子式之和不变)；矩阵合同正负惯性系数不变。等价不限制矩阵情况；相似只讨论方阵；合同只讨论实对称矩阵
  * 相似、合同一定等价，因为变换手段都是可逆矩阵
  * 实对称矩阵相似一定合同，反之未必。因为实对称矩阵存在正交矩阵 $Q$，满足 $Q^{-1} A Q=Q^T A Q=\Lambda$。或理解为相似则特征值相同，所以 $p,q$ 也相同，但合同只能得到 $p,q$ 相同，得不到特征值相同

### 1.3 正定二次型

## 2 题目

* 基础30讲
  * 例6.1(二次型矩阵表达式)
  * ⭐***例6.2(带平方项配方法)***
  * ⭐***例6.3(无平方项配方法)***
  * ⭐***例6.4(正交变换)***
  * 例6.5(特征向量性质)
  * ***例6.6(化简中间量)***
  * 例6.7(惯性指数)
  * 例6.8(惯性指数判断合同、配方法)
  * 例6.9(初等矩阵的转置和逆)
* 基础30讲课后题
* 1000题
