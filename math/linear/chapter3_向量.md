# 向量

## 1 知识点

### 1.1 向量与向量组

* 向量
  * 定义

    由 $n$ 个数组成的一个有序数组 $[a_1,a_2,\cdots,a_n]$ 称为一个 $n$ 维向量，记作 $\alpha=[a_1,a_2,\cdots,a_n]$，并称 $\alpha$ 为 $n$ 维行向量，则 $\alpha^T$ 为 $n$ 维列向量，其中 $a_i$ 为 向量 $\alpha$ 或 $\alpha^T$ 的第 $i$ 个分量

  * 运算
    * 相等：当向量 $\alpha=[a_1,a_2,\cdots,a_n],\beta=[b_1,b_2,\cdots,b_n]$ 均为 $n$ 维向量且 $a_i=b_i(i=1,2,\cdots,n)$ 时，$\alpha=\beta$
    * 加法：$\alpha+\beta=[a_1+b_1,a_2+b_2,\cdots,a_n+b_n]$
    * 数乘：$k\alpha=[ka_1,ka_2,\cdots,ka_n]$
    * 内积：设 $\alpha=[a_1,a_2,\cdots,a_n]^T,\beta=[b_1,b_2,\cdots,b_n]^T$，则
  
        $$
        \langle\alpha,\beta\rangle=\alpha^T\beta=\sum^n_{i=1}{a_i b_i}
        $$

    * 模：$\begin{Vmatrix}\alpha\end{Vmatrix}=\sqrt{\displaystyle\sum^n_{i=1}{a^2_i}}$，当 $\begin{Vmatrix}\alpha\end{Vmatrix}=1$ 时，称 $\alpha$ 为单位向量

  * 正交
  
    当内积 $\alpha^T\beta=0$ 时，称向量 $\alpha,\beta$ 是正交向量。设矩阵 $A=[\alpha,\beta]$，若满足 $A^T A=E$，则称矩阵 $A$ 为**正交矩阵**。若列向量组 $a_1,a_2,\cdots,a_n$ 满足

    $$
    a^T_i a_j=
    \begin{cases}
        0,&i\neq j \\
        1,&i=j
    \end{cases}
    $$

    则称列向量组 $a_1,a_2,\cdots,a_n$ 为标准或单位正交向量组，也称规范正交基

    * 施密特正交化

      对原向量 $\alpha_1,\alpha2$，其正交基 $\beta_1,\beta_2$、规范正交基 $\gamma_1,\gamma_2$ 为

      $$
      \begin{align*}
        \beta_1&=\alpha_1 \\
        \beta_2&=\alpha_2-\begin{Vmatrix}\alpha_2\end{Vmatrix}\cos{\theta}\cdot\dfrac{\alpha_1}{\begin{Vmatrix}\alpha_1\end{Vmatrix}} \\
        &=\alpha_2-\begin{Vmatrix}\alpha_1\end{Vmatrix}\begin{Vmatrix}\alpha_2\end{Vmatrix}\cos{\theta}\cdot\dfrac{\alpha_1}{\begin{Vmatrix}\alpha_1\end{Vmatrix}^2} \\
        &=\alpha_2-\langle\alpha_1,\alpha_2\rangle\cdot\dfrac{\alpha_1}{\langle\alpha_1,\alpha_1\rangle} \\
        &\xlongequal{\beta_1=\alpha_1}\alpha_2-\dfrac{\langle\alpha_2,\beta_1\rangle}{\langle\beta_1,\beta_1\rangle}\beta_1\\\\

        \gamma_1=\dfrac{1}{\begin{Vmatrix}\beta_1\end{Vmatrix}}&\beta_1\qquad
        \gamma_2=\dfrac{1}{\begin{Vmatrix}\beta_2\end{Vmatrix}}\beta_2
      \end{align*}
      $$

      **原空间的基未必是垂直的，正交化就是将原空间的非垂直基正交化变成垂直的方法，规范正交基则是进一步将正交基的长度变为 $1$，只保留方向**

