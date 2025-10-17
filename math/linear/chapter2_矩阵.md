# 矩阵

## 1 知识点

### 1.1 定义与基本运算

* 定义

  由 $m \times n$ 个数 $a_{ij}$ ($i=1,2,\cdots,m$; $j=1,2,\cdots,n$) 排成的 $m$ 行 $n$ 列的矩形表格

  $$
  \begin{bmatrix}
  a_{11} & a_{12} & \cdots & a_{1n} \\
  a_{21} & a_{22} & \cdots & a_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  a_{m1} & a_{m2} & \cdots & a_{mn}
  \end{bmatrix}
  $$

  称为一个 $m\times n$ 矩阵，记作 $A$ 或 $(a_{ij})_{m\times n }\,(i=1,2,\cdots,m$; $j=1,2,\cdots,n)$。当 $m=n$ 时，称为**方阵**。当矩阵 $A,B$ 行数和列数相同时，称 $A$ 与 $B$ 是**同型矩阵**

* 运算
  * 相等：矩阵 $A$ 与矩阵 $B$ 是同型矩阵的基础上，且对应元素都相等
  
  * 线性运算
    * 加法：矩阵 $A$ 与矩阵 $B$ 是同型矩阵时可以相加，即

      $$
      C=A+B=(a_{ij})_{m\times n }+(b_{ij})_{m\times n }=(c_{ij})_{m\times n }
      $$

    * 数乘矩阵：设 $k$ 是一个数，$A$ 是一个 $m \times n$ 矩阵。数 $k$ 和 $A$ 的乘积称为数乘矩阵，即

      $$
      kA = Ak = (ka_{ij})_{m\times n } = k
      \begin{bmatrix}
        a_{11} & a_{12} & \cdots & a_{1n} \\
        a_{21} & a_{22} & \cdots & a_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{m1} & a_{m2} & \cdots & a_{mn}
      \end{bmatrix}
      =
      \begin{bmatrix}
        ka_{11} & ka_{12} & \cdots & ka_{1n} \\
        ka_{21} & ka_{22} & \cdots & ka_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        ka_{m1} & ka_{m2} & \cdots & ka_{mn}
      \end{bmatrix}
      $$

    * 线性运算规律
      * 交换律：$A + B = B + A$
      * 结合律：$(A + B) + C = A + (B + C)$
      * 分配律：$k(A + B) = kA + kB$，$(k + l)A = kA + lA$
      * 数和矩阵相乘的结合律：$k(lA) = (kl)A = l(kA)$

  * 矩阵乘法

    设 $A$ 是一个 $m \times s$ 矩阵，$B$ 是一个 $s \times n$ 矩阵(矩阵 $A$ 的列数必须与矩阵 $B$ 的行数相等)，则 $A$，$B$ 可以相乘，乘积 $AB$ 是 $m \times n$ 矩阵，记 $C = AB = (c_{ij})_{m \times n}$。$C$ 的第 $i$ 行第 $j$ 列元素 $c_{ij}$ 是 $A$ 的第 $i$ 行的 $s$ 个元素与 $B$ 的第 $j$ 列的 $s$ 个对应元素两两乘积之和，即

    $$
    c_{ij} = \sum_{k=1}^{s} a_{ik} b_{kj}\,(i=1,2,\cdots,m; \ j=1,2,\cdots,n)
    $$

    * 结合律：$(A_{m\times s} B_{s\times r}) C_{r\times n} = A_{m\times s} (B_{s\times r} C_{r\times n})$;
    * 分配律： $\begin{cases}A_{m\times s} (B_{s\times n} + C_{s\times n}) = A_{m\times s} B_{s\times n} + A_{m\times s} C_{s\times n} \\ (A_{m\times s} + B_{m\times s}) C_{s\times n} = A_{m\times s} C_{s\times n} + B_{m\times s} C_{s\times n}\end{cases}$
    * 数乘与矩阵乘积的结合律：$(kA_{m\times s}) B_{s\times n} = A_{m\times s} (kB_{s\times n}) = k(A_{m\times s} B_{s\times n})$
    * 不满足交换律： $AB\neq BA$
    * $AB=O\not\Rightarrow A= O\,或\,B= O$
    * $AB=AC\Rightarrow A(B-C)=O$，即使 $A=O$，也得不到 $B-C=O$ 的结论

  * 转置矩阵

    将 $m\times n$ 矩阵 $A$ 的行列互换得到的 $n\times m$ 矩阵称为 $A$ 的转置矩阵，记作 $A^T$

    * $(A^T)^T = A$
    * $(kA)^T = kA^T$
    * $(A + B)^T = A^T + B^T$
    * $(ABC)^T = C^T B^T A^T$
    * $A^T A$ 必为方阵

  * 方阵的幂

    $n$ 阶方阵 $A$ 的 $k$ 次幂为 $A^k=\overbrace{AA\cdots A}^{k个A}$

    * 因矩阵乘法不满足交换律，故一般地，

      $$
      \begin{align*}
        &(A+B)^2 = (A+B)(A+B) = A^2 \underbrace{+ AB + BA}_{\textcolor{cyan}{\text{注意这里}}} + B^2 \neq A^2 + 2AB + B^2, \\
        &(A-B)^2 = A^2 \underbrace{- AB - BA}_{\textcolor{cyan}{\text{注意这里}}} + B^2 \neq A^2 - 2AB + B^2, \\
        &(A+B)(A-B) = A^2 \underbrace{- AB + BA}_{\textcolor{cyan}{\text{注意这里}}} - B^2 \neq A^2 - B^2, \\
        &(AB)^m = \overbrace{(AB)(AB)\cdots(AB)}^{m\text{个}} \neq A^mB^m.
      \end{align*}
      $$

    * 若 $f(x) = a_0 + a_1x + \cdots + a_mx^m$，则

      $$
      f(A) = a_0E + a_1A + \cdots + a_mA^m. \quad 因为 AE = EA = A.
      $$

    * 高幂次乘法时，可将 $A$ 分解为 $\alpha\beta^T$，再利用乘法结合律将中间的相乘次序改变得到常数

  * 方阵行列式

    * $\begin{vmatrix}kA\end{vmatrix} = k^n\begin{vmatrix}A\end{vmatrix} \neq k \begin{vmatrix}A\end{vmatrix}$ ($n \geq 2$, $k \neq 0,1$)
    * 若 $A, B$ 是同阶方阵，则 $\begin{vmatrix}AB\end{vmatrix} = \begin{vmatrix}A\end{vmatrix}\begin{vmatrix}B\end{vmatrix}$
    * 一般地，$\begin{vmatrix}A+B\end{vmatrix} \neq \begin{vmatrix}A\end{vmatrix} + \begin{vmatrix}B\end{vmatrix}$
    * $A \neq O \not\Rightarrow \begin{vmatrix}A\end{vmatrix} \neq 0$
    * $A \neq B \not\Rightarrow \begin{vmatrix}A\end{vmatrix} \neq \begin{vmatrix}B\end{vmatrix}$
    * $\begin{vmatrix}A^T\end{vmatrix} = \begin{vmatrix}A\end{vmatrix}$

  * 分块矩阵

    按行(列)划分成若干块，每块视作一个元素

    * 加法：两个矩阵的分块方法需一致，且块之间同型
    * 数乘：同普通数乘
    * 乘法：在普通乘法的基础上，每项中 $A$ 的块必须在前，因为乘法不满足交换律
    * 幂：若 $A,B$ 分别为 $m,n$ 阶方阵，则分块对角矩阵的幂为

      $$
      \begin{bmatrix}
        A & O \\
        O & B
      \end{bmatrix}^n=
      \begin{bmatrix}
        A^n & O \\
        O & B^n
      \end{bmatrix}
      $$

