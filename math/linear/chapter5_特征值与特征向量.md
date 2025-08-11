# 特征值与特征向量

## 1 知识点

### 1.1 特征值与特征向量

* 定义

  设 $A$ 为 $n$ 阶矩阵，$\lambda$ 为任意常数，若存在 $n$ 维非零列向量 $\xi$，使得
  
  $$
  A\xi=\lambda\xi,\quad\xi\neq0
  $$
  
  则称 $\lambda$ 为 $A$ 的**特征值**，$\xi$ 为 $A$ 的**特征向量**

* 求解

  由特征值与特征向量的定义得
  
  $$
  \begin{align*}
    &\lambda\xi-A\xi=0 \\
    \Leftrightarrow&(\lambda E-A)\xi=0 \tag{*}\\
    \Leftrightarrow&\begin{vmatrix}\lambda E-A\end{vmatrix}=0 \\
  \end{align*}
  $$
  
  因为 $\xi\neq 0$，即齐次线性方程组 $(\lambda E-A)\xi=0$ 存在非零解，可得 $r(\lambda E-A)<n$，因此其行列式为 $0$，据此解出所有的 $n$ 个 $\lambda_i$。将 $\lambda_i$ 代回 $(*)$ 式解齐次线性方程组即可得 $\xi_i$。**注意，因为 $\xi\neq 0$，所以求出来的 $\xi_i$ 的基础解系中常数 $k\neq 0$**

  > ⭐***行列式化简获得 $\lambda$ 多项式***
  >
  > **1.最优选**：化简行列式，根据行列式直接得到 $(\lambda-\lambda_1)(\lambda-\lambda_2)\cdots(\lambda-\lambda_n)$ 的形式，获得特征值
  >
  > **2.应急法**：直接求出行列式有关 $\lambda$ 的多项式 $\lambda^k+a_{k-1}\lambda^{k-1}+\cdots+a_1\lambda+a_0$，随后
  > * 确定一个解项
  >   * 尝试 $\lambda=-1,0,1$ 是否满足，若满足则可得到其中一个特征值的解项 $(\lambda-\lambda_i)$
  >   * 若 $\lambda=-1,0,1$ 均不满足，则尝试 $a_0$ 的因子，找到其中一个满足的因子作为 $(\lambda-\lambda_i)$。如 $a_0=2$ 的因子为 $\pm1,\pm2$，此方法的原理为多项式等于 $0$ 的有理根必为整数，且是 $a_0$ 的因子
  > * 配出完整解多项式：在确定一个解项 $(\lambda-\lambda_i)$ 后，使用**多项式除法**获得剩余的解项，再配成 $(\lambda-\lambda_1)(\lambda-\lambda_2)\cdots(\lambda-\lambda_n)$ 的形式