* 向量组
  * 定义

    设 $m$ 个 $n$ 维向量 $\alpha_1,\alpha_2,\cdots,\alpha_m$ 及 $n$ 个数 $k_1,k_2,\cdots,k_m$，则向量

    $$
    k_1\alpha_1+k_2\alpha_2+\cdots+k_m\alpha_m
    $$

    称为向量组 $\alpha_1,\alpha_2,\cdots,\alpha_m$ 的线性组合。若向量 $\beta$ 能表示为向量组 $\alpha_1,\alpha_2,\cdots,\alpha_m$ 的线性组合，则称向量 $\beta$ 能被该向量组**线性表示**

    * 线性相关

      若存在一组不全为 $0$ 的数 $k_1,k_2,\cdots,k_m$ ，使得

      $$
      k_1\alpha_1+k_2\alpha_2+\cdots+k_m\alpha_m=0 \\\\
      即\qquad\alpha_i=-\dfrac{k_1}{k_i}\alpha_1-\dfrac{k_2}{k_i}\alpha_2-\cdots-\dfrac{k_m}{k_i}\alpha_m
      $$

      则 $\alpha_i$ 可被向量组 $\alpha_1,\alpha_2,\cdots,\alpha_{i-1},\alpha_{i+1},\cdots,\alpha_m$ 表示，这时称向量组 $\alpha_1,\alpha_2,\cdots,\alpha_m$ **线性相关**。显然，含有零向量和成比例向量的向量组必定线性相关

    * 线性无关

      若不存在不全为 $0$ 的数 $k_1,k_2,\cdots,k_m$，使得 $k_1\alpha_1+k_2\alpha_2+\cdots+k_m\alpha_m=0$ 成立，则称向量组 $\alpha_1,\alpha_2,\cdots,\alpha_m$ 线性无关。**注意，向量组要么线性相关，要么线性无关**

  * 线性相关判别定理
    * 定理 $1$

      向量组 $\alpha_1,\alpha_2,\cdots,\alpha_n(n\geq 2)$ 线性相关 $\Leftrightarrow$ 向量组中至少有一个向量可以由其余 $n-1$ 个向量表示

      **逆否命题**：向量组 $\alpha_1,\alpha_2,\cdots,\alpha_n(n\geq 2)$ 线性无关 $\Leftrightarrow$ 向量组中任一向量都不能由其余 $n-1$ 个向量表示

    * 定理 $2$

      若向量组 $\alpha_1,\alpha_2,\cdots,\alpha_n(n\geq 2)$ **线性无关**，且向量组 $\beta,\alpha_1,\alpha_2,\cdots,\alpha_n(n\geq 2)$ 线性相关，则 $\beta$ 可由向量组 $\alpha_1,\alpha_2,\cdots,\alpha_n$ 线性表示，**且表示方法唯一**

    * 定理 $3$

      若向量组 $\beta_1,\beta_2,\cdots,\beta_t$ 可由向量组 $\alpha_1,\alpha_2,\cdots,\alpha_s$ 表示，且 $t>s$，则 $\beta_1,\beta_2,\cdots,\beta_t$ 线性相关

      **等价命题**：若向量组 $\beta_1,\beta_2,\cdots,\beta_t$ 可由向量组 $\alpha_1,\alpha_2,\cdots,\alpha_s$ 表示，且 $\beta_1,\beta_2,\cdots,\beta_t$ 线性无关，则 $s\geq t$

      **总结为：以少表多，多的相关(无论少线性相关与否)；高维能表示低维，低维不能表示高维**

    * 定理 $4$

      设 $m$ 个 $n$ 维向量 $\alpha_1,\alpha_2,\cdots,\alpha_m$，其中

      $$
      \begin{align*}
        方程组为&\quad
        \begin{cases}
          a_{11}x_1 + a_{12}x_2 + \cdots + a_{1m}x_m &= 0 \\
          a_{21}x_1 + a_{22}x_2 + \cdots + a_{2m}x_m &= 0 \\
          &\vdots \\
          a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{nm}x_m &= 0
        \end{cases}\\\\

        向量组为&\quad
        \alpha_1 = \begin{bmatrix} a_{11} \\ a_{21} \\ \vdots \\ a_{n1} \end{bmatrix},
        \alpha_2 = \begin{bmatrix} a_{12} \\ a_{22} \\ \vdots \\ a_{n2} \end{bmatrix},
        \cdots,
        \alpha_m = \begin{bmatrix} a_{1m} \\ a_{2m} \\ \vdots \\ a_{nm} \end{bmatrix}\\\\

        解形式为&\quad
        [\alpha_1,\alpha_2,\cdots,\alpha_m]
        \begin{bmatrix}
          x_1 \\
          x_2 \\
          \vdots \\
          x_m
        \end{bmatrix}=
        x_1\alpha_1+x_2\alpha_2+\cdots+x_m\alpha_m=0
      \end{align*}
      $$

      则有
      * 向量组 $\alpha_1,\alpha_2,\cdots,\alpha_m$ 线性相关 $\Leftrightarrow$ 该齐次线性方程组有非 $0$ 解 $\Leftrightarrow r\left([\alpha_1,\alpha_2,\cdots,\alpha_m]\right)<m$
      * 向量组 $\alpha_1,\alpha_2,\cdots,\alpha_m$ 线性无关 $\Leftrightarrow$ 该齐次线性方程组没有非 $0$ 解 $\Leftrightarrow r\left([\alpha_1,\alpha_2,\cdots,\alpha_m]\right)=m$
      * 任意 $n+1$ 个 $n$ 维向量必然是线性相关的

      对方程组而言，若
      * 方程个数 $n<$ 未知数个数 $m$：齐次线性方程组必有自由未知量，即必有非零解
      * 方程个数 $n=$ 未知数个数 $m$：若系数向量组行列式 $\neq 0$，则只有零解；反之有非零解
      * 方程个数 $n>$ 未知数个数 $m$：若 $r=m$ 则只有零解，$r<m$ 有非零解。$r$ 为向量组的秩

    * 定理 $5$

      设非齐次线性方程组为

      $$
      [\alpha_1,\alpha_2,\cdots,\alpha_m]
      \begin{bmatrix}
        x_1 \\
        x_2 \\
        \vdots \\
        x_m
      \end{bmatrix}=
      x_1\alpha_1+x_2\alpha_2+\cdots+x_m\alpha_m=\beta
      $$

      则有
      * $\beta$ 可以由向量组 $\alpha_1,\alpha_2,\cdots,\alpha_s$ 表示 $\Leftrightarrow$ 非齐次线性方程组有解 $\Leftrightarrow r\left([\alpha_1,\alpha_2,\cdots,\alpha_s]\right)=r\left([\beta,\alpha_1,\alpha_2,\cdots,\alpha_s]\right)$
      * **逆否命题**：$\beta$ 不能由向量组 $\alpha_1,\alpha_2,\cdots,\alpha_s$ 表示 $\Leftrightarrow$ 非齐次线性方程组无解 $\Leftrightarrow r\left([\alpha_1,\alpha_2,\cdots,\alpha_s]\right)+1=r\left([\beta,\alpha_1,\alpha_2,\cdots,\alpha_s]\right)$

    * 定理 $6$

      若向量组 $\alpha_1,\alpha_2,\cdots,\alpha_m$ 中部分向量线性相关，则整个向量组也线性相关

      **逆否命题**：若向量组 $\alpha_1,\alpha_2,\cdots,\alpha_m$ 线性无关，则整个向量组中任一部分向量也线性无关

    * 定理 $7$

      若向量组 $\alpha_1,\alpha_2,\cdots,\alpha_m$ 线性无关，则在对应位置添加任意个分量后新向量组仍然线性无关

      **逆否命题**：若向量组 $\alpha_1,\alpha_2,\cdots,\alpha_m$ 线性相关，则在对应位置去除任意个分量后新向量组仍然线性相关