* 重要矩阵
  * 零矩阵
  
    任意形状且所有元素为 $0$ 的矩阵为零矩阵，记作 $O$

  * 单位矩阵

    主对角线元素全为 $1$、其余元素全为 $0$ 的 $n$ 阶方阵称为 $n$ 阶单位矩阵，记作 $E$ 或 $E_n$

  * 数量矩阵

    常数 $k$ 与单位矩阵 $E$ 的乘积称为数量矩阵。特别地，$A\times kE=kE\times A$

  * 对角矩阵

    非主对角线元素全为 $0$ 的矩阵称为对角矩阵，记作 $\Lambda$

  * 上(下)三角矩阵

    当 $i>j\,(i<j)$ 时，$a_{ij}=0$ 的矩阵称为上(下)三角矩阵

  * ⚠️ $\text{Gram}$ 矩阵

    对 $m \times n$ 的实数矩阵 $A$，其列向量为 $\alpha_1, \alpha_2, \dots, \alpha_n$(即每个 $\alpha_i$ 是一个 $m$ 维向量)。则 $\text{Gram}$ 矩阵  $G$ 是一个 $n$ 阶方阵，表示各列向量之间的内积

    $$
    G = A^T A =
    \begin{bmatrix}
      \alpha_1^T \alpha_1 & \alpha_1^T \alpha_2 & \cdots & \alpha_1^T \alpha_n \\
      \alpha_2^T \alpha_1 & \alpha_2^T \alpha_2 & \cdots & \alpha_2^T \alpha_n \\
      \vdots & \vdots & \ddots & \vdots \\
      \alpha_n^T \alpha_1 & \alpha_n^T \alpha_2 & \cdots & \alpha_n^T \alpha_n
    \end{bmatrix}=
    \begin{bmatrix}
      \langle \alpha_1, \alpha_1 \rangle & \langle \alpha_1, \alpha_2 \rangle & \cdots & \langle \alpha_1, \alpha_n \rangle \\
      \langle \alpha_2, \alpha_1 \rangle & \langle \alpha_2, \alpha_2 \rangle & \cdots & \langle \alpha_2, \alpha_n \rangle \\
      \vdots & \vdots & \ddots & \vdots \\
      \langle \alpha_n, \alpha_1 \rangle & \langle \alpha_n, \alpha_2 \rangle & \cdots & \langle \alpha_n, \alpha_n \rangle
    \end{bmatrix}
    $$

    其中，$\langle \alpha_i\,,\alpha_j \rangle=\begin{Vmatrix}\alpha_i\end{Vmatrix}\begin{Vmatrix}\alpha_j\end{Vmatrix}\cos{\theta_{ij}}\,(i,j=1,2,\cdots,n)$，$\cos{\theta_{ij}}$ 用于度量 $\alpha_i\,,\alpha_j$ 的相似度，即余弦相似度

    * **$A A^T$ 研究行向量之间的相似度，$A^T A$ 研究列向量之间的相似度**。矩阵 $A$ 由列向量组成，因此研究的是列向量间的相似度，因此 $\text{Gram}$ 矩阵为 $A^T A$
    * 对任意矩阵 $A_{m\times n}$，其 $\text{Gram}$ 矩阵必定为 $n$ 阶对称方阵
    * $\mathrm{tr}{(A^T A)}=\mathrm{tr}{(A A^T)}$。因为主对角线都是 $\langle \alpha_i\,,\alpha_i \rangle$
    * 若 $A^T A=\Lambda$，则单个向量的模长就是对应主对角线元素的平方，且向量之间两两正交
    * $Ax=0$ 与 $A^T Ax=0$ 是同解方程组

  * 对称矩阵

    若矩阵 $A$ 满足 $A^T=A$，则称 $A$ 为对称矩阵。特别地，$\text{Gram}$ 矩阵为对称矩阵，因为 $\left(A^T A\right)^T\xlongequal{(AB)^T=B^T A^T}A^T \left(A^T\right)^T\xlongequal{(A^T)^T=A}A^T A$

  * 反对称矩阵

    若矩阵 $A$ 满足 $A^T=-A$，则称 $A$ 为反对称矩阵。显然有 $\begin{cases}a_{ij}=-a_{ji},&i\neq j \\ a_{ii}=0,&i=j\end{cases}$

  * 行(列)矩阵

    只有一行(列)元素的矩阵，也称行(列)向量。**特别地，对列向量 $A_{m\times 1}$，$A^T A$ 是一个数(即内积)；$A A^T$ 是 $n$ 阶方阵**。使用乘法结合律在幂次运算时可将方阵大量化简为常数

  * ⚠️秩 $1$ 矩阵

    设 $\alpha=[x_1,x_2,\cdots,x_n]^T,\,\alpha\neq 0$，则 $\alpha\alpha^T$ 必然是秩 $1$ 矩阵，因为 $\alpha\alpha^T$ 每列都是关于 $\alpha$ 的倍数，整个矩阵线性相关

    秩 $1$ 矩阵 $A$ 的特征值为 $\begin{cases}\lambda_1=\lambda_2=\cdots=\lambda_{n-1}=0 \\ \lambda_n=\text{tr}(A)\end{cases}$

    秩 $1$ 矩阵 $A$ 的 $k$ 次幂为 $A^n=\big[\mathrm{tr}(A)\big]^{n-1}A$