* 性质
  * $n$ 阶矩阵有 $n$ 个特征值(含重根)
  * $\lambda_0$ 是 $A$ 的特征值 $\Leftrightarrow\begin{vmatrix}\lambda E-A\end{vmatrix}=0$ </br> $\lambda_0$ 不是 $A$ 的特征值 $\Leftrightarrow\begin{vmatrix}\lambda E-A\end{vmatrix}\neq 0\Leftrightarrow\lambda E-A$ 可逆
  * 对 $n$ 阶矩阵 $A$，其特征值多项式满足

    $$
    \begin{vmatrix}\lambda E-A\end{vmatrix}=\sum^n_{k=0}{(-1)^k S_k \lambda^{n-k}}
    $$

    其中 $S_k$ 为 $A$ 的 $k$ 阶主子式之和，约定 $S_0=1$。且有

    $$
    \begin{align*}
      S_k=&\displaystyle\sum_{1 \le i_1 < i_2 < \cdots < i_k \le n} \lambda_{i_1} \lambda_{i_2} \cdots \lambda_{i_k}\\
      S_n=&\begin{vmatrix}A\end{vmatrix}=\displaystyle\prod^n_{k=1}{\lambda_k}\\
      S_1=&\text{tr}(A)=\displaystyle\sum^n_{k=1}{\lambda_k}
    \end{align*}
    $$

  * $\xi_0\,(\xi_0\neq 0)$ 是 $A$ 的属于 $\lambda_0$ 的特征向量 $\Leftrightarrow\xi_0$ 是齐次线性方程组 $(\lambda_0 E-A)x=0$ 的非零解
  * $k$ 重特征值 $\lambda$ 最多只有 $k$ 个线性无关的特征向量
  * 若 $\xi_1,\xi_2$ 是 $A$ 的属于对应特征值 $\lambda_1,\lambda_2$ 的特征向量，则

    $$
    \begin{cases}
      \lambda_1\neq\lambda_2,&\xi_1,\xi_2线性无关 \\
    \lambda_1=\lambda_2,&\xi_1,\xi_2 可能线性无关,也可能线性相关
    \end{cases}
    $$

  * 若 $\xi_1,\xi_2$ 是 $A$ 的属于同一特征值 $\lambda$ 的特征向量，则**非零向量** $k_1\xi_1+k_2\xi_2$ 仍是 $A$ 的属于 $\lambda$ 的特征向量。**此处不能仅限制 $k_1\neq0,k_2\neq0$，因为 $\xi_1,\xi_2$ 可能是线性相关的，应限制 $k_1\xi_1+k_2\xi_2$ 整体为非零向量**
  * 若 $\xi_1,\xi_2$ 是 $A$ 的属于不同特征值 $\lambda_1,\lambda_2$ 的特征向量，则 $k_1\xi_1+k_2\xi_2\,(k_1\neq0,k_2\neq0)$ 不是 $A$ 的属于任何特征值的特征向量。**因为不同特征值对应的特征向量线性无关，因此此处仅限制 $k_1\neq0,k_2\neq0$ 即可**
  * 一个特征向量不能属于两个不同的特征值。即 $\xi_1$ 是 $\lambda_1$ 的特征向量，那么 $\xi_1$ 就不能是 $\lambda_2\,(\lambda_2\neq\lambda_1)$ 的特征向量

* 常用矩阵的特征值与特征向量

  设 $\xi$ 为矩阵 $A$ 属于特征值 $\lambda$ 的特征向量，则

  | **矩阵** | $kA$ | $A^k$ | $f(A)$ | $A^{-1}$ | $A^{*}$ | $P^{-1}AP$ |
  |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
  | **特征值** | $k\lambda$ | $\lambda^k$ | $f(\lambda)$ | $\lambda^{-1}$ | $\dfrac{\begin{vmatrix}A\end{vmatrix}}{\lambda}$ | $\lambda$ |
  | **特征向量** | $\xi$ | $\xi$ | $\xi$ | $\xi$ | $\xi$ | $P^{-1}\xi$ |

  * $f(x)$ 为多项式，若 $f(A)=O$，则 $f(\lambda)=0$
  * 三角矩阵主对角线上的元素就是特征值。求行列式易证
  * 秩 $1$ 矩阵 $A$ 的特征值为 $\begin{cases}\lambda_1=\lambda_2=\cdots=\lambda_{n-1}=0 \\ \lambda_n=\text{tr}(A)\end{cases}$

### 1.2 相似

#### 1.2.1 矩阵相似

* 定义

  设 $A,B$ 为 $n$ 阶方阵，若存在 $n$ 阶可逆矩阵 $P$，使得 $P^{-1}AP=B$，则称 $A$ 相似于 $B$，记作 $A\sim B$

* 性质

  若 $A\sim B$，则有
  * $r(A)=r(B)$
  * $\lambda_A=\lambda_B$，即 $\begin{vmatrix}\lambda E-A\end{vmatrix}=\begin{vmatrix}\lambda E-B\end{vmatrix}$，矩阵 $A,B$ 的特征值相同
  * $r(\lambda E-A)=r(\lambda E-B)$，且 $(\lambda E-A)\sim(\lambda E-B)$
  * $S_{A_k}=S_{B_k}$，即 $A,B$ 的各阶主子式之和相等

    **$A\sim B$ 是上述性质的必要不充分条件。相似一定满足性质；不满足性质则一定不相似，满足性质未必相似**