### 1.2 重要向量组

* 极大线性无关组

  在向量组 $\alpha_1, \alpha_2, \cdots, \alpha_s$ 中，若存在部分组 $\alpha_{i_1}, \alpha_{i_2}, \cdots, \alpha_{i_r}$ 满足
  * $\alpha_{i_1}, \alpha_{i_2}, \cdots, \alpha_{i_r}$ 线性无关
  * 向量组中任一向量 $\alpha_i(i=1, 2, \cdots, s)$ 均可由 $\alpha_{i_1}, \alpha_{i_2}, \cdots, \alpha_{i_r}$ 线性表示
  
  则称向量组 $\alpha_{i_1}, \alpha_{i_2}, \cdots, \alpha_{i_r}$ 是原向量组的极大线性无关组

  **向量组的极大线性无关组一般不唯一，只由一个零向量组成的向量组不存在极大线性无关组，一个线性无关向量组的极大线性无关组就是该向量组本身**

* 等价向量组

  设两个向量组: $(\text{I})\alpha_1, \alpha_2, \cdots, \alpha_s$, $(\text{II})\beta_1, \beta_2, \cdots, \beta_t$. 若 $(\text{I})$ 中每个向量 $\alpha_i (i=1, 2, \cdots, s)$ 均可由 $(\text{II})$ 中向量线性表示，则称向量组 $(\text{I})$ 可由向量组 $(\text{II})$ 线性表示；若向量组 $(\text{I}),(\text{II})$ 可以相互线性表示，则称向量组 $(\text{I})$ 与向量组 $(\text{II})$ 是等价向量组，记作 $(\text{I})\cong(\text{II})$。等价的充要条件为
  
  $$
  (\text{I})\cong(\text{II})\Leftrightarrow
  \begin{cases}
    (\text{I})可由(\text{II})表示\\
    (\text{II})可由(\text{I})表示
  \end{cases}\Leftrightarrow
  \begin{cases}
    r(\text{I})=r(\text{II})\\
    可以单方向表示
  \end{cases}\Leftrightarrow
  r(\text{I})=r(\text{II})=r(\text{I}\,|\,\text{II})
  $$

  **向量组等价要求向量同维且三秩相等，但向量个数可以不等；矩阵等价要求同型且二秩相等**
  
  等价向量组满足
  * 自反、对称、传递
  * 向量组与它的极大线性无关组等价
  
