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

    此时 $\Lambda\sim A\simeq\Lambda$，二次型系数矩阵就是特征值正交矩阵。**特别地，正交矩阵是指特征向量两两正交，且任意特征向量的模长为 $1$ 的矩阵，因此求完特征向量后必须 $①$ 施密特正交化 $②$ 单位化**

  * **惯性定理**：无论选取什么可逆线性变换将二次型化成标准形或规范形，**标准形或规范形的**正项个数 $p$、负项个数 $q$ 均保持不变。$p$ 称为正惯性指数，$q$ 称为负惯性指数。则二次型的秩 $r(A)=p+q$。两个二次型合同的充要条件为

    $$
    A\simeq B
    \Leftrightarrow\begin{cases}p_A=p_B \\ q_A=q_B\end{cases}
    \Leftrightarrow\begin{cases}r(A)=r(B) \\ p_A=p_B \\ q_A=q_B\end{cases}
    \Leftrightarrow\begin{cases}正特征值个数相同 \\ 负特征值个数相同\end{cases}
    $$

    **由惯性定理可得，只要获得了二次型的标准形，那么不需要再做额外变换，只需从标准形中读出 $p,q$，就唯一确定了规范形。即对应正负零项填 $+1,-1,0$**

* 化简
  * 拉格朗日配方法
    * 若原式无平方项，则直接进行一次线性变换，利用平方差公式创造出新变量的平方项
    * 从第一个变量开始，将所有带它的项凑成一个平方项。直到所有变量凑完。$n$ 个变量凑完仍然应该是 $n$ 个变量，缺项补 $0$
    * 使用新变量进行线性变换，则新二次型只剩平方项。作反变换得到 $x=Cy$，$C$ 即为所用的可逆线性变换。若刚开始因为没有平方项已经做了一次线性变换，则 $x=C_1 C_2 z$
  
  * 可逆矩阵定义法

    目的是找到可逆矩阵 $C$，使 $C^T A C=\Lambda$，有如下方法

    * 拉格朗日配方法：通过凑平方转化回拉格朗日配方法
    * 成对初等变换(合同对角化)：$\begin{bmatrix}A\,|\,E\end{bmatrix}\xrightarrow{成对初等变换}\begin{bmatrix}\Lambda\,|\,C^T\end{bmatrix}$
  
      > ***证明***
      >
      > 因为 $C$ 可逆，因此 $C$ 可写作若干初等变换矩阵的乘积，即 $C=E_1 E_2\cdots E_k$ ，显然 $C^T=E_k^T \cdots E_2^T E_1^T$ 仍然是若干初等变换矩阵的乘积。由于 $A$ 经过初等行列变换可得到 $\Lambda$，$E$ 经过成对初等变换后可得到 $C^T$(即 $C^T E=E_k^T \cdots E_2^T E_1^T E=C^T$ )，则有 $\begin{bmatrix}A\,|\,E\end{bmatrix}\xrightarrow{成对初等变换}\begin{bmatrix}\Lambda\,|\,C^T\end{bmatrix}$

       </br>

      > ***成对初等变换***
      >
      > 1. $A$ 做列变换进行消元，破坏了对称性，再对 $A$ 补一个行变换保持 $A^T=A$，$E$ 也执行该补充的行变换
      > 2. $A$ 做行变换进行消元，破坏了对称性，再对 $A$ 补一个列变换保持 $A^T=A$，$E$ 什么也不做

  * 正交变换
    * 写出二次型对应的矩阵 $A$
    * 求正交矩阵 $Q$，使得 $Q^{-1}AQ=\Lambda$(特征值、特征向量、施密特正交化)
    * 令 $x=Qy$，$Q$ 即为所做的正交变换，$f=x^T A x=y^T \Lambda y=\displaystyle\sum^n_{i=1}{\lambda_i y^2_i}$ 即为标准形

* 总结
  * 矩阵等价秩不变；矩阵相似特征多项式相同(即所有 $k$ 阶主子式之和不变)；矩阵合同正负惯性系数不变。等价不限制矩阵情况；相似只讨论方阵；合同只讨论实对称矩阵
  * 相似、合同一定等价，因为变换手段都是可逆矩阵
  * 实对称矩阵相似一定合同，反之未必。因为实对称矩阵存在正交矩阵 $Q$，满足 $Q^{-1} A Q=Q^T A Q=\Lambda$。或理解为相似则特征值相同，所以 $p,q$ 也相同，但合同只能得到 $p,q$ 相同，得不到特征值相同

### 1.3 正定二次型

$n$ 元二次型 $f(x_1,x_2,\cdots,x_n)=x^T A x$，若对任意 $x=\begin{bmatrix}x_1,x_2,\cdots,x_n\end{bmatrix}^T\neq 0$ 均有 $x^T A x>0$，则称 $f$ 为正定二次型，对应矩阵 $A$ 为正定矩阵。有