### 1.2 矩阵的逆

* 定义

  $A,B$ 均为 $n$ 阶方阵，若 $AB=BA=E_n$，则称 $A$ 是可逆矩阵，并称 $B$ 是 $A$ 的逆矩阵，且逆矩阵唯一，记作 $A^{-1}$。**重要地，$A$ 可逆 $\Leftrightarrow\begin{vmatrix}A\end{vmatrix}\neq 0$**

* 性质

  设 $A,B$ 均为 $n$ 阶可逆矩阵，则
  * $(A^{-1})^{-1}=A$
  * 若 $k\neq 0$，则 $(kA)^{-1}=\dfrac{1}{k}A^{-1}$
  * $ABC$ 同样可逆，且 $(ABC)^{-1}=C^{-1}B^{-1}A^{-1}$
  * $A^T$ 同样可逆，且 $(A^T)^{-1}=(A^{-1})^T$
  * $\begin{vmatrix}A^{-1}\end{vmatrix}=\begin{vmatrix}A\end{vmatrix}^{-1}$

* 求逆矩阵
  * 定义法：求出 $B$，使得 $AB=E$
  * 分解法：将 $A$ 分解为若干可逆矩阵的乘积，则 $A$ 就可逆；再利用穿透原则求这若干项乘积的逆即为 $A$ 的逆

