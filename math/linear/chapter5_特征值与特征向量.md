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

### 1.2 相似

* 矩阵相似
  * 定义

    设 $A,B$ 为 $n$ 阶方阵，若存在 $n$ 阶可逆矩阵 $P$，使得 $P^{-1}AP=B$，则称 $A$ 相似于 $B$，记作 $A\sim B$

  * 性质

    若 $A\sim B$，则有
    * $r(A)=r(B)$
    * $\lambda_A=\lambda_B$，即 $\begin{vmatrix}\lambda E-A\end{vmatrix}=\begin{vmatrix}\lambda E-B\end{vmatrix}$，矩阵 $A,B$ 的特征值相同
    * $r(\lambda E-A)=r(\lambda E-B)$，且 $(\lambda E-A)\sim(\lambda E-B)$
    * $S_{A_k}=S_{B_K}$，即 $A,B$ 的各阶主子式之和相等

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

* 矩阵的相似对角化

* 实对称矩阵的相似对角化

## 2 题目

* 基础30讲
  * ⭐***例5.1(求特征值特征向量)***
  * ⭐***例5.2(秩1矩阵)***
  * 例5.3(幂等矩阵)
  * 例5.4(二阶主子式之和)
  * ***例5.5(列1向量、 $A^{*}$ 的特征值特征向量、特征值定义)***
  * 例5.6(相似证明性质法)
  * 例5.7(相似则主子式之和相等)
  * ***例5.8(相似变换手段、秩1矩阵)***
* 基础30讲课后题
* 1000题