$$
\begin{align*}
  \qquad\qquad\qquad\qquad\qquad&\qquad n元二次型f=x^T A x正定 \\
  \textcolor{cyan}{定义法}&\begin{cases}
    \Leftrightarrow对任意x\neq 0均有x^T A x>0 \\
    \Leftrightarrow A\simeq E
  \end{cases} \\
  \textcolor{cyan}{配方法}&\begin{cases}
    \Leftrightarrow f的正惯性指数p=n
  \end{cases} \\
  \textcolor{cyan}{特征值法}&\begin{cases}
    \Leftrightarrow A的特征值\lambda_i>0\,(i=1,2,\cdots,n)
  \end{cases} \\
  \textcolor{cyan}{可逆矩阵法}&\begin{cases}
    \Leftrightarrow 存在可逆变换将A变为规范形，即C^T A C=E，即A\simeq E \\
    \Leftrightarrow A=(C^T)^{-1} E C^{-1}=(C^T)^{-1}C^{-1}=(C^{-1})^T C^{-1}\xlongequal{令D=C^{-1}}D^T D
  \end{cases} \\
  \textcolor{cyan}{顺序主子式法}&\begin{cases}
    \Leftrightarrow A的顺序主子式均大于0
  \end{cases} \\
  \textcolor{cyan}{必要条件}&\begin{cases}
    \Rightarrow A的主对角线元素a_{ii}>0\,(i=1,2,\cdots,n) \\
    \Rightarrow \begin{vmatrix}A\end{vmatrix}>0
  \end{cases}
\end{align*}
$$

## 2 进阶

### 2.1 二次型 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

* 根据 $f$ 写出 $A$ $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式)}$

  对拥有非对称矩阵的二次型
  
  $$
  f(x)=x^2_1+x^2_2+x^2_3+2x_1x_2+2x_2x_3
  =x^T\begin{bmatrix}
    1 & 2 & 0 \\
    0 & 1 & 2 \\
    0 & 0 & 1
  \end{bmatrix}x
  =x^T B x
  $$
  
  其二次型矩阵为 $A=\dfrac{B+B^T}{2}=\begin{bmatrix}1 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 1\end{bmatrix}$

* ⚠️配方法、正交变换法 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式)}$
  * 区别：配方法的矩阵 $C$ 只要求可逆，正交变换法的 $Q$ 是正交矩阵，是特征向量
  * 伪配方法：非拉格朗日配方法。根据 $x=Cy$ 的变换过程，查看 $C$ 是否可逆，若可逆，则保性质；否则不保性质
  * 正交变换传递性：正交变换也相似，又回到相似的处理上去了：$A\sim B$，$B=\Lambda$ 或 $B\neq\Lambda$

* ⚠️合同 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式)}$
  * 同阶实对称矩阵合同的判定
  
    同阶实对称矩阵合同 $\Leftrightarrow$ 正负惯性指数相同

  * 求可逆矩阵 $C$ 使 $C^TAC=\Lambda$

    先对 $A$ 配方，**再修改配方后的系数使之满足 $\Lambda$**，据此得出可逆矩阵 $C$

  * 求可逆矩阵 $C$ 使 $C^TAC=B\neq\Lambda$

    对 $f(x)=x^TAx$ 配方得到 $C_1$，对 $g(y)=y^TBy$ 配方**并对齐 $f=C^T_1AC_1$ 的系数**得到 $C_2$。因为 $C^T A C=B$，所以 $C_1x=C_2y$，即可得 $x=(C^{-1}_1C_2)y=Cy$

  * 总结
    * 求可逆矩阵 $C$ 的方法是一致的，只不过当 $B=\Lambda$ 时可以少配方一次，因为 $\Lambda$ 已经是配好的了。对齐系数时将多余的因子塞进平方里即可。最后看是谁变到谁，求出对应的 $C$ 或 $C^{-1}$ 即可
    * 若能用正交变换，则既合同也相似
    * 实对称矩阵相似一定合同，合同无法确定相似

* 正定 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式)}$
  * 若 $A$ 正定，则 $A^{-1},A^{*},A^n,kA,C^TAC$ 都正定。其中 $m$ 为正整数，$k>0$
  * 若 $A,B$ 正定，则 $A+B$ 也正定，$\begin{bmatrix}A & O \\ O & B\end{bmatrix}$ 也正定
  * 若 $A,B$ 正定，则 $A,B$ 正定 $\Leftrightarrow AB=BA$

* 二次型最值 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{22} (转换等价表述) + \text{D}_\text{23} (化归经典形式)}$

  若 $Q$ 是 $A$ 的正交矩阵，则有

  $$
  \begin{gather*}
    f(x)=x^T A x\xlongequal{x=Qy}y^T Q^T A Q y=y^T \Lambda y=\sum^n_{i=1}{\lambda_i y_i^2} \\\\
    \min\{\lambda_i\}\sum^n_{i=1}{y_i^2}\leq f(x)=\sum^n_{i=1}{\lambda_i y_i^2}\leq\max\{\lambda_i\}\sum^n_{i=1}{y_i^2}\\\\
    \min\{\lambda_i\}\leq\dfrac{f(x)}{x^Tx}\xlongequal[x^T x=y^T Q^T Q y=y^T y]{x=Qy}\dfrac{\displaystyle\sum^n_{i=1}{\lambda_i y_i^2}}{\displaystyle\sum^n_{i=1}{y_i^2}}\leq\max\{\lambda_i\}
  \end{gather*}
  $$

  据此可以获得 $\dfrac{f(x)}{x^Tx}$ 的最值。**但务必注意，获取最值时使用的是 $y$，因此求最值时先用 $y$ 带入，再带回 $x=Qy$ 获得 $x$**

