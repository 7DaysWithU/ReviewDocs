# 一元函数积分学几何应用

## 1 知识点

* 平面图形面积
  * 平面直角坐标系

    曲线 $y=f_1(x)$ 与 $y=f_2(x)$ 及 $x=a,x=b(a<b)$ 所围平面图形的面积为

    $$
    S=\int^b_a{\Big\lvert f_1(x)-f_2(x)\Big\rvert\mathrm{d}x}
    $$
  * 极坐标系

    曲线 $r=r_1(\theta)$ 与 $r=r_2(\theta)$ 与两射线 $\theta=\alpha,\theta=\beta(0<\beta-\alpha\leq2\pi)$ 所围平面图形的面积为

    $$
    S=\dfrac{1}{2}\int^{\beta}_{\alpha}{\Big\lvert r_1^2(\theta)-r_2^2(\theta)\Big\rvert\mathrm{d}\theta}
    $$
  * 参数方程

    曲线 $\begin{cases}x=x(t) \\ y=y(t)\end{cases},t\in[\alpha, \beta]$ 所围平面图形的面积为

    $$
    S=\int^b_a{\Big\lvert y(t)\Big\rvert\mathrm{d}x}=\int^{\beta}_{\alpha}{\Big\lvert y(t)\cdot x^{'}(t)\Big\rvert\mathrm{d}t}
    $$

    **注意 $\mathrm{d}x=x^{'}(t)\mathrm{d}t$ 后要同步更改上下限**
* 旋转体体积
  * 绕 $x$ 轴旋转

    曲线 $y=f(x)$ 与 $x=a,x=b(a<b)$ 及 $x$ 轴所围成的曲边梯形绕 $x$ 轴旋转一周得到的旋转体体积为

    $$
    V=\int^b_a{\pi\left[f(x)^2\right]\mathrm{d}x}
    $$
  * 绕 $y$ 轴旋转

    曲线 $y=f(x)$ 与 $x=a,x=b(0\leq a<b)$ 及 $x$ 轴所围成的曲边梯形绕 $y$ 轴旋转一周得到的旋转体体积为

    $$
    V=\int^b_a{2\pi x\lvert f(x)\rvert\mathrm{d}x}
    $$
  * 平面曲线绕定直线旋转

    平面曲线 $L$：$y=f(x),x\in[a,b]$，且 $f(x)$ 可导 </br>
    定直线 $L_0$：$A x+B y+C=0$，且过 $L_0$ 的任意一条垂线与 $L$ 至多一个交点 </br>
    则 $L$ 绕 $L_0$ 选择一周所得旋转体的体积为

    $$
    V=\dfrac{\pi}{\left(A^2+B^2\right)^\frac{3}{2}}\int^b_a{\left[Ax+Bf(x)+C\right]^2\lvert Af^{'}(x)-B\rvert\mathrm{d}x}
    $$
  * 绕极轴旋转

    设平面图形 $D=\{(r,\theta)\,|\,0\leq r\leq r(\theta),\,\theta\in[\alpha,\beta]\subset[0,\pi]\}$，则 $D$ 绕极轴旋转一周所得旋转体的体积为

    $$
    V=\dfrac{2}{3}\pi\int^{\beta}_{\alpha}{r^3(\theta)\sin{\theta}\mathrm{d}\theta}
    $$
* 函数平均值

  设 $x\in[a,b]$，由定积分中值定理可得，函数 $f(x)$ 在 $[a,b]$ 上的平均值为

  $$
  \begin{align*}
    \overline{f}&=\dfrac{1}{b-a}\int^b_a{f(x)}\\\\
    \Rightarrow\overline{f}&=f(\xi),\xi\in[a,b]
  \end{align*}
  $$

* 平面图形形心
  
  设平面区域 $D=\{(x,y)|a\leq x\leq b,0\leq y\leq f(x)\}$，$y=f(x)$ 在 $[a,b]$ 上连续，则 $D$ 的形心坐标为

  $$
  \begin{align*}
    \overline{x}&=\dfrac{\int^b_a{xf(x)\mathrm{d}x}}{\int^b_a{f(x)\mathrm{d}x}}\\\\
    \overline{y}&=\dfrac{\dfrac{1}{2}\int^b_a{f^2(x)\mathrm{d}x}}{\int^b_a{f(x)\mathrm{d}x}}
  \end{align*}
  $$

* 平面曲线弧长
  * 平面光滑曲线由直角坐标方程 $y=f(x),x\in[a,b]$ 给出，则弧长

    $$
    s=\int^b_a{\sqrt{1+\left[f^{'}\left(x\right)\right]^2}\mathrm{d}x}
    $$

  * 平面光滑曲线由参数方程 $\begin{cases}
    x=x(t)\\
    y=y(t)
  \end{cases},t\in[\alpha, \beta]$ 给出，则弧长
  
    $$
    s=\int^{\beta}_{\alpha}{\sqrt{\left[x^{'}\left(t\right)\right]^2+\left[y^{'}\left(t\right)\right]^2}\mathrm{d}t}
    $$

  * 平面光滑曲线由极坐标方程 $r=r(\theta),\theta\in[\alpha,\beta]$ 给出，则弧长

    $$
    s=\int^{\beta}_{\alpha}{\sqrt{\left[r\left(\theta\right)\right]^2+\left[r^{'}\left(\theta\right)\right]^2}\mathrm{d}\theta}
    $$

* 旋转体侧面积
  * 曲线 $L$：$y=f(x),x\in[a,b]$ 绕 $x$ 轴旋转一周所得旋转体侧面积为

    $$
    S=2\pi\int^b_a{\left\lvert f\left(x\right)\right\rvert\sqrt{1+\left[f^{'}\left(x\right)\right]^2}\mathrm{d}x}
    $$

  * 曲线 $L$：$\begin{cases}
    x=x(t)\\
    y=y(t)
  \end{cases},t\in[\alpha, \beta]$ 绕 $x$ 轴旋转一周所得旋转体侧面积为
  
    $$
    S=2\pi\int^{\beta}_{\alpha}{\left\lvert y\left(t\right)\right\rvert\sqrt{\left[x^{'}\left(t\right)\right]^2+\left[y^{'}\left(t\right)\right]^2}\mathrm{d}t}
    $$

  * 曲线 $L$：$r=r(\theta),\theta\in[\alpha,\beta]$ 绕 $x$ 轴旋转一周所得旋转体侧面积为

    $$
    S=2\pi\int^{\beta}_{\alpha}{\left\lvert r\left(\theta\right)\sin{\theta}\right\rvert\sqrt{\left[r\left(\theta\right)\right]^2+\left[r^{'}\left(\theta\right)\right]^2}\mathrm{d}\theta}
    $$

* 平行截面面积已知的立体体积

  在区间 $[a,b]$ 上，垂直于 $x$ 轴的平面截立体 $\Omega$ 所得到的截面面积为 $x$ 的 **连续** 函数 $A(x)$，取体积微元 $\mathrm{d}V=A(x)\mathrm{d}x$，则 $\Omega$ 体积为

  $$
  V=\int^b_a{A(x)\mathrm{d}x}
  $$

  ***常用微元划分思想***

## 2 进阶

### 2.1 计算图形的相关几何量 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

* 计算公式与基本图形的几何量大观 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作)}$
  * 所围面积、旋转体体积、弧长、旋转体侧面积、形心、平均值、立体体积
  * 心形线、阿基米德螺线、平摆线、星形线、三叶玫瑰线、四叶玫瑰线

* 各种函数表达式的几何量计算 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式)}$

## 3 题目

* 基础30讲
  * 例10.1(递推式、未定式)
  * ***例10.2(参数方程求平面面积、换元法)***
  * 例10.3(伯努利爽纽线、极坐标平面面积)
  * ***例10.4(分段求平面面积、$e^{ax}\cdot bx$ 求积分)***
  * 例10.5(绕 $x$ 轴、定义域)
  * 例10.6(绕 $y$ 轴、坐标轴变换)
  * ***例10.7(平面图形面积、平面曲线绕定直线旋转、坐标轴变换)***
  * ***例10.8(函数平均值、构造变限积分)***
  * 例10.9(形心)
  * 例10.10(平面直角方程弧长)
  * 例10.11(极坐标方程弧长)
  * 例10.12(表面积、换元法)
  * 例10.13(星形线、表面积、对称性)
  * ***例10.14(旋转体体积、微元法)***
* 基础30讲课后题
  * 10.2(取体积微元)
  * 10.8(参数方程、换元法)
  * ***10.9(分段函数取微元、不能用公式)***
* 1000题基础
  * 05(未知f(x)直接分部积分法)
  * ***08(变化率)***
  * ***11(反函数切换积分视角)***
  * 15($\sec^3{x}$ 积分)
  * ***16(绕非坐标轴直线旋转)***
  * 17(反函数切换积分视角)
  * 19(变化率、参数方程)
* 强化36讲
  * 例10.1(心形线弧长、面积、旋转体体积、半角公式)
  * 例10.2(阿基米德螺线面积)
  * 例10.3(三叶玫瑰线面积)
  * ***例10.4(平摆线弧长、面积、旋转体体积)***
  * 例10.5(星形线弧长、面积、旋转体体积)
  * ***例10.6(笛卡尔叶形线面积、渐近线)***
  * 例10.7(极限定义的幂函数)
  * 例10.8(积分定义的幂函数)
  * ***例10.9(已知旋转体体积反求幂函数参数、 $a^{f(x)}$ 特殊情况下的积分)***
  * ***例10.10(求三角函数定义的函数的弧长、半角公式)***
  
    > 注意函数的定义域。利用半角公式 $\cos{2\theta}=\cos^2{\theta}-\sin^2{\theta}$ 化简 $\sqrt{1\pm\cos{\theta}}$ 的情况
  
  * ***例10.11(x,y互换位置)***
  * ⭐***例10.12(函数绕平行坐标轴的直线旋转)***
  
    > 若函数 $f(x)$ 绕 $y=a$ 旋转，求旋转体的体积，则 $r=f(x)-a$，计算积分 $\int^b_a{\pi r^2\mathrm{d}x}$ 即可。绕 $x$ 轴旋转其实是绕 $y=0$ 旋转的特殊情况
  
  * 例10.13(求指数函数定义的函数的旋转体体积)
  * ⭐***例10.14(悬链线函数、经典化简)***
  
    > $\sqrt{1+\left(\dfrac{1}{2}\Box-\dfrac{1}{2\Box}\right)^2}=\sqrt{\left(\dfrac{1}{2}\Box+\dfrac{1}{2\Box}\right)^2}$，本质就是配平方

* 1000题强化
  * ***04(二阶常系数非齐次线性微分方程、极限母为零子也为0、面积、旋转体体积)***
  * ⭐***06(取微元 $\mathrm{d}y$、x,y互换位置、函数绕平行坐标轴的直线旋转)***
  * ⭐***07(注意函数的定义域、三角函数分段积分、等比级数)***
  
    > 等比级数求和公式：$S=\dfrac{a_1}{1-q},\,\lvert q\rvert<1$
  
  * ⭐***09(一阶线性微分方程、积分去绝对值、分类讨论常数 $C$、利用函数性态证明三次方程无解)***
  * ***11(一阶线性微分方程、计算、同1000题强化07)***
  * ⭐***12(平均值、多元函数变限积分换元)***
  
    > 见到 $f(x)\int^x_0{f(u)\mathrm{d}u}$，一般令 $F(x)=\int^x_0{f(u)\mathrm{d}u}$，则 $f(x)\int^x_0{f(u)\mathrm{d}u}=F^{'}(x)F(x)$，且 $\int{F^{'}(x)F(x)\mathrm{d}x}=\int{F(x)\mathrm{d}[F(x)]}=\dfrac{1}{2}F^2(x)+C$

  * ***13(定积分带值时如遇无定义点需要分区间用牛顿莱布尼茨公式，无定义点取极限)***
  * ⭐***14(平均值)***
  
    > 若 $g(x)$ 的一个原函数是 $f(x)$，则 $f(x)=\displaystyle\int{g(x)\mathrm{d}x}=\displaystyle\int^x_a{g(x)\mathrm{d}x}$。若写作变限积分形式，则需要题目条件求出具体的 $a$
    >
    > 求平均值的积分时，既可以用分部积分消项(有特殊值或特殊结构)，也可以积变限积分交换积分次序(题目不直接给出 $f(x)$，而是给出其原函数)
  
  * ⛔***19(一阶线性微分方程积出 $\ln{\lvert\phi(x)\rvert}$ 可以忽略绝对值、先积y、函数绕平行坐标轴的直线旋转)***
  * ***20(旋转体简单时可以直接用圆锥体体积公式之类的公式直接求，积分麻烦)***
  * ***21($x(y)$ 函数、求导抵消积分、微分方程分离参变量)***
  * ***22(双曲线、积y、$\int{\sqrt{a^2+x^2}\mathrm{d}x}$)***
  * ***23(微分方程分离变量、利用 $\sin{2x}$ 凑平方和公式)***
  
    > $1+\sin{2x}=(\sin{x}+\cos{x})^2$

  * ⭐***24(形心、构造函数证明积分不等式)***
  * ***25(计算、平摆线旋转体体积表面积)***