### 1.3 伴随矩阵

* 定义

  将行列式 $\begin{vmatrix}A\end{vmatrix}$ 的 $n^2$ 个元素的代数余子式按如下形式排成的矩阵称为 $A$ 的伴随矩阵，记作 $A^*$，即

  $$
  A^* =
  \begin{bmatrix}
    A_{11} & A_{21} & \cdots & A_{n1} \\
    A_{12} & A_{22} & \cdots & A_{n2} \\
    \vdots & \vdots & \ddots & \vdots \\
    A_{1n} & A_{2n} & \cdots & A_{nn}
  \end{bmatrix}
  $$

  且有 $A^* A=A A^*=\begin{vmatrix}A\end{vmatrix}E$

* 性质
  * $A^*=\begin{vmatrix}A\end{vmatrix}A^{-1}$，$A^{-1}=\dfrac{1}{\begin{vmatrix}A\end{vmatrix}}A^*$，$A=\begin{vmatrix}A\end{vmatrix}(A^*)^{-1}$
  * $(狗)(狗^*)=\begin{vmatrix}狗\end{vmatrix}E$
  * $kA^{*}=k^{n-1}A^{*}$
  * $\begin{vmatrix}A^*\end{vmatrix}=\begin{vmatrix}A\end{vmatrix}^{n-1}$，$(A^*)^*=\begin{vmatrix}A\end{vmatrix}^{n-2}A,\begin{vmatrix}(A^*)^{*}\end{vmatrix}=\begin{vmatrix}A\end{vmatrix}^{(n-1)^2}$
  * $(A^*)^{-1}=(A^{-1})^*$，$(A^T)^*=(A^*)^T$
  * $(ABC)^*=C^* B^* A^*$

* 求逆矩阵
  * 确定 $\begin{vmatrix}A\end{vmatrix}\neq 0$ 以保证 $A$ 有逆
  * 根据 $A$ 写出 $A^*$
  * 利用 $A^{-1}=\dfrac{1}{\begin{vmatrix}A\end{vmatrix}}A^*$ 求得逆

### 1.4 初等变换与初等矩阵

* 初等矩阵定义
  
  对单位矩阵 $E$ 经过一次初等变换得到的矩阵为初等矩阵，具体变换为
  
  * 倍乘：$E_i(k)\,(k\neq 0)$，在 $E$ 的第 $i$ 行(列)乘 $k$ 倍
  * 换行：$E_{ij}$，将 $E$ 的第 $i,j$ 行(列)互换
  * 倍加：$E_{ij}(k)$，将 $E$ 的第 $j$ 行的 $k$ 倍加到第 $i$ 行上(或将 $E$ 的第 $i$ 列的 $k$ 倍加到第 $j$ 列上)

  **左行右列：初等矩阵在 $A$ 左边则 $A$ 进行行变换；初等矩阵在 $A$ 右边则 $A$ 进行列变换**

