# 线性方程组

## 1 知识点

### 1.1 齐次线性方程组

* 有解的条件

  设系数矩阵为 $A_{m\times n}$，则
  
  $$
  \begin{cases}
    r(A)=n,&方程组有唯一零解 \\
    r(A)=r<n,&方程组有无穷多解，且有n-r个线性无关解
  \end{cases}
  $$

* 解的性质
  * 若 $\xi_1,\xi_2$ 为 $Ax=0$ 的解，则 $k_1\xi_1+k_2\xi_2$ 也是 $Ax=0$ 的解。即

    $$
    A(k_1\xi_1+k_2\xi_2)=k_1A\xi_1+k_2A\xi_2=0
    $$

    其中 $k_1,k_2$ 为任意常数
  * 若 $r(A_{m\times n })=n$，则方程组 $Ax=0$ 有唯一零解，若 $AB=AC$，则 $B=C$
  * $Ax=0$ 的解中有 $n-r(A)$ 个线性无关的解向量
  * 系数矩阵的行向量与解向量 $\beta=[b_1,b_2,\cdots,b_n]^T$ 正交。即 $\alpha_i\beta=\alpha_{11}b_1+\alpha_{12}b_2+\cdots+\alpha_{1n}b_n=0$，因为这就是齐次方程组中的一个方程

* 基础解系与解的结构

  设 $\xi_1,\xi_2,\cdots,\xi_{n-r}$ 满足
  
  $$
  \begin{cases}
    是方程组 Ax=0 的解 \\
    互相之间线性无关 \\
    方程组 Ax=0 的任一解均可以由\xi_1,\xi_2,\cdots,\xi_{n-r}线性表示
  \end{cases}
  $$

  则称 $\xi_1,\xi_2,\cdots,\xi_{n-r}$ 为 $Ax=0$ 的**基础解系**；称 $k_1\xi_1,k_2\xi_2,\cdots,k_{n-r}\xi_{n-r}$ 为方程组 $Ax=0$ 的**通解**。其中 $k_1,k_2,\cdots,k_{n-r}$ 为任意常数

* 求解步骤
  * 将系数矩阵 $A$ 作初等行变换变为行阶梯形矩阵 $B$，得 $r(A)=r$
  * 按列找出一个秩为 $r$ 的子矩阵，则剩余列位置的未知数即为自由变量
  * 求出 $\xi_1,\xi_2,\cdots,\xi_{n-r}$
    * $s$ 个解：因为自由变量的个数 $s=n-r$，遂令出 $s$ 个 $\xi_i=[\cdots]^T\,(i=1,2,\cdots,s)$
    * 线性无关：在对应自由变量的位置确定取值使基础解系 $\xi_i$ 线性无关，最简单的方法是取 $E_s$ 对应填入(定理 $7$：原来无关，延长必无关)
    * $\xi_i$ 是解：从最底层行阶梯往上逐阶梯将每个 $\xi_i$ 带入 $Ax=0$ 求出约束变量位置的值
  * 使用 $k_1\xi_1,k_2\xi_2,\cdots,k_{n-r}\xi_{n-r}$ 表示通解。其中 $k_1,k_2,\cdots,k_{n-r}$ 为任意常数

### 1.2 非齐次线性方程组

* 有解的条件

  设系数矩阵为 $A_{m\times n}$，$b$ 为非齐次项，则
  
  $$
  \begin{cases}
    r(A)\neq r([A,b]),&方程组无解 \\
    r(A)=r([A,b])=n,&方程组有唯一解 \\
    r(A)=r([A,b])=r\leq n,&方程组有无穷多解
  \end{cases}
  $$

* 解的性质
  
  若 $\eta_1,\eta_2,\eta$ 为 $Ax=b$ 的解，$\xi$ 对应齐次线性方程组 $Ax=0$ 的解，则
  * 非齐次方程解的差是齐次方程的解：$\eta_1-\eta_2$ 为 $Ax=0$ 的解
  * 非齐次方程解的结构为齐次通解加一个非齐次特解：$k\xi+\eta$ 为 $Ax=b$ 的解
  * $Ax=b$ 的解中有 $n-r(A)+1$ 个线性无关的解向量
  * $\eta,\eta+\xi_1,\eta+\xi_2,\cdots,\eta+\xi_n$ 线性无关