* 定理
  * 若 $A\sim B$，则

    $$
    \begin{cases}
      A^{k}\sim B^{k} \\
      f(A)\sim f(B) \\
      A^{-1}\sim B^{-1},&A可逆 \\
      f\left(A^{-1}\right)\sim f\left(B^{-1}\right),&A可逆 \\
      A^{*}\sim B^{*}
    \end{cases}
    $$

      且变换手段均相同，为 $P^{-1}AP=B$

  * 若 $A\sim B$，则 $A^T\sim B^T$，但变换手段为 $P^T A^T (P^T)^{-1}=B^T$
  * 若 $A\sim C\,,B\sim D$，则

    $$
    \begin{bmatrix}
      A & O \\
      O & B
    \end{bmatrix}\sim
    \begin{bmatrix}
      C & O \\
      O & D
    \end{bmatrix}
    $$

* 证明相似
  * 定义法：证明存在可逆矩阵 $P$，使得 $P^{-1}AP=B$
  * 传递性：若 $A\sim B,B\sim C$，则 $A\sim C$
  * 性质法：相似一定满足性质；不满足性质则一定不相似，满足性质未必相似
  * 对角化：若 $A\sim\Lambda\sim B$，则 $A\sim B$

#### 1.2.2 矩阵的相似对角化

* 定义
  
  设 $A$ 为 $n$ 阶矩阵，若存在 $n$ 阶可逆矩阵 $P$，使得 $P^{-1}AP=\Lambda$，则称 $A$ 可相似对角化，记作 $A\sim\Lambda$，并称 $\Lambda$ 为 $A$ 的**相似标准形**。有

  $$
  \begin{align*}
    P=\begin{bmatrix}
      \xi_1 & \xi_2 & \cdots & \xi_n
    \end{bmatrix},\quad&
    \Lambda=\begin{bmatrix}
      \lambda_1 & & & \\
      & \lambda_2 & & \\
      & & \ddots & \\
      & & & \lambda_n
    \end{bmatrix}\\

    P^{-1}AP=&\Lambda\\

    AP=&P\Lambda\\

    A\begin{bmatrix}
      \xi_1 & \xi_2 & \cdots & \xi_n
    \end{bmatrix}=&
    \begin{bmatrix}
      \xi_1 & \xi_2 & \cdots & \xi_n
    \end{bmatrix}
    \begin{bmatrix}
      \lambda_1 & & & \\
      & \lambda_2 & & \\
      & & \ddots & \\
      & & & \lambda_n
    \end{bmatrix}\\

    A\xi_i=&\lambda_i\xi_i\,,i=(1,2,\cdots,n)
  \end{align*}
  $$

  因此 $\xi_i$ 即为 $A$ 关于特征值 $\lambda_i$ 的特征向量。由于 $P$ 可逆，因此 $A$ 的特征向量线性无关，即
  * $A\sim\Lambda\Leftrightarrow A$ 有 $n$ 个线性无关的特征向量
  * $A\sim\Lambda\Leftrightarrow A$ 对应的每个 $k_i$ 重特征值都有 $k_i$ 个线性无关的特征向量，即 $k_i=n-r(\lambda_i E-A)$
  * $A$ 有 $n$ 个不同的特征值 $\Rightarrow A\sim\Lambda$
  * $A$ 是实对称矩阵 $\Rightarrow A\sim\Lambda$

* 求解

  **正解**：若求得 $A$ 的特征值 $\lambda_1,\lambda_2,\cdots,\lambda_n$，特征向量 $\xi_1,\xi_2,\cdots,\xi_n$，即可令

  $$
  P=\begin{bmatrix}
      \xi_1 & \xi_2 & \cdots & \xi_n
  \end{bmatrix}\qquad
  \Lambda=\begin{bmatrix}
    \lambda_1 & & & \\
    & \lambda_2 & & \\
    & & \ddots & \\
    & & & \lambda_n
  \end{bmatrix}
  $$

  **反解**：若存在可逆矩阵 $P$，使得 $P^{-1}AP=\Lambda$，则 $A=P\Lambda P^{-1}$，且有

  $$
  \begin{align*}
    P^{-1}A^{k}P=\Lambda^{k},\quad&A^{k}=P\Lambda^{k}P^{-1} \\
    P^{-1}f(A)P=f(\Lambda),\quad&f(A)=Pf(\Lambda)P^{-1}
  \end{align*}
  $$

#### 1.2.3 实对称矩阵的相似对角化