* 初等矩阵性质
  * 初等矩阵的转置仍然是初等矩阵，且 $\begin{cases} \left[E_i\left(k\right)\right]^T=E_i(k) \\ \left[E_{ij}\right]^T=E_{ij} \\ \left[E_{ij}\left(k\right)\right]^T=E_{ji}(k) \end{cases}$
  * 因为 $\begin{cases} \begin{vmatrix}E_i(k)\end{vmatrix}=k\neq 0 \\ \begin{vmatrix}E_{ij}\end{vmatrix}=-1\neq 0 \\ \begin{vmatrix}E_{ij}(k)\end{vmatrix}=1\neq 0 \end{cases}$，所以初等矩阵都可逆，则 $\begin{cases} \left[E_i\left(k\right)\right]^{-1}=E_i(\dfrac{1}{k}) \\ \left[E_{ij}\right]^{-1}=E_{ij} \\ \left[E_{ij}\left(k\right)\right]^{-1}=E_{ij}(-k) \end{cases}$
  * 根据 $A^{*}=\begin{vmatrix}A\end{vmatrix}A^{-1}$，对应行列式和逆可以获得初等矩阵的伴随矩阵
  * 若 $A$ 是可逆矩阵，则 $A$ 可以表示为有限个初等矩阵的乘积

* 求逆矩阵

  若 $A$ 是可逆矩阵，则 $A$ 可以表示为有限个初等矩阵的乘积，即
  
  $$
  \begin{align*}
    A=&P_1 P_2 \cdots P_n \\
    P^{-1}_n \cdots P^{-1}_2 P^{-1}_1 A=&P^{-1}_n \cdots P^{-1}_2 P^{-1}_1 P_1 P_2 \cdots P_n \\
    Q_n \cdots Q_2 Q_1 A=&E \\
    Q_n \cdots Q_2 Q_1 A A^{-1}=&E A^{-1} \\
    Q_n \cdots Q_2 Q_1 E=&A^{-1}
  \end{align*}
  $$

  因此注意到第 $3,5$ 行，当使用同一个初等矩阵变换序列 $Q_n \cdots Q_2 Q_1$ 时，$A$ 变换为 $E$，$E$ 变换为 $A^{-1}$。结合左行右列性质，有
  
  $$
  \begin{align*}
    \begin{bmatrix}
      A \, \vdots \, E
    \end{bmatrix}
    &\xlongequal{初等行变换}
    \begin{bmatrix}
      E \, \vdots \, A^{-1}
    \end{bmatrix} \\\\
  
    \begin{bmatrix}
      A \\
      \cdots \\
      E
    \end{bmatrix}
    &\xlongequal{初等列变换}
    \begin{bmatrix}
      E \\
      \cdots \\
      A^{-1}
    \end{bmatrix}
  \end{align*}
  $$

* 行阶梯形矩阵、行最简阶梯形矩阵
  * 行阶梯形矩阵

    若有零行(即元素全为零的行)，则零行全都位于非零行的下方；各非零行左起第一个非零元素的列指标由上至下是严格增大的

  * 行最简阶梯形矩阵
  
    若行阶梯形矩阵非零行的第一个非零元素为 $1$，并且这些非零元素所在列的其他元素均为 $0$，则称为行最简阶梯形矩阵

  * 性质

    对任何非零矩阵 $A$，总可以经过有限次初等行变换将其化为行阶梯型矩阵和行最简阶梯形矩阵。可逆矩阵的行最简阶梯形矩阵是单位矩阵，因为

    $$
    可逆\Leftrightarrow行列式\neq 0\Leftrightarrow n阶子式\neq 0\Leftrightarrow r=n\Leftrightarrow行最简阶梯形矩阵=E_n
    $$