* 求解步骤
  * 求出 $Ax=0$ 的通解 $k_1\xi_1,k_2\xi_2,\cdots,k_{n-r}\xi_{n-r}$
  * 求出 $Ax=b$ 的一个特解 $\eta$
    * 设 $\eta=[\cdots]^T$
    * 令自由变量对应位置的数值为 $0$，方便计算
    * 从最底层行阶梯往上逐阶梯将 $\eta$ 带入 $Ax=b$ 求出约束变量位置的值
  * $Ax=b$ 的解为 $k_1\xi_1,k_2\xi_2,\cdots,k_{n-r}\xi_{n-r}+\eta$。其中 $k_1,k_2,\cdots,k_{n-r}$ 为任意常数

### 1.3 齐次、非齐次方程组公共解

齐次线性方程组 $A_{m \times n}x = 0$ 和 $B_{m \times n}x = 0$ 的公共解是满足方程组 $\begin{bmatrix} A \\ B \end{bmatrix} x = 0$ 的解，即联立求解。同理，$Ax = \alpha$ 与 $Bx = \beta$ 的公共解是满足方程组 $\begin{bmatrix} A \\ B \end{bmatrix} x = \begin{bmatrix} \alpha \\ \beta \end{bmatrix}$ 的解

* 若给出 $A_{m \times n}x = 0$ 的基础解系 $\xi_1, \xi_2, \ldots, \xi_s$ 和 $B$ 的具体表达式，则先写出 $Ax = 0$ 的通解 $k_1\xi_1 + k_2\xi_2 + \cdots + k_s\xi_s$，代入 $B_{m \times n}x = 0$，求出 $k_i (i=1,2,\ldots,s)$ 之间的关系，代回 $A_{m \times n}x = 0$ 的通解，即可得 $Ax = 0$ 与 $Bx = 0$ 的公共解。

* 若给出 $A_{m \times n}x = 0$ 的基础解系 $\xi_1, \xi_2, \ldots, \xi_s$ 与 $B_{m \times n}x = 0$ 的基础解系 $\eta_1, \eta_2, \ldots, \eta_t$，则 $Ax = 0$ 与 $Bx = 0$ 的公共解 $\gamma = k_1\xi_1 + k_2\xi_2 + \cdots + k_s\xi_s = l_1\eta_1 + l_2\eta_2 + \cdots + l_t\eta_t$，即

  $$
  k_1\xi_1 + k_2\xi_2 + \cdots + k_s\xi_s - l_1\eta_1 - l_2\eta_2 - \cdots - l_t\eta_t= 0
  $$

  解此式，求出 $k_i$ 或 $l_j$, $i=1,2,\ldots,s$; $j=1,2,\ldots,t$，即可求出 $\gamma$

### 1.4 同解方程组

* 齐次线性方程组

  若两个**齐次线性方程组** $A_{m\times n}x=0$ 和 $B_{s\times n}x=0$ 有完全相同的解，则称它们为**同解方程组**。有

  $$
  \begin{align*}
    &\qquad Ax=0,Bx=0是同解方程组\\\\
    &\Leftrightarrow\begin{cases}
      Ax=0的基础解系\xi满足Bx=0\\
      Bx=0的基础解系\eta满足Ax=0
    \end{cases}\\\\
    &\Leftrightarrow\xi与\eta是等价向量组\\\\
    &\Leftrightarrow r(A)=r(B)且
    \begin{cases}
      Ax=0的解满足Bx=0&或\\
      Bx=0的解满足Ax=0
    \end{cases}\\\\
    &\xLeftrightarrow{①} r(A)=r(B)=r(\begin{bmatrix}A \\ B\end{bmatrix}) \\\\
    &\xLeftrightarrow{②} A与B的行向量组等价 \\\\
    &\xLeftrightarrow{③}存在矩阵P,Q，满足B=PA，A=QB
  \end{align*}
  $$

  * **特别地，$r(A)=r(B)=r(\begin{bmatrix}A \\ B\end{bmatrix})\not\Leftrightarrow Ax=b$ 与 $Bx=b$ 是同解方程组，因为 $\begin{bmatrix}A\,|\,b\end{bmatrix}\xrightarrow{初等行变换}\begin{bmatrix}B\,|\,b^{'}\end{bmatrix}$，不能确定 $b=b^{'}$，因此 $Ax=b$ 与 $Bx=b$ 解不一定相同，自然不一定是同解方程组**
  * 对 $③$ 的使用：因为 $P,Q$ 不要求是可逆矩阵，但如果找到了 $P$，满足 $B=PA$，且 $P$ 是可逆的，那么就有 $A=P^{-1}B=QB$，一箭双雕，不用再额外找 $Q$ 了。但如果 $P$ 不可逆，就必须同时找到 $P,Q$ 满足 $③$

