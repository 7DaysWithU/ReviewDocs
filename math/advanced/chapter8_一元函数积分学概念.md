# 一元函数积分学概念

## 1 知识点

### 1.1 不定积分

* 原函数、不定积分
  * 定义：设函数 $f(x)$在区间$I$ 上，若存在可导函数 $F(x)$，对于区间上任意一点都有 $F^{'}(x)=f(x)$ 成立，则称 $F(x)$ 是 $f(x)$ 的一个原函数，称 $\int{f(x)\mathrm{d}x}=F(x)+C$ 为 $f(x)$ 在区间 $I$ 上的不定积分
  * 先确定区间再谈论其他
* 原函数(不定积分)存在定理

    $$
    f(x)在区间I内
    \begin{cases}
        连续，有\\\\

        有第一类间断点
        \begin{cases}
            可去间断点&，没有\\
            跳跃间断点&，没有
        \end{cases}\\\\

        有第二类间断点
        \begin{cases}
            无穷间断点&，没有\\
            振荡间断点&，可能有
        \end{cases}
    \end{cases}
    $$

  * 连续函数必有原函数：若函数 $f(x)$在$[a,b]$ 上连续，则函数 $F(x)=\int^x_a{f(t)\mathrm{d}t}$ 在 $[a,b]$ 上可导，且 $F^{'}(x)=f(x)$
    * 使用积分中值定理、夹逼准则证明
    * 总结：$f(x)$ 连续 $\Rightarrow\begin{cases}
      \int{f(x)\mathrm{d}x}=\int^x_a{f(t)\mathrm{d}t}+C\\
      \Big(\int^x_a{f(t)\mathrm{d}t}\Big)^{'}=f(x)\Leftrightarrow F^{'}(x)=f(x)
    \end{cases}$
  * 含有第一类间断点和无穷间断点的 $f(x)$ 在区间内必定没有原函数
    * 若 $f(x)$ 可导，且 $\lim\limits_{x\to x_0}{f^{'}(x)}=0$，则 $f^{'}(x)$ 在 $x_0$ 处连续
      * 可导必连续、洛必达、导数定义来证明
    * 若 $f(x)$ 可导，则 $f^{'}(x)$ 有介值性
      * 辅助函数、零点定理或介值定理、费马定理证明
    * 若 $f^{'}(x)$ 存在且 $\neq0$，则 $f^{'}(x)$ 必恒正或恒负
      * 介值性证明
    * 若 $f^{'}(x)$在$[a,b]$ 上存在，则 $f^{'}(x)$ 一定没有第一类间断点

### 1.2 定积分

* 定义：若函数 $f(x)$ 在区间 $[a,b]$ 上有界，在 $(a,b)$ 上任取 $n-1$ 个分点 $x_i(i=1,2,\cdots,n-1)$，定义 $x_0=a,x_n=b$，且 $a=x_0<x_1<x_2<\cdots<x_n=b$，记 $\Delta x_k=x_k-x_{k-1},k=1,2,\cdots,n$，并任取一点 $\xi_k\in[x_{k-1}, x_k]$，记 $\lambda=\max\limits_{1\leq k\leq n}{\Delta x_k}$。则当 $\lambda\to0$，且 $\lim\limits_{\lambda\to0}{\sum^n_{k=1}{f(\xi_k)\Delta x_k}}$ 存在且与分点 $x_i$ 及点 $\xi_k$ 的取法无关时，称为函数 $f(x)$ 在区间 $[a,b]$ 上可积，记作

  $$
  \int^b_a{f(x)\mathrm{d}x}=\lim\limits_{\lambda\to0}{\sum^n_{k=1}{f(\xi_k)\Delta x_k}}
  $$

  当将区间 $[a,b]$ $N$ 等分时，每个小区间为 $I_k=\Bigg[a+\dfrac{b-a}{N}(k-1),a+\dfrac{b-a}{N}k\Bigg]$，当 $\xi_k\in I_k$ 时，可进一步写为

  $$
  \int^b_a{f(x)\mathrm{d}x}=\lim\limits_{N\to\infty}{\sum^N_{i=1}{f\big(\xi_k\big)\dfrac{b-a}{N}}}
  $$

  * 几何意义：定积分 $\int^b_a{f(x)\mathrm{d}x}$ 表示由曲线 $f(x)$ 、直线 $x=a,x=b$ 与 $x$ 轴围出的曲边梯形的面积。特别的，若 $f(x)\leq0$，则定积分表示曲边梯形面积的 ***负值***
* 定积分存在定理
  * 充分条件：区间有限、函数有界
    * 若函数 $f(x)$ 在区间 $[a,b]$ 上连续，则 $\int^b_a{f(x)\mathrm{d}x}$ 存在
      * 闭区间连续函数必有界
    * 若函数 $f(x)$ 在区间 $[a,b]$ 上单调，则 $\int^b_a{f(x)\mathrm{d}x}$ 存在
    * 若函数 $f(x)$ 在区间 $[a,b]$ 上有界，且仅有有限个间断点 ***(不包含无穷间断点)***，则 $\int^b_a{f(x)\mathrm{d}x}$ 存在
      * 无穷间断点会导致函数无界
  * 必要条件
    * 若 $\int^b_a{f(x)\mathrm{d}x}$ 存在，则函数 $f(x)$ 在区间 $[a,b]$ 上连续
* 定积分性质
  * 两个规定
    * 当 $b=a$ 时，$\int^a_a{f(x)\mathrm{d}x}=0$
    * 当 $a>b$ 时，$\int^b_a{f(x)\mathrm{d}x}=-\int^a_b{f(x)\mathrm{d}x}$
  * 区间长度定理
    * 设 $a<b$，则 $\int^b_a{\mathrm{d}x}=b-a=L$，其中 $L$ 为区间 $[a,b]$ 的长度
  * 积分线性性质
    * 设 $k_1,k_2$ 为常数，则 $\int^b_a{\Big(k_1 f(x)\pm k_2 g(x)\Big)\mathrm{d}x}=k_1\int^b_a{f(x)\mathrm{d}x}\pm k_2\int^b_a{g(x)\mathrm{d}x}$
  * 积分可拆性
    * ***无论 $a,b,c$ 的大小如何***，恒有 $\int^b_a{f(x)\mathrm{d}x}=\int^c_a{f(x)\mathrm{d}x}+\int^b_c{f(x)\mathrm{d}x}$
  * 积分保号性
    * 若在区间 $[a,b]$ 上有 $f(x)\leq g(x)$，则有 $\int^b_a{f(x)\mathrm{d}x}\leq\int^b_a{g(x)\mathrm{d}x}$。注意，若函数 $f(x)-g(x)$ 连续且不恒为 $0$，则等号无法取到
    * 特殊的，有 $\lvert\int^b_a{f(x)\mathrm{d}x}\rvert\leq\int^b_a{\lvert f(x)\rvert\mathrm{d}x}$
  * 估值定理
    * 设 $m,M$ 分别为 $f(x)$ 在区间 $[a,b]$ 上的最小值和最大值，$L$ 为区间 $[a,b]$ 的长度，则有 $m L\leq\int^b_a{f(x)\mathrm{d}x}\leq M L$
  * ***中值定理***
    * 设 $f(x)$ 在区间 $[a,b]$ 上连续，则 $\exist\xi\in[a,b]$，满足 $\int^b_a{f(x)\mathrm{d}x}=f(\xi)(b-a)$
    * 将 $\begin{cases}
      F(x)=\int^x_a{f(t)\mathrm{d}t}\\
      F^{'}(x)=f(x)
    \end{cases}$ 带入拉格朗日中值定理 $F(b)-F(a)=F^{'}(\xi)(b-a)$ 即可证明

### 1.3 变限积分

* 定义：当 $x$ 在区间 $[a,b]$ 上变动时，对于每一个 $x$ 值，$\int^x_a{f(t)\mathrm{d}t}$ 都有一个确定的值，因此该积分是一个关于 $x$ 的函数，记作

  $$
  F(x)=\int^x_a{f(t)\mathrm{d}t}
  $$

  称 $F(x)$ 为变上限积分。同理可定义变下限积分、全变限积分。统称为变限积分

* 变限积分性质
  * 若 $f(x)$ 在区间 $I$ 上可积，则 $F(x)=\int^x_a{f(t)\mathrm{d}t}$ 在区间 $I$ 上连续
  * 若 $f(x)$ 在区间 $I$ 上连续，则函数 $F(x)=\int^x_a{f(t)\mathrm{d}t}$ 在 $I$ 上可导，且 $F^{'}(x)=f(x)$
  * 若 $x=x_0\in I$ 是 $f(x)$ 唯一的跳跃间断点，则 $F(x)=\int^x_a{f(t)\mathrm{d}t}$ 在 $x_0$ 处不可导，且

    $$
    \begin{cases}
      F^{'}_-(x_0)=\lim\limits_{x\to x^-_0}{f(x)}\\
      F^{'}_+(x_0)=\lim\limits_{x\to x^+_0}{f(x)}
    \end{cases}
    $$
  
  * 若 $x=x_0\in I$ 是 $f(x)$ 唯一的可去间断点，则 $F(x)=\int^x_a{f(t)\mathrm{d}t}$ 在 $x_0$ 处可导，且 $F^{'}(x_0)=\lim\limits_{x\to x_0}{f(x)}\neq f(x_0)$

### 1.4 反常积分

* 定义、敛散性
  * 无穷区间上的反常积分

    设 $F(x)$ 是 $f(x)$ 在相应区间上的一个原函数
    * $\int^{+\infty}_a{f(x)\mathrm{d}x}=\Big[\lim\limits_{x\to+\infty}{F(x)}\Big]-F(a)$，若极限存在，则称反常积分收敛，否则称发散
    * $\int^b_{-\infty}{f(x)\mathrm{d}x}=F(b)-\Big[\lim\limits_{x\to-\infty}{F(x)}\Big]$，若极限存在，则称反常积分收敛，否则称发散
    * $\int^{+\infty}_{-\infty}{f(x)\mathrm{d}x}=\int^{x_0}_{-\infty}{f(x)\mathrm{d}x}+\int^{+\infty}_{x_0}{f(x)\mathrm{d}x}$，若右端两个积分都收敛，则称反常积分收敛，否则称发散
  * 无界函数的反常积分

    设 $F(x)$ 是 $f(x)$ 在相应区间上的一个原函数，$x_0$ 为 $f(x)$ 的瑕点(使 $f(x)$ 在 $U(x_0,\delta)$ 内无界的点称为瑕点)
    * 若 $x=a$ 是唯一瑕点，则 $\int^b_a{f(x)\mathrm{d}x}=F(b)-\Big[\lim\limits_{x\to a^+}{F(x)}\Big]$,若极限存在，则称反常积分收敛，否则称发散
    * 若 $x=b$ 是唯一瑕点，则 $\int^b_a{f(x)\mathrm{d}x}=\Big[\lim\limits_{x\to b^-}{F(x)}\Big]-F(a)$,若极限存在，则称反常积分收敛，否则称发散
    * 若 $x=c\in(a,b)$ 是唯一瑕点，则 $\int^a_b{f(x)\mathrm{d}x}=\int^c_a{f(x)\mathrm{d}x}+\int^b_c{f(x)\mathrm{d}x}$，若右端两个积分都收敛，则称反常积分收敛，否则称发散
  * 将 $\infty$ 和瑕点统称为奇点。***判别敛散性时，一个积分只能有一个奇点***
* 敛散性判别法
  * 无穷区间
    * 比较判别法

      设函数 $f(x),g(x)$ 在区间 $[a,+\infty)$ 上连续，且 $0\leq f(x)\leq g(x)(a\leq x<+\infty)$，则
      * 当 $\int^{+\infty}_a{g(x)\mathrm{d}x}$ 收敛时，$\int^{+\infty}_a{f(x)\mathrm{d}x}$ 也收敛
      * 当 $\int^{+\infty}_a{f(x)\mathrm{d}x}$ 发散时，$\int^{+\infty}_a{g(x)\mathrm{d}x}$ 也发散
    * 比较判别法的极限形式

      设函数 $f(x),g(x)$ 在区间 $[a,+\infty)$ 上连续，且 $f(x)\geq0,g(x)>0,\lim\limits_{x\to+\infty}{\dfrac{f(x)}{g(x)}}=\lambda$，则
      * $\lambda\neq0$ 且 $\lambda\neq\infty$ 时，$f(x),g(x)$ 是同阶无穷小，$\int^{+\infty}_a{f(x)\mathrm{d}x}$ 与 $\int^{+\infty}_a{g(x)\mathrm{d}x}$ 具有相同的敛散性
      * $\lambda=0$ 时，$f(x)$ 趋 $0$ 速度比 $g(x)$ 快，若 $\int^{+\infty}_a{g(x)\mathrm{d}x}$ 收敛，则 $\int^{+\infty}_a{f(x)\mathrm{d}x}$ 也收敛
      * $\lambda=\infty$ 时，$g(x)$ 趋 $0$ 速度比 $f(x)$ 快，若 $\int^{+\infty}_a{g(x)\mathrm{d}x}$ 发散，则 $\int^{+\infty}_a{f(x)\mathrm{d}x}$ 也发散
  * 无界函数
    * 比较判别法

      设函数 $f(x),g(x)$ 在区间 $(a,b]$ 上连续，瑕点同为 $a$，且 $0\leq f(x)\leq g(x)(a<x\leq b)$，则
      * 当 $\int^b_a{g(x)\mathrm{d}x}$ 收敛时，$\int^b_a{f(x)\mathrm{d}x}$ 也收敛
      * 当 $\int^b_a{f(x)\mathrm{d}x}$ 发散时，$\int^b_a{g(x)\mathrm{d}x}$ 也发散
    * 比较判别法的极限形式

      设函数 $f(x),g(x)$ 在区间 $(a,b]$ 上连续，且 $f(x)\geq0,g(x)>0(a<x\leq b),\lim\limits_{x\to a^+}{\dfrac{f(x)}{g(x)}}=\lambda$，则
      * $\lambda\neq0$ 且 $\lambda\neq\infty$ 时，$f(x),g(x)$ 是同阶无穷小，$\int^b_a{f(x)\mathrm{d}x}$ 与 $\int^b_a{g(x)\mathrm{d}x}$ 具有相同的敛散性
      * $\lambda=0$ 时，$g(x)$ 趋 $\infty$ 速度比 $f(x)$ 快，若 $\int^b_a{g(x)\mathrm{d}x}$ 收敛，则 $\int^b_a{f(x)\mathrm{d}x}$ 也收敛
      * $\lambda=\infty$ 时，$f(x)$ 趋 $\infty$ 速度比 $g(x)$ 快，若 $\int^b_a{g(x)\mathrm{d}x}$ 发散，则 $\int^b_a{f(x)\mathrm{d}x}$ 也发散
  * 重要结论

    $$
    \int^1_0{\dfrac{1}{x^p}}，\int^1_0{\dfrac{\ln{x}}{x^p}}
    \begin{cases}
      收敛，0<p<1\\\\
      发散，1\leq p
    \end{cases}
    $$

    </br>

    $$
    \int^{+\infty}_1{\dfrac{1}{x^p}}，\int^{+\infty}_1{\dfrac{\ln{x}}{x^p}}
    \begin{cases}
      发散，p\leq1\\\\
      收敛，1<p
    \end{cases}
    $$

    * ***凡是与 $x$ 趋 $0$ 速度相同(即与 $x$ 是同阶无穷小)的式子都可以带入上述公式中的 $x$***

## 2 题目

* 基础30讲
  * 例8.2(不连续一定不可导)
  * 例8.3(原函数存在定理、定积分存在定理)
  * 例8.4(定积分几何意义)
  * 例8.5(定积分几何意义)
  * 例8.6(凑定积分定义)
  * 例8.7(定积分保号性证明)
  * 例8.8(定积分中值定理证明)
  * 例8.9-10(定积分保号性)
  * 例8.11-13(变限积分性质)
  * 例8.14(有界性证明、估值定理、积分保号性)
  * 例8.15(反常积分重要结论、比阶)
  * 例8.16(反常积分重要结论、比阶)
  * ***例8.17-19(敛散性判别)***
* 基础30讲课后题
  * 8.1(积分比大小)
  * 8.2(可积、可导、原函数存在综合判断)
  * 8.4(定积分定义)
  * 8.5(定积分定义、夹逼准则)
  * 8.6(取整函数、变限积分)
  * 8.7(积分换元法)
* 1000题
  * 01(定积分定义)
  * 02(积分区间形式)
  * 04(奇偶性质)
  * 05(定积分性质)
  * 08(几何意义)
  * ***09(变限积分求导、反函数求导)***
  * 10(奇偶性质)
  * ***14(收敛判断模板)***
  * 15(收敛判断)
  * ***18(不可解函数求积分)***
  * 20(奇偶性质)
  * 21(求不定积分)
  * 24(反常积分)
