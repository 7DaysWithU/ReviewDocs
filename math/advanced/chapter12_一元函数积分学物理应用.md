# 一元函数积分学物理应用

## 1 知识点

* 变力沿直线做功

  设方向沿 $x$ 轴正向的力函数为 $y=F(x),x\in[a,b]$，则物体沿 $x$ 轴从 $a$ 移动到 $b$ 时，变力 $F(x)$ 做功为

  $$
  W=\int^b_a{F(x)\mathrm{d}x}
  $$

  功的微元为 $\mathrm{d}W=F(x)\mathrm{d}x$

* 抽水做功

  设 $A(x)$ 为容器内水平面面积关于竖直方向 $x$ 的函数，则将容器内的水全部抽出所做的功为

  $$
  W=\int^b_a{x\cdot\rho gA(x)\mathrm{d}x}
  $$

  功的微元为
  $
  \begin{cases}
    W=Fx\\
    F=mg\\
    m=\rho V\\
    V=A(x)\mathrm{d}x
  \end{cases}\Rightarrow\mathrm{d}W=\rho gA(x)\mathrm{d}x\cdot x
  $

  * 特别注意总高度的选取，无论哪种建系方式，恒有 ***$总高度=排水口的高度-容器底底的高度$，且注意总高度一定是正数***。详见1000题04

* 静水压力

  设 $f(x)$ 为垂直浸没在水中的平板的右端关于竖直方向 $x$ 的函数，$h(x)$ 为左端的函数，则整个平板所受压力为

  $$
  F=\int^b_a{\rho\,g\,x\cdot\left[f\left(x\right)-h\left(x\right)\right]\mathrm{d}x}
  $$

  压力的微元为
  $
  \begin{cases}
    F=PS\\
    P=\rho gh
  \end{cases}
  \Rightarrow\mathrm{d}F=\rho\,g\,x\cdot\left[f\left(x\right)-h\left(x\right)\right]\mathrm{d}x
  $

* 引力

  设一长度为 $L$，线密度为 $\mu$ 的细棒，在细棒右端距离 $a$ 处有一质量为 $m$ 的质点 $M$。已知引力常量为 $G$，则细棒与质点间的引力为

  $$
  F=\int^0_{-L}{G\cdot\dfrac{m\cdot \mu\mathrm{d}x}{\left(a-x\right)^2}}
  $$

  引力的微元为
  $
  \begin{cases}
    F=G\cdot\dfrac{m_1m_2}{r^2}\\
    \mathrm{d}m_棒=\mu\mathrm{d}x\\
    r=(a-x)
  \end{cases}
  \Rightarrow\mathrm{d}F=G\cdot\dfrac{m\cdot\mu\mathrm{d}x}{\left(a-x\right)^2}
  $

## 2 进阶

### 2.1 求解物理应用题 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

* 物理问题 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{22} (转换等价表述)}$
  * 类型：变力沿直线做功、变速直线运动位移、抽水做功、静水压力、引力、自行建立微元表达式
  * 建系时注意各种变量的正负，设计速度时可用分部积分法转换路程速度加速度，注意分力的求解

## 3 题目

* 基础30讲
  * 例12.1(变力沿直线做功)
  * 例12.2(抽水做功)
  * 例12.3(静水压力)
* 基础30讲课后习题
  * ***12.3(高空抽水)***
* 1000题基础
  * 01(引力、力的方向、力分解)
  * ***02(净水压力、计算)***
  * 03(引力、变限积分的极限)
  * ***04(抽水做功、定高度)***
  * ***05(抽水液面高度变化率)***
  * 06(灌水液面高度变化率)
  * ***07(双变化率、恒等变形、链式求导、不定积分求通解)***
  * 08(静水压力、椭圆)
* 强化36讲
  * 例12.1(物体的线密度，注意方向与长度的关系)
  * ***例12.2(变速直线运动位移、路程速度加速度关系、分部积分法)***
  * 例12.3(抽水做功)
  * 例12.4(静水压力)
  * ⛔***例12.5(引力的分力)***
  * 例12.6(微元法建立表达式)
* 1000题强化
  * ***01(静水压力不好求左右函数时，直接求微元块的边长、三角形相似)***
  * ⭐***02(求变化率)***
  * ***04(不均匀密度图形的重心)***