* 非齐次线性方程组

  若两个**非齐次线性方程组** $A_{m\times n}x=\beta$ 和 $B_{s\times n}x=\gamma$ 均有解，则

  $$
  \begin{align*}
    &\qquad Ax=\beta,Bx=\gamma是同解方程组\\\\
    &\xLeftrightarrow{①} Ax=0,Bx=0同解且Ax=\beta与Bx=\gamma有公共解 \\\\
    &\xLeftrightarrow{②}\underbrace{r(A)=r(B)=r}_{\textcolor{cyan}{齐次同解}}(\begin{bmatrix}A \\ B\end{bmatrix})\underbrace{=r(\left[\begin{array}{c:c}A & \beta \\ B & \gamma\end{array}\right])}_{\textcolor{cyan}{非齐次公共解}} \\\\
    &\xLeftrightarrow{③}[A,\beta]与[B,\gamma]的行向量组等价
  \end{align*}
  $$

## 2 进阶

### 2.1 求线性方程组 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

* 一般问题 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{P}_\text{2} (反证思路)}$

* 公共解问题 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{22} (转换等价表述)}$

* 同解问题 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{22} (转换等价表述)}$

## 3 题目

* 基础30讲
  * ⭐***例4.1(非齐次线性方程组求解)***
  * 例4.2(非齐次线性方程组求解、正交向量、垂直)
  * 例4.3(线性无关解的个数(即自由度))
  * ***例4.4(伴随的秩、基础解系)***
  * ***例4.5(基础解系组合)***
  * 例4.6(非齐次线性方程组有解的条件)
  * ⭐***例4.7(夹逼确定秩、$A_{m\times n}^T A_{m\times n}x=A_{m\times n}^T b$ 必然有解)***
  * 例4.8(非齐次线性方程组有解的条件、解非齐次线性方程组)
  * 例4.9(非齐次线性方程组解的性质)
  * ***例4.10(解与未知数是正交的)***
  * ***例4.11(线性表示、非齐次线性方程解的秩)***
  * ⭐***例4.12(方程组公共解)***
  * 例4.13(同解求未知数)
  * 例4.14(秩相等且可单方向表示证同解)
  * ⭐***例4.15(四秩相同证明、$A_{m\times n}^T A_{m\times n}x=0$ 与 $A_{m\times n}x=0$ 是同解方程组)***
* 基础30讲课后题
  * ***4.6(非齐次线性方程解的结构、夹逼确定秩)***
* 1000题基础
  * 03(秩的性质)
  * ***05(非齐次解的差是齐次的解、$A^T Ax=0$ 与 $Ax=0$ 是同解方程组)***
  * ***06(初等行变换不改变列向量组的线性相关性)***
  * ***07(非齐次方程线性无关解向量个数)***
  * ***09(线性无关向量凑够维度线性表示高维向量)***
* 强化36讲
  * ***例5.1(解的情况、矩阵分解)***
  * ***例5.2(用行列式判断满秩、反对称矩阵的 $x^T A x=0$)***
  * ***例5.3(方程组求解的等价表述)***
  * ⭐***例5.4(公共解问题)***
  
    > 解之前一定先看看能不能通过消元、移项来化简，因为直接硬求计算量大还容易算错

  * ***例5.5(联立方程的秩、秩不等式推导)***
  * ⭐***例5.6(用矩阵表示证明同解)***
  * ⭐***例5.7(用三秩相同证明同解、逆否命题推断)***
  
    > 设有命题 $p,q$，若有 $p\Rightarrow q$，则有 $\overline{q}\Rightarrow\overline{p}$

  * ⭐***例5.8(四秩相同证明同解、逆否命题推断)***
* 1000题强化
  * ***01(矩阵的秩等于行列向量组的秩、原来无关延长也无关)***
  * ***02(正定二次型定义法)***
  * 03(四秩相同)
  
    > 因为四秩相同，所以 $A^T Ax=A^Tb$ 一定有解

  * ⭐***04(根据通解反求系数矩阵、已知基础解系求公共解)***
  * ⭐***05(两种方法证同解、分块矩阵初等变换、用行列式证零解)***
  
    > * 证同解必须熟练三秩相同和向量组等价方法
    > * 证明方程组零解一般看是否满秩，如果是方阵可以看行列式，这样可能更快

  * ⭐***06(向量组 $A$ 表示向量组 $B$ 的表示方法、矩阵方程)***
  
    > 把含参向量组表示问题转换成非齐次方程解的情况，分析参数不同时的秩，即表示方法没有/唯一/无穷多

  * ***08(抽象型方程组凑系数求解)***
