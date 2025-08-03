# 一元函数积分学定理应用

## 1 知识点

### 1.1 积分等式

* 中值定理
  * 扩展的积分中值定理

    设 $f(x),g(x)$ 在区间 $[a,b]$ 上连续，且 $g(x)$ 在区间 $[a,b]$ 上**不变号**，则存在 $\xi\in[a,b]$，满足

    $$
    \int^b_a{f(x)g(x)\mathrm{d}x}=f(\xi)\int^b_a{g(x)\mathrm{d}x}
    $$

    当 $g(x)=1$ 时即为一般的积分中值定理
  * 多重罗尔/拉格朗日中值定理求高阶导
* 夹逼准则

  通过放缩将待求积分的被积函数上下界找出来，求极限时对上下界求极限用夹逼准则

* 积分法

  通过分部积分法获得高阶导或降低次数

### 1.2 积分不等式

* 函数单调性

  通过常数参数化处理整体信息，最后再取原始的常数带入分析(定积分 $\to$ 变上限积分)

* 拉格朗日中值定理

  看到 $f(x)$ 与 $f^{'}(x)$ 想到拉格朗日中值定理，将二者联系起来。必要时分区间用。多用于 $f(x)$ 一阶可导且某一端点值较简单的情况

* 泰勒公式

  多用于 $f(x)$ 二阶可导且 $f(x)$ 存在简单值的情况

* 积分方法

  常用分部积分法升/降导数阶数、保号性放缩

  * 分部积分法放缩
  $$
  \begin{align*}
    \left\lvert\int{u\mathrm{d}v}\right\rvert
    &\leq\left\lvert uv-\int{v\mathrm{d}u}\right\rvert\\
    &\leq\left\lvert uv\right\rvert+\left\lvert\int{v\mathrm{d}u}\right\rvert\\
    &\leq\left\lvert uv\right\rvert+\int{\left\lvert v\right\rvert\mathrm{d}u}
  \end{align*}
  $$

  * 分区间放缩
  $$
  \begin{align*}
    \left\lvert\int^b_a{u\mathrm{d}v}\right\rvert
    \leq\left\lvert\int^c_a{u\mathrm{d}v}\right\rvert+\left\lvert\int^b_c{u\mathrm{d}v}\right\rvert\\
    \leq\int^c_a{\left\lvert u\right\rvert\mathrm{d}v}+\int^b_c{\left\lvert u\right\rvert\mathrm{d}v}
  \end{align*}
  $$

* 牛顿莱布尼茨公式

  分区间凑出定积分，最后根据可加性凑出完整的定积分

* 总结

  $$
  \begin{align*}
    积分中值定理&: \int^b_a{f(x)\mathrm{d}x}=f\left(\xi\right)(b-a)\\\\
    扩展的积分中值定理&: \int^b_a{f(x)g(x)\mathrm{d}x}=f\left(\xi\right)\int^b_a{g(x)\mathrm{d}x}\\\\
    牛顿莱布尼茨公式&: \int^x_a{f^{'}(t)\mathrm{d}t}=f(x)-f(a)\\\\
    拉格朗日中值定理&: f(x)-f(a)=f^{'}\left(\xi\right)(x-a)\\\\
    变限积分求导&: \left[\int^{x+2}_x{f(t)\mathrm{d}t}\right]^{'}=f(x+2)-f(x)
  \end{align*}
  $$

## 2 题目

* 基础30讲
  * 例11.1(1)(扩展的积分中值定理证明)
  * 例11.1(2)(积分中值定理、放缩夹逼准则、变化的 $\xi$ 函数)
  * 例11.2(积分中值定理、罗尔中值定理、拉格朗日中值定理)
  * 例11.3(放缩、夹逼准则)
  * 例11.4(放缩、积分保号性、$\lim\limits_{x\to0}{x^a\ln{x}}=0,a>0$)
  * 例11.5(取整函数、夹逼准则)
  * 例11.6(分部积分)
  * 例11.7(缩放、常数参数化、变限积分单调性)
  * 例11.8(拉格朗日中值定理、积分绝对值保号性)
* 基础30讲课后题
  * 11.2(扩展的积分中值定理)
  * 11.4(单调性、常数参数化、牛顿莱布尼茨公式)
  * ***11.5(拉格朗日中值定理、不等式等号能否取到)***
  * ***11.6(泰勒公式、不等式等号能否取到)***
* 1000题
  * 01(零点定理证存在根、单调性证根的唯一性)
  * ***03(超区间求反三角函数、周期函数积分的 $n$ 与 $n+1$、夹逼准则)***
  * 05(罗尔中值定理、构造辅助函数)
  * 06(换元法)
  * 07(带值试、$-x$ 换元)
  * ***08(常数参数化、构造辅助函数)***
  * 11(换元法)