* 向量组的秩

  向量组 $\alpha_1, \alpha_2, \cdots, \alpha_s$ 的极大线性无关组 $\alpha_{i_1}, \alpha_{i_2}, \cdots, \alpha_{i_r}$ 中所含的向量个数 $r$ 即为向量组的秩，记作
  
  $$
  r(\alpha_1, \alpha_2, \cdots, \alpha_s)=r(\alpha_{i_1}, \alpha_{i_2}, \cdots, \alpha_{i_r})
  $$

  **等价向量组秩相同(三秩相同)；但向量组秩相同未必等价( $r(\text{I}\,|\,\text{II})\xlongequal{?}r(\text{I})$ )**

  秩有如下性质
  * $矩阵A的秩=A的行向量组的秩=A的列向量组的秩$
  * 若 $A\xrightarrow{初等行变换}B$，则
    * $A的行向量组 \cong B的行向量组$
    * $A,B$ 任何相应的列向量组具有相同的线性相关性
  * 设向量组 $\alpha_1, \alpha_2, \cdots, \alpha_s$ 及 $\beta_1, \beta_2, \cdots, \beta_t$，若任意 $\beta_i(i=1,2,\cdots,t)$ 均可由 $\alpha_1, \alpha_2, \cdots, \alpha_s$ 线性表示，则 $r(\beta_1, \beta_2, \cdots, \beta_t) \leq r(\alpha_1, \alpha_2, \cdots, \alpha_s)$，因为高维兼容低维
  
### 1.3 向量空间

* 定义

  若 $\xi_1, \xi_2, \cdots, \xi_n$ 是 $n$ 维向量空间 $\mathbb{R}^n$ 中的线性无关的有序向量组，则任一向量 $\alpha \in \mathbb{R}^n$ 均可由 $\xi_1, \xi_2, \cdots, \xi_n$ 线性表示(即 $\xi_1, \xi_2, \cdots, \xi_n$ 可以张成这个 $n$ 维空间 $\mathbb{R}^n$)，记为

  $$
  \alpha = a_1\xi_1 + a_2\xi_2 + \cdots + a_n\xi_n,
  $$

  称有序向量组 $\xi_1, \xi_2, \cdots, \xi_n$ 是 $\mathbb{R}^n$ 的一个基，基向量的个数 $n$ 称为向量空间的维数，而 $[a_1, a_2, \cdots, a_n]([a_1, a_2, \cdots, a_n]^T)$ 称为向量 $\alpha$ 在基 $\xi_1, \xi_2, \cdots, \xi_n$ 下的坐标，或称为 $\alpha$ 的坐标行(列)向量