* 分块矩阵的逆

  $$
  \begin{align*}
    若A=
    \begin{bmatrix}
      A_1 & & &\\
      & A_2 & &\\
      & & \ddots & \\
      & & & A_s
    \end{bmatrix},\quad
    则A^{-1}=
    \begin{bmatrix}
      A^{-1}_1 & & &\\
      & A^{-1}_2 & &\\
      & & \ddots & \\
      & & & A^{-1}_s
    \end{bmatrix} \\\\

    若A=
    \begin{bmatrix}
      & & & A_1 \\
      & & A_2 & \\
      & \ddots & & \\
      A_s & & &\\
    \end{bmatrix},\quad
    则A^{-1}=
    \begin{bmatrix}
      & & & A^{-1}_s \\
      & & \ddots & \\
      & A^{-1}_2 & & \\
      A^{-1}_1 & & &\\
    \end{bmatrix}
  \end{align*}
  $$

  其中 $A_i (i=1,2,\cdots,s)$ 可逆，则 $A$ 可逆

### 1.5 矩阵方程

含未知矩阵的方程称为矩阵方程。解方程应先化简方程为左侧形式，再利用各种性质求解

$$
\begin{align*}
  AX=B \quad&\Rightarrow\quad X=A^{-1}B \\
  XA=B \quad&\Rightarrow\quad X=BA^{-1} \\
  AXB=C \quad&\Rightarrow\quad X=A^{-1}CB^{-1}
\end{align*}
$$

### 1.6 等价矩阵

矩阵 $A_{m\times n}$ 经过有限次初等行列变换可以化为如下形式的矩阵

$$
\begin{bmatrix}
  E_{r(A)} & O \\
  O & O
\end{bmatrix}_{m\times n}
$$

其中，$r(A)$ 为 $A$ 的秩，该矩阵称为 $A$ 的等价标准形，且等价标准形是唯一的。设 $A$ 的一次变换为 $PAQ=B$，其中 $P,Q$ 可逆(任意可逆矩阵可以分解为若干初等矩阵的乘积)，则称 $A$ 与 $B$ 等价(等价关系满足自反、对称、传递)，记作 $A\cong B$ ，有 $r(A)=r(B)$，即

$$
矩阵A,B等价 \Leftrightarrow 矩阵A,B同型且秩相等
$$

### 1.7 矩阵的秩

* 定义

  若 $A_{m\times n}$ 存在 $k$ 阶子式不为 $0$，而任意 $k+1$ 阶子式为 $0$，则 $r(A)=k$。将 $A$ 使用有限次初等行变换为行阶梯形矩阵后，非零行的个数即为秩；或将 $A$ 使用有限次初等行列变换为等价标准形矩阵，通过 $E_{r(A)}$ 获得秩

* 性质
  * $0 \leq r(A_{m\times n}) \leq \min\{m, n\}$
  * $r(kA) = r(A) (k \neq 0)$
  * $r(AB) \leq \min\{r(A), r(B)\}$
  * $r(A + B) \leq r([A,B]) \leq r(A) + r(B)$
  * $\lvert r(A)-r(B)\rvert\leq r(A-B)\leq r(A)+r(B)$
  * $r(AB)\geq r(A)-r(B)-n$
  * $r(ABC)\geq r(AB)+r(BC)-r(B)$
  * 若 $A$ 为 $n(n \geq 2)$ 阶方阵，$r(A^*) =\begin{cases} n, & r(A) = n, \\ 1, & r(A) = n-1, \\ 0, & r(A) < n-1 \end{cases}$
  * 设 $A$ 是 $m \times n$ 矩阵，$P$, $Q$ 分别是 $m$ 阶、$n$ 阶可逆矩阵，则 $r(A) = r(PA) = r(AQ) = r(PAQ)$，即初等变换不改变秩，而可逆矩阵可以分解为若干初等变换矩阵
  * 若 $A_{m \times n}B_{n \times s} = O$，则 $r(A) + r(B) \leq n$
  * $r(A) = r(A^T) = r(A^TA) = r(AA^T)$
  * 若 $r(A_{m\times n})=n$，则 $r(AB)=r(B)$；若 $r(A_{m\times n})=m$，则 $r(BA)=r(B)$

## 2 进阶

### 2.1 矩阵运算 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

* 证明 $A$ 是零矩阵 $O$ $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式)}$
  * 秩：若 $r(A)=0$，则 $A=O$
  * 证 $A^{*}=O$：若 $r(A)<n-1$，则 $A^{*}=O$
  * ⚠️迹：若 $\mathrm{tr}{(A A^T)}=0$，则 $A=O$
  * ⚠️正交：若 $A$ 的行向量与 $B$ 的列向量均正交，则 $AB=O$