* 性质
  * 若 $A$ 是实对称矩阵，则其特征值是实数，特征向量是实向量
  * 若 $\xi_1,\xi_2$ 是 $A$ 的属于对应特征值 $\lambda_1,\lambda_2$ 的特征向量，则

    $$
    \begin{cases}
      \lambda_1\neq\lambda_2,&\xi_1\perp\xi_2 \\
    \lambda_1=\lambda_2,&\xi_1,\xi_2 可能线性无关,也可能正交
    \end{cases}
    $$

    因此若实对称矩阵 $A,B$ 的特征值相同，则一定有 $A\sim\Lambda\sim B$

  * 对任意 $n$ 阶实对称矩阵 $A$，存在 $n$ 阶正交矩阵 $Q$，使得

    $$
    Q^{-1}AQ=Q^T AQ=
    \begin{bmatrix}
      \lambda_1 & & & \\
      & \lambda_2 & & \\
      & & \ddots & \\
      & & & \lambda_n
    \end{bmatrix}
    $$

    其中，$\lambda_i\,(i=1,2,\cdots,n)$ 为 $A$ 的特征值，$Q=\begin{bmatrix}\eta_1,\eta_2,\cdots,\eta_n\end{bmatrix}$ 为 $A$ 的特征向量 $\begin{bmatrix}\xi_1,\xi_2,\cdots,\xi_n\end{bmatrix}$ 的标准正交化基

* 施密特正交化

  若 $\alpha_1,\alpha_2,\cdots,\alpha_n$ 线性无关但不正交，令
  
  $$
  \beta_i=\alpha_i-\sum^{i-1}_{k=1}{\dfrac{\langle\alpha_i,\beta_k\rangle}{\langle\beta_k,\beta_k\rangle}\beta_k}\quad(i=1,2,\cdots,n) \\

  \eta_i=\dfrac{\beta_i}{\begin{Vmatrix}\beta_i\end{Vmatrix}}\quad(i=1,2,\cdots,n)
  $$

  则 $\beta_1,\beta_2,\cdots,\beta_n$ 相互正交；$\eta_1,\eta_2,\cdots,\eta_n$ 是 $\alpha_1,\alpha_2,\cdots,\alpha_n$ 的规范(标准)正交基
  
* 求解
  * 求得 $A$ 的特征值 $\lambda_1,\lambda_2,\cdots,\lambda_n$，特征向量 $\xi_1,\xi_2,\cdots,\xi_n$
  * 将 $\xi_1,\xi_2,\cdots,\xi_n$ 标准正交化为 $\begin{bmatrix}\eta_1,\eta_2,\cdots,\eta_n\end{bmatrix}$
  * 令 $Q=\begin{bmatrix}\eta_1,\eta_2,\cdots,\eta_n\end{bmatrix}$，则 $Q$ 为正交矩阵，且 $Q^{-1}AQ=Q^T AQ=\Lambda$

## 2 进阶

