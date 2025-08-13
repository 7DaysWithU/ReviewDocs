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
  
### 1.3 正定二次型

## 2 题目

* 基础30讲
  * 例6.1(二次型矩阵表达式)
* 基础30讲课后题
* 1000题