* 计算 $A^{n}$  $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式)}$
  * 秩 $1$ 方阵：$A^n=\big[\mathrm{tr}(A)\big]^{n-1}A$
  * 试算高阶找规律
  * 加法分解：$A^n\xlongequal{分解为}(B+C)^n$，利用二项式定理展开计算。一般 $B,C$ 中的一个高阶会很简单，这样大部分二项式都是 $0$，只用计算前几个二项式
  * 初等变换
    * 有现成的初等矩阵：可以直接按左行右列对 $A$ 做初等变换，$E^n$ 表示做 $n$ 次相应的初等变换
    * 没有现成的初等矩阵：做初等变换。如 $P^{-1}AP=B\Rightarrow AP=PB\Rightarrow[P\,\vdots\,PB]\xrightarrow{初等行变换}[E\,\vdots\,PBP^{-1}]$。初等列变换就竖着拼
  * 相似分解：$A^n=(P \Lambda P^{-1})^n=P \Lambda^n P^{-1}$，利用乘法结合律让中间的 $P^{-1}P$ 结合成 $E$

* $A^{T}A$、$A^{*}$、$A^{-1}$ 与初等矩阵 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{2} (脱胎换骨)}$
  * 扰动法

    若 $A$ 满足条件 $T$ 的前提是满足条件 $t$，但有时 $A$ 不满足 $t$，则令 $B=A+kE$ 满足 $t$，这样 $B$ 就满足 $T$。再回头令 $k\to 0$ 检验 $A$ 不满足 $t$ 时是否仍然满足 $T$

    > 例如未知矩阵 $A$ 满足某个等式，要分 $A$ 可逆与不可逆两种情况分别讨论

  * $A^{-1}$ 等价条件大观： [逆的大观](../../resource/image/advanced/inverse_matrix.png "逆的大观")
  * 初等矩阵
    * 左行右列初等变换、初等行(列)变换求逆矩阵、求高阶幂、化行阶梯形求极大线性无关组
    * ⚠️矩阵分解、矩阵满秩分解、等价标准形(详见 **强化36讲-线代-P30**)

* ⚠️分块矩阵 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式)}$

  运算、逆、矩阵分解(详见 **强化36讲-线代-P32~P35**)

  ***横拼左同多化零、竖拼右同多化零***

* ⚠️矩阵方程 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{2} (脱胎换骨)}$
  
  $$
  \begin{align*}
    AX=B \quad&\Rightarrow\quad X=A^{-1}B \\
    XA=B \quad&\Rightarrow\quad X=BA^{-1} \\
    AXB=C \quad&\Rightarrow\quad X=A^{-1}CB^{-1}
  \end{align*}
  $$

  * 如果 $A$ 可逆：利用初等变换两边同时变过去
  * 如果 $A$ 不可逆：视 $B=[\beta_1,\beta_2,\cdots,\beta_n]$，求方程组的解，最后再拼回来
  * 如果前两种都不行：把 $X$ 全部设出来 $x_{ij}$，直接带入方程比较对应位置的数值

* ⚠️矩阵的秩 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{2} (脱胎换骨) + \text{D}_\text{41} (试取特殊情况) + \text{P}_\text{12} (反向思路)}$

## 3 题目

* 基础30讲
  * ***例2.1(列向量分解、乘法结合律、方阵的幂)***
  * 例2.2(求高阶先试算2阶)
  * 例2.3(加法分解出E、二项展开式、高阶试算)
  * 例2.4(定义法求逆矩阵、提公因式剩E)
  * ***例2.5(分解法求矩阵逆、提公因式剩E、幺元E)***
  * 例2.6(伴随矩阵定义证明)
  * 例2.7(用伴随矩阵求二阶矩阵逆)
  * 例2.8(用伴随矩阵求三阶矩阵逆)
  * 例2.9(复合运算)
  * ***例2.10(分块矩阵求逆、待定系数法)***
  * 例2.11(复合运算)
  * ***例2.12(初等行变换求逆矩阵)***
  * 例2.13(初等矩阵性质)
  * 例2.14(两次初等变换)
  * 例2.15(分块矩阵求逆)
  * ***例2.16(三角分块矩阵求逆)***
  * ***例2.17(矩阵方程、逆的性质、求逆矩阵)***
  * ***例2.18(等价矩阵的等价标准形相同、初等变换)***