* $\text{Jordan}$ 标准型

  当矩阵 $A$ 不可相似对角化时，使用 $\text{Jordan}$ 标准型完成对应操作

  * 构造 $\text{Jordan}$ 标准型 $J$

    > 💡***构造口诀：***
    >
    > $k$ 重根 $\lambda$ ，向量 $s=n-r(\lambda E-A)$，块数就是 $s$ 个；
    >
    > 要画几个 1？$k - s$ 个不能错。  
    >
    > 从头开始连着画，大块优先最稳妥；  
    >
    > 1 在上方斜线走，块间不能跨着填。

    以下为部分示例

    $$
    \begin{align*}
      J_1 = \begin{bmatrix}
      \lambda & 0 & 0 & 0 \\
      0 & \lambda & 0 & 0 \\
      0 & 0 & \lambda & 0 \\
      0 & 0 & 0 & \lambda
      \end{bmatrix}\quad

      J_2 = \begin{bmatrix}
      \lambda & 1 & 0 & 0 \\
      0 & \lambda & 0 & 0 \\
      0 & 0 & \lambda & 0 \\
      0 & 0 & 0 & \lambda
      \end{bmatrix}\quad

      J_3 = \begin{bmatrix}
      \lambda_1 & 1 & 0 & 0 \\
      0 & \lambda_1 & 0 & 0 \\
      0 & 0 & \lambda_2 & 0 \\
      0 & 0 & 0 & \lambda_3
      \end{bmatrix}
    \end{align*}
    $$

    **$J_1$: $4$ 阶矩阵 $A$，特征值全为 $\lambda$，几何重数 $s=4$**

    > 既然所有的特征值都是 $\lambda$ 并且几何重数是 $4$，这意味着矩阵是可以对角化的。所以 $\text{Jordan}$ 标准形将是一个对角矩阵。

    **$J_2$: $4$ 阶矩阵 $A$，特征值全为 $\lambda$，几何重数 $s=3$**

    > 这里有一个特征值 $\lambda$ 出现了四次，但是几何重数只有 $3$，意味着有一个 $\text{Jordan}$ 块大小大于 $1$。因为 $k - s = 4 - 3 = 1$，我们只需要一个 $1$ 在超对角线上。请注意，这里的 $\text{Jordan}$ 块构造可能不是唯一的，取决于基础向量的选择。此处展示的是最常见的一种情况。

    **$J_3$ : $4$ 阶矩阵 $A$，特征值为 $\lambda_1,\lambda_1,\lambda_2,\lambda_3$，其中 $\lambda_1$ 对应的几何重数 $s=1$**

    > 由于 $\lambda_1$ 的几何重数为 $1$，对于 $\lambda_1$ 来说，我们将有一个大小为 $2\times2$ 的 $\text{Jordan}$ 块，而对于 $\lambda_2$ 和 $\lambda_3$ 则各自对应一个 $1\times1$ 的块。

  * 性质
    * 对任意方阵 $A$ 恒有 $A\sim J$；若 $A$ 可以相似对角化，则 $J=\Lambda$
    * 传递性：若 $A\sim J\sim B$，则 $A\sim B$

  * 求可逆矩阵 $P$ 使得 $P^{-1}AP=J$
    * 根据重根个数确定 $A$ 的 $\text{Jordan}$ 标准型 $J$
    * 设可逆矩阵 $P^{-1}AP=J$，得到 $AP=PJ$
    * 设 $P=\begin{bmatrix}\xi_1,\xi_2,\cdots,\xi_n\end{bmatrix}$，带入 $AP=PJ$，解齐次方程和非齐次方程获得全部的 $\xi_i$，并拼成 $P$。此处齐次方程照常求解，非齐次方程可以只求特解，因为为了处理方便最后会使齐次通解系数 $k=0$，齐次通解就没必要求了
    * 可进一步变换得到具体的 $A=PJP^{-1}$，可以求 $A^n$ 等关于 $A$ 的问题

## 3 题目

* 基础30讲
  * ⭐***例5.1(求特征值特征向量)***
  * ⭐***例5.2(秩1矩阵)***
  * 例5.3(幂等矩阵)
  * 例5.4(二阶主子式之和)
  * ***例5.5(列1向量、 $A^{*}$ 的特征值特征向量、特征值定义)***
  * 例5.6(相似证明性质法)
  * 例5.7(相似则主子式之和相等)
  * ***例5.8(相似变换手段、秩1矩阵)***
  * ***例5.9(相似对角化判断)***
  * ***例5.10(性质得特征值、不可逆时的行列式性质)***
  * 例5.11, 13(特征值与特征向量性质)
  * 例5.12(求 $P^{-1}AP$ )
  * ***例5.14( $AP=PB$ 形式综合)***
  * 例5.15(反解A)
  * 例5.16( $f(A)=Pf(\Lambda)P^{-1}$ )
  * ***例5.17(反解A、高次幂 $A^{k}=P\Lambda^{k}P^{-1}$ )***
  * ⭐***例5.18(求标准正交基)***
  * 例5.19(传递性证明相似对角化)
* 基础30讲课后题
  * 5.2(变换后的特征向量)
  * ***5.3(利用相似对角化证相似)***
  * ***5.5(特征值定义、基础运算、$(A-E)\xi=A\xi-E\xi=(\lambda-1)\xi$ )***
  * 5.9(从定义出发，因为方程组解不唯一)
  * 5.12(相似必要性质)
  * 5.14(实对称矩阵不同特征值的特征向量正交，内积为0)
  * ***5.15(分块矩阵、试算高次幂、Jordan标准型)***
* 1000题