* 定理

  * 定理 $8$
  
    若 $\eta_1, \eta_2, \cdots, \eta_n$ 和 $\xi_1, \xi_2, \cdots, \xi_n$ 是 $\mathbb{R}^n$ 中的两个基，且有关系

    $$
    [\eta_1, \eta_2, \cdots, \eta_n] = [\xi_1, \xi_2, \cdots, \xi_n]
    \begin{bmatrix}
    c_{11} & c_{12} & \cdots & c_{1n} \\
    c_{21} & c_{22} & \cdots & c_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    c_{n1} & c_{n2} & \cdots & c_{nn}
    \end{bmatrix}
    = [\xi_1, \xi_2, \cdots, \xi_n] C
    \tag{*}
    $$

    则 $(*)$ 式称为由基 $\xi_1, \xi_2, \cdots, \xi_n$ 到基 $\eta_1, \eta_2, \cdots, \eta_n$ 的**基变换公式**，矩阵 $C$ 称为由基 $\xi_1, \xi_2, \cdots, \xi_n$ 到基 $\eta_1, \eta_2, \cdots, \eta_n$ 的**过渡矩阵**，$C$ 的第 $i$ 列即是 $\eta_i$ 在基 $\xi_1, \xi_2, \cdots, \xi_n$ 下的坐标，**且过渡矩阵 $C$ 是可逆矩阵**。即

    $$
    \begin{cases}
      \eta_1 &= c_{11}\xi_1 + c_{21}\xi_2 + \cdots + c_{n1}\xi_n, \quad [c_{11}, c_{21}, \cdots, c_{n1}] \text{ 为 } \eta_1 \text{ 在 } \xi_1, \xi_2, \cdots, \xi_n \text{ 下的坐标} \\
      \eta_2 &= c_{12}\xi_1 + c_{22}\xi_2 + \cdots + c_{n2}\xi_n, \quad [c_{12}, c_{22}, \cdots, c_{n2}] \text{ 为 } \eta_2 \text{ 在 } \xi_1, \xi_2, \cdots, \xi_n \text{ 下的坐标} \\
      &\vdots \\
      \eta_n &= c_{1n}\xi_1 + c_{2n}\xi_2 + \cdots + c_{nn}\xi_n, \quad [c_{1n}, c_{2n}, \cdots, c_{nn}] \text{ 为 } \eta_n \text{ 在 } \xi_1, \xi_2, \cdots, \xi_n \text{ 下的坐标}
    \end{cases}
    $$

  * 定理 $9$

    设 $\alpha$ 在基 $\xi_1, \xi_2, \cdots, \xi_n$ 和基 $\eta_1, \eta_2, \cdots, \eta_n$ 下的坐标分别是 $x = [x_1, x_2, \cdots, x_n]^T$, $y = [y_1, y_2, \cdots, y_n]^T$，即

    $$
    \alpha = [\xi_1, \xi_2, \cdots, \xi_n] x = [\eta_1, \eta_2, \cdots, \eta_n] y
    $$

    又由基 $\xi_1, \xi_2, \cdots, \xi_n$ 到基 $\eta_1, \eta_2, \cdots, \eta_n$ 的过渡矩阵为 $C$，即

    $$
    [\eta_1, \eta_2, \cdots, \eta_n] = [\xi_1, \xi_2, \cdots, \xi_n] C
    $$

    则

    $$
    \alpha = [\xi_1, \xi_2, \cdots, \xi_n] x = [\eta_1, \eta_2, \cdots, \eta_n] y = [\xi_1, \xi_2, \cdots, \xi_n] Cy
    $$

    即

    $$
    x = Cy \quad \text{或} \quad y = C^{-1}x.
    \tag{**}
    $$

    当使用新的基时，向量在不同基下的坐标发生改变。$(**)$ 式称为**坐标变换公式**

## 2 题目

* 基础30讲
  * 例3.1(行阶梯形求秩、线性相关判别定理5、方程组求解)
  * 例3.2(线性相关判别定理2，6)
  * 例3.3(线性相关判别定理、线性相关定义、线性表示)
  * 例3.4(等价向量组)
  * ***例3.5(行列情况与线性相关与否、范德蒙德行列式)***
  * ***例3.6(线性无关证明)***
  * ⭐***例3.7(向量组求极大线性无关组)***
  * ***例3.8(极大线性无关组乘行阶梯形)***
  * 例3.9-11(秩定理证明、高维表示低维)
  * ***例3.12(矩阵等价、向量组等价)***
  * 例3.13(过渡矩阵、坐标变换公式)
  * ***例3.14(施密特正交化)***
* 基础30讲课后题
  * 3.3(定理5、系数矩阵法)
  * ***3.8(定理2、由极大线性无关组表示的向量才是唯一解、求方程组)***
  * ⭐***3.9(极大线性无关组)***
  * 3.12(待定系数法解方程组)
* 1000题
  * 05(充分必要条件，左乘列满秩不改变秩)
  * ***10(施密特正交化)***
