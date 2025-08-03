# 0基础

## 1 知识点

* 线性运算
  * 加法：$a+b$
  * 数乘：$k\cdot a$

* 点积运算

    $(\alpha,\beta)$ 称为向量 $\alpha$ 与向量 $\beta$ 的点积运算,即将 $\alpha$,$\beta$ 的所有分量对应相乘再相加

  * 一行乘一列

    $$
    [a_1,a_2]\begin{bmatrix}b_1 \\ b_2\end{bmatrix}=a_1b_1+a_2b_2
    $$

  * 一行乘多列

    $$
    [a_1,a_2]\begin{bmatrix}b_1&c_1\\b_2&c_2\end{bmatrix}=\begin{bmatrix}a_1b_1+a_2b_2,a_1c_1+a_2c_2\end{bmatrix}
    $$

  * 多行乘一列

    $$
    \begin{bmatrix}a_1&a_2\\b_1&b_2\end{bmatrix}\begin{bmatrix}c_1\\c_2\end{bmatrix}=\begin{bmatrix}a_1c_1+a_2c_2\\b_1c_1+b_2c_2\end{bmatrix}
    $$

  * 多行乘多列

    $$
    \begin{bmatrix}
      a_1 & a_2 \\
      b_1 & b_2
    \end{bmatrix}
    \begin{bmatrix}
      c_1 & d_1 \\
      c_2 & d_2
    \end{bmatrix}
    =\begin{bmatrix}
      a_1c_1+a_2c_2 & a_1d_1+a_2d_2 \\
      b_1c_1+b_2c_2 & b_1d_1+b_2d_2
    \end{bmatrix}
    $$

* 线性变换

  | 类型 | 矩阵形式 | 几何作用 | 是否正交矩阵 | 是否保距离 | 是否保面积 | 是否可逆 | 特征值 |
  |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
  | $x$ 轴对称 | $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ | 将点关于 $x$ 轴镜像翻转 | ✅ 是 | ✅ 是 | ✅ 是 | ✅ 是 | $1, -1$ |
  | $y$ 轴对称 | $\begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$ | 将点关于 $y$ 轴镜像翻转 | ✅ 是 | ✅ 是 | ✅ 是 | ✅ 是 | $-1, 1$ |
  | 原点对称 | $\begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$ | 将点关于原点镜像翻转 | ✅ 是 | ✅ 是 | ✅ 是 | ✅ 是 | $-1, -1$ |
  | 缩放 | $\begin{bmatrix} a & 0 \\ 0 & b \end{bmatrix}$ | $x$ 方向放大 $a$ 倍，$y$ 方向放大 $b$ 倍 | ❌ 否 </br> (单位矩阵除外) | ❌ 否 </br> (单位矩阵除外) | ❌ 否 </br> (单位矩阵除外) | ✅ 是 | $a, b$ |
  | $x$ 方向剪切 | $\begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}$ | $x$ 坐标随 $y$ 值线性偏移 | ❌ 否 | ❌ 否 | ✅ 是 | ✅ 是 | $1, 1$ |
  | $y$ 方向剪切 | $\begin{bmatrix} 1 & 0 \\ k & 1 \end{bmatrix}$ | $y$ 坐标随 $x$ 值线性偏移 | ❌ 否 | ❌ 否 | ✅ 是 | ✅ 是 | $1, 1$ |
  | 旋转 $\theta$ 角 | $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ | 绕原点逆时针旋转 $\theta$ 角 | ✅ 是 | ✅ 是 | ✅ 是 | ✅ 是 | $\cos\theta \pm i\sin\theta$ |

  * 正交矩阵：满足 $A^T A = I$，表示变换保持向量长度和角度不变，如旋转和对称
  * 保距离变换：变换前后任意两点之间的距离不变
  * 保面积变换：变换前后图形的面积不变，即使形状变化
  * 可逆性：所有这些变换都是可逆的，除非缩放因子为 $0$ (不在此表范围内)
  * 特征值：可以帮助判断变换是否包含旋转(复数特征值)、缩放(实数特征值)等

## 2 题目

* 基础30讲
* 基础30讲课后题
* 1000题