## 3 题目

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
  * ⭐***例6.10(正定判别法)***
  * ***例6.11(非拉格朗日配方法二次型、正定定义、齐次方程唯一零解)***
  * ***例6.12( $A^{*},A^{-1}$ 正定充要条件)***
* 基础30讲课后题
  * ⭐***6.12(依据正交计算未知特征向量)***
  * 6.13(分类讨论正定)
* 1000题基础
  * ⛔***04(二次型等于0的解、正定判别法、正定二次型的规范形、二次型化规范形)***
  * ***05(二次型合同前提是 $A,B$ 都是实对称矩阵、$(\lambda E-A)\sim(\lambda E-B)$ )***
  * ⛔***09(矩阵分解)***
  * ⭐***12(二次型最值)***
  
    > 求二次型 $f=x^T A x$ 在 $x^T x=\displaystyle\sum^n_{i=1}{x_i^2}=k$ 条件下的最值，$Q$ 是 $A$ 的正交矩阵，有
    >
    > $$
    > x^T A x\xlongequal[x=Qy]{x^T x=k}y^T Q^T A Q y=y^T \Lambda y\xlongequal{x^T x=y^T Q^T Q y=y^T y=k}\displaystyle\sum^n_{i=1}{\lambda_i y_i^2}
    > $$
    >
    > 根据限制条件 $y^T y=k$ 和缩放，显然 $\min\{\lambda_i\}k\leq\displaystyle\sum^n_{i=1}{\lambda_i y_i^2}\leq\max\{\lambda_i\}k$
  
  * ***13(二次型惯性指数、二次型化规范形)***
  * ⭐***15(非拉格朗日配方法求C)***
  * ***16(求未知数时可将具体特征值带入算行列式)***
  * ⭐***20(求 $\dfrac{x^TAx}{x^TBx}$ 的最值、最值点取值)***
  * ***21(依据正交计算未知特征向量)***
  * ***22(方程组个数与变量个数的数量对正定的影响)***
* 强化36讲
  * 例9.1(写二次型矩阵 $A$)
  * 例9.2(通过变形获得二次型矩阵 $A$、向量内积、判断正定)
  * ⭐***例9.3(含参合同条件、求正交矩阵)***
  * ***例9.4(求惯性指数、无平方项配方法)***
  * ***例9.6(伪配方法)***
  * ⭐***例9.7(正交变换也相似、$P^{-1}_1 A P_1=\Lambda=P^{-1}_2 B P_2$)***
  * ⭐***例9.8(求可逆矩阵 $C$ 使 $C^TAC=\Lambda$)***
  * ⭐***例9.9(求可逆矩阵 $C$ 使 $C^TAC=B\neq\Lambda$)***
  * ***例9.10(判断合同与相似)***
  * ⭐***例9.11(求可逆矩阵 $C$ 使 $C^TAC=B\neq\Lambda$、合同与相似)***
  * ***例9.12(判断正定)***
  * ⭐***例9.13($D^TD$ 正定求 $D$)***
  * ⭐***例9.14($P^{-1}P=E$ 逆用、$A^n$ 逆用)***
  
    > 正用都很熟悉，逆用有时能帮大忙。如 $kE=P^{-1}\cdot kE\cdot P$，$A^n=P\Lambda^n P^{-1}\Leftrightarrow\Lambda=P^{-1}\sqrt[n]{A^n}P$

  * ⭐***例9.15(求 $\dfrac{x^TAx}{x^TBx}$ 的最大值)***
* 1000题强化
  * ***04(无平方项配方法、含参讨论惯性指数)***
  * ⭐***10(求正交矩阵 $Q$ 使 $Q^TAQ=B\neq\Lambda$、计算)***
  
    > $A\sim\Lambda\sim B\Leftrightarrow Q^T_1AQ_1=Q^T_2BQ_2$

  * ⛔***11(写二次型矩阵、求最大值、求最大值点)***
  
    > **解题之前先看看 $A$ 是不是实对称矩阵，二次型 $x^TAx$ 的 $A$ 必须是实对称矩阵**

  * ⭐***13(使用同一个矩阵 $P$ 分别将 $A,B$ 化成 $E,\Lambda$)***
  * ⭐⭐⭐⭐⭐***14(写二次型矩阵、求可逆矩阵 $C$ 使 $C^TAC=B\neq\Lambda$)***
  
    > **讨论二次型矩阵必须是实对称矩阵！！！！！！！！！！！！**

  * ⭐***19($D^T D$ 证正定)***