* 基础30讲课后题
  * 2.5(秩的性质、秩与行列式的关系)
  * ***2.7(列向量分解、乘法结合律)***
  * 2.8(高阶找规律)
  * ***2.9(矩阵方程留E手、乘法分配率)***
  * 2.10(E拆成逆)
  * 2.11(初始条件元素相等)
  * ***2.12(等价标准形求秩、非满秩情况下优先行列式确定未知数)***
* 1000题基础
  * 06(伴随与逆的关系、待定系数法)
  * 10(秩、可逆、初等列变换)
  * ***13(可逆矩阵可分解为若干初等变换矩阵、初等变换不改变秩)***
  * ***15(高阶多项式展开凑方程留E手)***
* 强化36讲
  * ⭐***例3.1(用 $\text{tr}$ 证明零矩阵)***
  * ***例3.2(秩 $1$ 矩阵的高次幂)***
  * 例3.3(试算高阶找规律)
  * ⭐***例3.4(旋转算子)***
  * 例3.5(矩阵加法分解)
  * ***例3.6(矩阵分解为初等变换矩阵)***
  * ⭐***例3.7(矩阵分解为相似矩阵)***
  * ⭐***例3.8(扰动法、伴随、等价、相似、合同)***
  * ***例3.9($(狗)(狗^*)=\begin{vmatrix}狗\end{vmatrix}E$)***
  * ***例3.10(用行列式联系 $A,A^{*}$)***
  * ***例3.11($x^T A x$ 行和列和、反对称矩阵)***
  * ***例3.12(抽象型矩阵求逆、多项式除法)***
  
    > 若 $AB=E$，则 $B$ 就是 $A^{-1}$

  * ***例3.13(抽象型矩阵求逆、待定系数法)***
  * ***例3.14利用特征值判断可逆、(看到 $f(A)$ 想 $f(\lambda)$)***
  
    > 特征值没有 $0\Rightarrow\det{(A)}\neq 0\Rightarrow A$ 可逆

  * 例3.15(初等矩阵的伴随矩阵)
  * ⛔***例3.16(用初等变换求高阶幂)***
  * ⭐***例3.17(矩阵分解、用初等变换求高阶幂)***
  
    > 高阶矩阵可以简写成列向量组形式 $A=[\alpha_1,\alpha_2,\cdots,\alpha_n]$ 以便于进行矩阵分解

  * ***例3.18(分块矩阵的秩)***
  * ⛔***例3.19(初等变换不改变秩、矩阵方程转非齐次线性方程组)***
  
    > * 经过初等变换的前后两个矩阵秩相同，有时候可能想找变换方式但找不到，这时就用秩
    > * 求矩阵方程 $AP=B$ 时，可以转化成求多个非齐次方程组来求，即视 $B=[\beta_1,\beta_2,\cdots,\beta_n]$，分别求 $Ax=0$ 的通解 $\xi$ 和 $Ax=\beta_i$ 的特解 $\eta_i$，那么 $B=[\xi+\eta_1,\xi+\eta_2,\cdots,\xi+\eta_n]$，最后再根据 $P$ 是否可逆等条件确定通解 $\xi$ 的任意常数 $k_i$ 们的约束关系

  * ⭐***例3.20(矩阵方程转非齐次线性方程组、思路试探)***
  * ***例4.1(竖拼右同多化零、左乘列满秩矩阵不改变秩)***
  * ***例4.2(行满秩矩阵的消除)***
  * ⭐***例4.3(试算、行(列)满秩矩阵的消除)***
  * ***例4.4(分块矩阵的"初等变换"、秩越乘越小)***
  * ***例4.5(秩的加减不等式)***
  * ***例4.6($r(AB)\geq r(A)-r(B)-n$)***
  * ***例4.7($r(ABC)\geq r(AB)+r(BC)-r(B)$、秩越乘越小)***
  * ⭐***例4.8(分块矩阵的"初等变换"、横拼竖拼、四秩相同)***
  * ***例4.9($A^{*}$ 的秩、$AB=O$ 时的秩不等式)***
* 1000题强化
