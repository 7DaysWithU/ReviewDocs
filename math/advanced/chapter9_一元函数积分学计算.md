# 一元函数积分学计算

## 1 知识点

### 1.1 不定积分计算

* 凑微分法

    $$
    \int{f\big[g(x)\big]g^{'}(x)\mathrm{d}x}=\int{f\big[g(x)\big]\mathrm{d}\big[g(x)\big]}\xlongequal{令u=g(x)}\int{f(u)\mathrm{d}u}
    $$

  * 最后得到的是关于 $u$ 的全体原函数，一定要把 $x$ 代回去
  * 可以先对最复杂的部分求导试探一下能不能凑
* 换元法

    $$
    \int{f(x)\mathrm{d}x}\xlongequal{令x=g(u)}\int{f\big[g(u)\big]\mathrm{d}\big[g(u)\big]}=\int{f\big[g(u)\big]g^{'}(u)\mathrm{d}u}
    $$

  * 常用换元法
    * 三角函数代换

        $$
        \begin{cases}
            \sqrt{a^2-x^2}&\Rightarrow&令x=a\sin{t},&\lvert t\rvert<\dfrac{\pi}{2}\\\\
            \sqrt{a^2+x^2}&\Rightarrow&令x=a\tan{t},&\lvert t\rvert<\dfrac{\pi}{2}\\\\
            \sqrt{x^2-a^2}&\Rightarrow&令x=a\sec{t},&
            \begin{cases}
                若x<0,则\dfrac{\pi}{2}<t<\pi\\
                若x>0,则0<t<\dfrac{\pi}{2}
            \end{cases}
        \end{cases}
        $$

    * 恒等变形后三角代换
    * 根式代换：当被积函数含有根式时，可以尝试凑平方开出来绝对值，大部分难办的情况直接令 $\sqrt{\text{*}}=t$
    * 倒代换：被积函数分母幂次比分子高 $2$ 次及以上的时候作倒代换，令 $x=\dfrac{1}{t}$
    * 复杂函数的直接代换：当被积函数中含有超越式时，可以考虑直接把这个复杂函数令成 $t$
* 分部积分法

    $$
    \int{u(x)v^{'}(x)\mathrm{d}x}=u(x)v(x)-\int{v(x)u^{'}(x)\mathrm{d}x}
    $$

  * ***$u\leftarrow$ 反、对、幂、三、指 $\rightarrow v$。三指和指三可互换***
  * 高阶推广
      ![高阶分部积分法](../../resource/image/advanced/chapter9_%E4%B8%80%E5%85%83%E5%87%BD%E6%95%B0%E7%A7%AF%E5%88%86%E5%AD%A6%E8%AE%A1%E7%AE%97_%E9%AB%98%E9%98%B6%E5%88%86%E9%83%A8%E7%A7%AF%E5%88%86%E6%B3%95.jpeg "高阶分部积分法")
* 有理函数积分
  * 定义：形如 $\int{\dfrac{P_n(x)}{Q_m(x)}},(n<m)$ 的积分成为有理函数的积分，若 $n\geq m$ 则需要化简成最简有理函数。其中，$P_n(x)$ 为有关 $x$ 的 $n$ 次多项式，$Q_m(x)$ 为有关 $x$ 的 $m$ 次多项式
  * 化简

    若 $Q_m(x)$ 在实数域内可因式分解，则可把 $\int{\dfrac{P_n(x)}{Q_m(x)}}$ 拆成若干项最简有理分式之和方便积分

    在化简完与原始进行 $A,B$ 参数的确定时，既可全部化简出来一一对应，也可以 $x$ 取特殊值，消除某几个参数来快速求解

    * $Q_m(x)$ 的一次单因式 $a x+b$ 产生一项 $\dfrac{A}{a x+b}$
    * $Q_m(x)$ 的 $k$ 重一次因式 $(a x+b)^k$ 产生 $k$ 项，分别为 $\dfrac{A_1}{a x+b},\dfrac{A_2}{a x+b},\cdots,\dfrac{A_k}{a x+b}$
    * $Q_m(x)$ 的二次单因式 $a x^2+b x+c$ 产生一项 $\dfrac{A x+B}{a x^2+b x+c}$
    * $Q_m(x)$ 的 $k$ 重二次因式 $(a x^2+b x+c)^k$ 产生 $k$ 项，分别为

        $$
        \dfrac{A_1 x+B_1}{a x^2+b x+c},\dfrac{A_2 x+B_2}{a x^2+b x+c},\cdots,\dfrac{A_k x+B_k}{a x^2+b x+c}
        $$

* 总结

    $$
    不定积分计算思路
    \begin{cases}
      1.&恒等变换&\\
      2.1&凑微分法&\\
      2.2&换元法&
      \begin{cases}
        根式能凑出来平方就用三角函数代换\\
        凑不出来直接令\sqrt{*}=t
      \end{cases}\\\\
      3.&分部积分法&
      \begin{cases}
        一般情况\\
        方程情况
        \begin{cases}
          I=口-I\\
        I=口-I_1+I_1\\
        I_n=F(I_{n-1},I_{n-1})递推
        \end{cases}
      \end{cases}
    \end{cases}
    $$

### 1.2 定积分计算

* 计算

    设函数 $F(x)$ 是连续函数 $f(x)$ 在 $[a,b]$ 上的一个原函数，则

    $$
    \int^b_a{f(x)\mathrm{d}x}=F(x)\Big|^b_a=F(b)-F(a)
    $$

    若 $f(x)$ 在 $[a,b]$ 上分段有原函数，在 $[a,c)$ 上有原函数 $F_1(x)$，$(c,b]$ 上有原函数 $F_2(x)$，则

    $$
    \begin{align*}
      \int^b_a{f(x)\mathrm{d}x}=&\int^c_a{f(x)\mathrm{d}x}+\int^b_c{f(x)\mathrm{d}x}\\\\
      =&F_1(c-0)-F_1(a)+F_2(b)-F_2(c+0)
    \end{align*}
    $$

* 换元法

    $$
    \int^b_a{f(x)\mathrm{d}x}\xlongequal[a=g(\alpha),b=g(\beta)]{令x=g(u)}\int^\beta_\alpha{f\big[g(u)\big]\mathrm{d}\big[g(u)\big]}=\int^\beta_\alpha{f\big[g(u)\big]g^{'}(u)\mathrm{d}u}
    $$

    换元三换：
  * 换变量：$x=g(t)$
  * 换界限：$a=g(\alpha),b=g(\beta)$
  * 换积分：$f(x)\mathrm{d}x=f\big[g(u)\big]g^{'}(u)\mathrm{d}u$
* 分部积分法

    $$
    \int^b_a{u(x)v^{'}(x)\mathrm{d}x}=u(x)v(x)\Big|^b_a-\int^b_a{v(x)u^{'}(x)\mathrm{d}x}
    $$
* 定理
  * 奇偶周期性质
    * 若 $f(x)$ 为连续的奇函数，则 $\int^a_{-a}{f(x)\mathrm{d}x}=0$
    * 若 $f(x)$ 为连续的偶函数，则 $\int^a_{-a}{f(x)\mathrm{d}x}=2\int^a_0{f(x)\mathrm{d}x}$
    * 若 $f(x)$ 是以 $T$ 为周期的连续函数，则 $\int^{a+T}_a{f(x)\mathrm{d}x}=\int^T_0{f(x)\mathrm{d}x}$
  * 区间再现公式
    * 若 $f(x)$ 为连续函数，则 $\int^b_a{f(x)\mathrm{d}x}=\int^b_a{f(a+b-x)\mathrm{d}x}$
  * 华里士公式(点火公式)

      $$
      \begin{align*}
        \int^{\frac{\pi}{2}}_0{\sin^n{x}\mathrm{d}x}=\int^{\frac{\pi}{2}}_0{\cos^n{x}\mathrm{d}x}=&
        \begin{cases}
          \dfrac{n-1}{n}\cdot\dfrac{n-3}{n-2}\cdot\cdots\dfrac{2}{3}\cdot1,&n>1且为奇数\\\\
          \dfrac{n-1}{n}\cdot\dfrac{n-3}{n-2}\cdot\cdots\dfrac{1}{2}\cdot\dfrac{\pi}{2},&n为正偶数
        \end{cases}\\\\

        \int^{\pi}_0{\sin^n{x}\mathrm{d}x}=&
        \begin{cases}
          2\cdot\dfrac{n-1}{n}\cdot\dfrac{n-3}{n-2}\cdot\cdots\dfrac{2}{3}\cdot1,&n>1且为奇数\\\\
          2\cdot\dfrac{n-1}{n}\cdot\dfrac{n-3}{n-2}\cdot\cdots\dfrac{1}{2}\cdot\dfrac{\pi}{2},&n为正偶数
        \end{cases}\\\\

        \int^{\pi}_0{\cos^n{x}\mathrm{d}x}=&
        \begin{cases}
          0,&n>1且为奇数\\\\
          2\cdot\dfrac{n-1}{n}\cdot\dfrac{n-3}{n-2}\cdot\cdots\dfrac{1}{2}\cdot\dfrac{\pi}{2},&n为正偶数
        \end{cases}\\\\

        \int^{2\pi}_0{\sin^n{x}\mathrm{d}x}=\int^{2\pi}_0{\cos^n{x}\mathrm{d}x}=&
        \begin{cases}
          0,&n>1且为奇数\\\\
          4\cdot\dfrac{n-1}{n}\cdot\dfrac{n-3}{n-2}\cdot\cdots\dfrac{1}{2}\cdot\dfrac{\pi}{2},&n为正偶数
        \end{cases}
      \end{align*}
      $$
  
  * 三指公式

    $$
    \begin{align*}
      \int^b_a{e^{Ax}\cdot\sin{\left(Bx\right)}\mathrm{d}x}=\dfrac{
        \left.\left|
        \begin{matrix}
          \left[e^{Ax}\right]^{'} & \left[\sin{\left(Bx\right)}\right]^{'}\\
          e^{Ax} & \sin{\left(Bx\right)}
        \end{matrix}
        \right|\right|^b_a
      }{A^2+B^2}\\\\

      \int^b_a{e^{Ax}\cdot\cos{\left(Bx\right)}\mathrm{d}x}=\dfrac{
        \left.\left|
        \begin{matrix}
          \left[e^{Ax}\right]^{'} & \left[\cos{\left(Bx\right)}\right]^{'}\\
          e^{Ax} & \cos{\left(Bx\right)}
        \end{matrix}
        \right|\right|^b_a
      }{A^2+B^2}
    \end{align*}
    $$

### 1.3 变限积分计算

* 求导公式

    设 $F(x)=\int^{\phi_2(x)}_{\phi_1(x)}{f(t)\mathrm{d}t}$，其中 $f(x)$ 在区间 $[a,b]$ 上连续，可导函数 $\phi_2(x),\phi_1(x)$ 的值域在 $[a,b]$ 上。则在 $\phi_2(x),\phi_1(x)$ 的公共定义域上，有

    $$
    F^{'}(x)=\dfrac{\mathrm{d}\Big[\int^{\phi_2(x)}_{\phi_1(x)}{f(t)\mathrm{d}t}\Big]}{\mathrm{d}x}=f\big[\phi_2(x)\big]\phi^{'}_2(x)-f\big[\phi_1(x)\big]\phi^{'}_1(x)
    $$

    ***$f(t)$ 必须为单一变量函数，若为 $f(x,t)$ 或其他多元函数，求导前必须先换元！***
* 定理
  * $f(x)$ 为可积的奇函数 $\Rightarrow\int^x_0{f(t)\mathrm{d}t}$ 为偶函数
    * 若 $f(x)$ 是连续的奇函数，则 $\int^x_a{f(t)\mathrm{d}t}+C$ 也是偶函数，即 $f(x)$ 的全体原函数都是偶函数
  
  * $f(x)$ 为可积的偶函数 $\Rightarrow\begin{cases}
    \int^x_0{f(t)\mathrm{d}t}为奇函数\\\\
    \int^x_a{f(t)\mathrm{d}t}(a\neq0)
    \begin{cases}
      若\int^x_a{f(t)\mathrm{d}t}=\int^x_0{f(t)\mathrm{d}t},为奇函数\\\\
      若\int^x_a{f(t)\mathrm{d}t}\neq\int^x_0{f(t)\mathrm{d}t},为非奇非偶函数
    \end{cases}
  \end{cases}$
    * 若 $f(x)$ 是连续的偶函数，则在 $f(x)$ 的全体原函数中只有 $\int^x_0{f(t)\mathrm{d}t}$ 为奇函数

  * $f(x)$ 是周期为 $T$ 的可积函数，则

      $$
      \int^x_0{f(t)\mathrm{d}t}是以T为周期的周期函数\Leftrightarrow\int^T_0{f(x)\mathrm{d}x}=0
      $$

    * $\int^x_a{f(t)\mathrm{d}t}=\int^0_a{f(t)\mathrm{d}t}+\int^x_0{f(t)\mathrm{d}t}=C+\int^x_0{f(t)\mathrm{d}t}$ 也是以 $T$ 为周期的周期函数 $(a\neq0)$

### 1.4 反常积分计算

* 注意识别奇点
* $\Gamma$ 函数
  * 定义

      $$
      \Gamma(\alpha)=\int^{+\infty}_0{x^{\alpha-1}e^{-x}\mathrm{d}x}=2\int^{+\infty}_0{x^{2\alpha-1}e^{-x^2}\mathrm{d}x},(x>0)
      $$

  * 递推式

      $$
      \begin{align*}
        \Gamma(\alpha+1)=&\alpha\Gamma(\alpha)\\\\
        \Gamma(n+1)=&n!\,,n\in\N^+
      \end{align*}
      $$
  
  * 特殊值

      $$
      \begin{align*}
        \Gamma(1)=&1\\\\
        \Gamma(\dfrac{1}{2})=&\sqrt{\pi}
      \end{align*}
      $$

## 2 题目

* 基础30讲
  * 例9.1(凑微分法)
  * 例9.2(凑微分法)
  * ***例9.3(三角函数代换)***
  * 例9.4(换元法、分部积分法)
  * ***例9.5(三角函数代换、分部积分法、凑微分法、积分方程)***
  * 例9.6(凑微分法、分部积分法)
  * 例9.7(三角函数化简、凑微分法、分部积分法)
  * ***例9.8-9(有理函数积分)***
  * 例9.10(有理函数积分、凑平方)
  * 例9.12(不定积分定义、换元法)
  * 例9.13(三角函数代换、换元法、点火公式)
  * ***例9.14-15(换元法、奇偶性质)***
  * 例9.16(周期性证明)
  * 例9.17(区间再现公式证明)
  * 例9.18(区间再现公式、积分方程)
  * ***例9.19(不可积函数分部积分法)***
  * 例9.21(变限积分求导、泰勒公式)
  * ***例9.22(多元变限积分求导)***
  * 例9.23(变限积分奇偶性证明)
  * 例9.25(变限积分周期性证明)
  * ***例9.24(变限积分奇偶性)***
  * 例9.26(带奇点反常积分计算)
  * 例9.27(反常积分计算、换元法)
  * 例9.28(分部积分法建立递推式)
  * 例9.29($\Gamma$ 函数)
* 基础30讲课后题
  * 9.2(定积分再积分)
  * 9.7(换元法)
  * 9.8(换元法)
  * ***9.10(三角函数化简、保号性)***
  * 9.11(三角函数化简、积分方程)
  * ***9.12(换元法、裂项积分)***
  * 9.13(奇偶性质)
  * 9.14(三角函数化简)
  * ***9.15(变限积分计算)***
  * 9.16(换元法、变限积分求导)
  * 9.17(多元变限积分求导、分段函数求导)
* 1000题
  * ***01(常用积分)***
  * 03(换元法)
  * 04(凑微分法、裂项)
  * 05(换元法)
  * 06(凑微分法、凑平方)
  * 09(换元利用递推式)
  * 10(三角函数代换)
  * 12(洛必达、多元变限积分求导)
  * ***13(函数、连续、导数综合)***
  * 14(周期性)
  * ***15(函数、连续、导数综合)***
  * 16(多元变限积分求导)
  * 18(复杂部分可求导直接分部积分法)
  * 19(原函数)
  * ***20(凑分部积分)***
  * 21(基本公式)
  * 22(奇偶性质)
  * ***23($x$ 范围)***
  * ***24(积分极限)***
  * ***25(反三角函数性质)***
  * 26(换元法)
  * 27(同取积分构造方程)
  * 28(奇偶性质)
  * ***30(同取积分构造方程)***
  * ***31(洛必达、多元变限积分求导)***
  * 32(反函数、积分确定 $C$)
  * 33(洛必达、换元法)
  * ***34(复杂部分可求导直接分部积分法)***
  * 35(换元法)
  * 36(万能公式代换)
