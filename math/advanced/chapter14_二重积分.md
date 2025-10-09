# 二重积分

## 1 知识点

### 1.1 概念、性质、对称性

* 概念

  设 $f(x,y)$ 是有界闭区域 $D$ 上的有界函数，将闭区间 $D$ 任意分割成 $n$ 个小闭区间 $\Delta\sigma_1,\Delta\sigma_2,\cdots,\Delta\sigma_n$，其中 $\Delta\sigma_i$ 表示第 $i$ 个小闭区域，也表示它的面积。在每个 $\Delta\sigma_i$ 上任取一点 $f(\xi_i,\eta_i)$，作乘积 $f(\xi_i,\eta_i)\Delta\sigma_i\,(i=1,2,\cdots,n)$，再作和 $\sum^n_{i=1}{f(\xi_i,\eta_i)\Delta\sigma_i}$。当 $\lambda=\max{\left\{\Delta\sigma_i\right\}}\to0$ 时，和的极限总是存在，且与 $\Delta\sigma_i$ 的分割方法与点 $f(\xi_i,\eta_i)$ 的取法无关，则称此极限值为函数 $f(x,y)$ 在闭区域 $D$ 上的二重积分，记作 $\iint_D{f(x,y)\mathrm{d}\sigma}$，即
  
  $$
  \iint_D{f(x,y)\mathrm{d}\sigma}=\lim\limits_{\lambda\to0}{\sum^n_{i=1}{f(\xi_i,\eta_i)\Delta\sigma_i}}
  $$

  当将区间 $[a,b]$ 和 $[c,d]$ $N$ 等分时，每个小区间为
  
  $$
  \begin{align*}
    I_{x_k}=\left[a+\dfrac{b-a}{N}(k-1),a+\dfrac{b-a}{N}k\right] \\\\
    I_{y_k}=\left[c+\dfrac{d-c}{N}(k-1),c+\dfrac{d-c}{N}k\right]
  \end{align*}
  $$

  当点 $(\xi_{x_k},\xi_{y_k})$ 满足 $\xi_{x_k}\in I_{x_k},\,\xi_{y_k}\in I_{y_k}$ 时，可进一步写为

  $$
  \iint_D{f(x,y)\mathrm{d}\sigma}=\lim\limits_{N\to\infty}{\sum^N_{i=1}{\sum^N_{j=1}{f(\xi_{x_k},\xi_{y_k})\cdot\dfrac{b-a}{N}\cdot \dfrac{d-c}{N}}}}
  $$
  
  **若 $f(x,y)$ 在有界闭区域 $D$ 上连续，则二重积分 $\iint_D{f(x,y)\mathrm{d}\sigma}$ 一定存在**

* 性质
  * 区域面积

    $\iint_D{1\cdot\mathrm{d}\sigma}=A$，其中 $A$ 为 $D$ 的面积

  * 可积函数必有界

    当 $f(x,y)$ 在有界闭区域 $D$ 上可积时，$f(x,y)$ 在 $D$ 上必有界

  * 积分的线性性质

    $\iint_D{\left[k_1f\left(x,y\right)\pm k_2f\left(x,y\right)\right]\mathrm{d}\sigma}=k_1\iint_D{f\left(x,y\right)\mathrm{d}\sigma}\pm k_2\iint_D{f\left(x,y\right)\mathrm{d}\sigma}$，其中 $k_1,k_2$ 为常数

  * 积分的可加性

    $\iint_D{f(x,y)\mathrm{d}\sigma}=\iint_{D_1}{f(x,y)\mathrm{d}\sigma}+\iint_{D_2}{f(x,y)\mathrm{d}\sigma}$，其中 $D_1\cup D_2=D$，且 $D_1\cap D_2=\varnothing$

  * 积分的保号性

    当 $f(x,y),g(x,y)$ 在有界闭区域 $D$ 上可积时，若在 $D$ 上有 $f(x,y)\leq g(x,y)$，则

    $$
    \iint_D{f(x,y)\mathrm{d}\sigma}\leq\iint_D{g(x,y)\mathrm{d}\sigma}
    $$

    特别地，有

    $$
    \left\lvert\iint_D{f(x,y)\mathrm{d}\sigma}\right\rvert\leq\iint_D{\left\lvert f(x,y)\right\rvert\mathrm{d}\sigma}
    $$

  * ⚠️二重积分估值定理

    设 $M=\max\limits_D{\left\{f(x,y)\right\}}\,,m=\min\limits_D{\left\{f(x,y)\right\}}$，$A$ 为 $D$ 的面积，则有

    $$
    mA\leq\iint_D{f(x,y)\mathrm{d}\sigma}\leq MA
    $$

    **可配合拉格朗日乘数法求二元函数区域最值，再确定区域内二重积分的范围**

  * ⚠️二重积分中值定理

    设 $f(x,y)$ 在有界闭区域 $D$ 上连续，$A$ 为 $D$ 的面积，则在 $D$ 上至少存在一点 $(\xi,\eta)$，使得

    $$
    \iint_D{f(x,y)\mathrm{d}\sigma}=f(\xi,\eta)A
    $$

    **当被积函数是抽象函数或非常难算时，可以考虑中值定理处理(基础30讲例14.2)**

  * ⚠️扩展的二重积分中值定理

    设 $f(x,y),g(x,y)$ 在有界闭区域 $D$ 上连续，且 $g(x,y)$ 在 $D$ 上不变号，则在 $D$ 上至少存在一点 $(\xi,\eta)$，使得

    $$
    \iint_D{f(x,y)\cdot g(x,y)\mathrm{d}\sigma}=f(\xi,\eta)\cdot\iint_D{g(x,y)\mathrm{d}\sigma}
    $$

  * 累次积分计算

    **若确定先积部分相当于后积部分为常数时，可以直接计算后积部分**。常用于带变限积分的情况

* 对称性
  * 普通对称性

    * 若 $D$ 关于 $x=a$ 对称，$(x,y)$ 关于 $x=a$ 的对称点为 $(2a-x,y)$，则

      $$
      \iint_D{f(x,y)\mathrm{d}\sigma}=
      \begin{cases}
          2\iint_{D_1}{f(x,y)\mathrm{d}\sigma},&f(x,y)=f(2a-x,y)\\
          0,&f(x,y)=-f(2a-x,y)
      \end{cases}
      $$

      其中 $D_1$ 为 $x=a$ 一侧的部分

      **当 $a=0$ 时为 $f(x,y)$ 关于 $y$ 轴对称**

    * 若 $D$ 关于 $y=a$ 对称，$(x,y)$ 关于 $x=a$ 的对称点为 $(x,2a-y)$，则

      $$
      \iint_D{f(x,y)\mathrm{d}\sigma}=
      \begin{cases}
          2\iint_{D_1}{f(x,y)\mathrm{d}\sigma},&f(x,y)=f(x,2a-y)\\
          0,&f(x,y)=-f(x,2a-y)
      \end{cases}
      $$

      其中 $D_1$ 为 $y=a$ 一侧的部分

      **当 $a=0$ 时为 $f(x,y)$ 关于 $x$ 轴对称**

    * 若 $D$ 关于原点对称，$(x,y)$ 关于原点的对称点为 $(-x,-y)$，则

      $$
      \iint_D{f(x,y)\mathrm{d}\sigma}=
      \begin{cases}
          2\iint_{D_1}{f(x,y)\mathrm{d}\sigma},&f(x,y)=f(-x,-y)\\
          0,&f(x,y)=-f(-x,-y)
      \end{cases}
      $$

      其中 $D_1$ 为关于原点对称的半个部分

    * 若 $D$ 关于 $y=x$ 对称，$(x,y)$ 关于 $y=x$ 的对称点为 $(y,x)$，则

      $$
      \iint_D{f(x,y)\mathrm{d}\sigma}=
      \begin{cases}
          2\iint_{D_1}{f(x,y)\mathrm{d}\sigma},&f(x,y)=f(y,x)\\
          0,&f(x,y)=-f(y,x)
      \end{cases}
      $$

      其中 $D_1$ 为关于 $y=x$ 对称的半个部分

  * 轮换对称性

    **在直角坐标系下**，若把 $x,y$ 对调，区域 $D$ 不变(或区域 $D$ 关于 $y=x$ 对称)，则有

    $$
    \iint\limits_{D(x,y)}{f(x,y)\,\mathrm{d}x\,\mathrm{d}y}=\iint\limits_{D(y,x)}{f(y,x)\,\mathrm{d}y\,\mathrm{d}x}
    $$

    由于 $f(x,y),f(y,x)$ 都不好算，但

    $$
    I=\dfrac{1}{2}\left[\iint\limits_{D(x,y)}{f(x,y)\,\mathrm{d}x\,\mathrm{d}y}+\iint\limits_{D(y,x)}{f(y,x)\,\mathrm{d}y\,\mathrm{d}x}\right]
    $$

    两个积分值根据可加性相加后被积函数可能就好算了

### 1.2 计算

* 直角坐标系
  * $X$ 型区域

    上下是曲边 $y=\phi_1(x),y=\phi_2(x)$，左右是直线 $x=a,x=b$

    $$
    \iint_D{f(x,y)\mathrm{d}\sigma}=\displaystyle\int^b_a{\mathrm{d}x}\displaystyle\int^{\phi_2(x)}_{\phi_1(x)}{f(x,y)\mathrm{d}y}
    $$

  * $Y$ 型区域

    左右是曲边 $x=\psi_1(x),x=\psi_2(x)$，上下是直线 $y=a,y=b$

    $$
    \iint_D{f(x,y)\mathrm{d}\sigma}=\displaystyle\int^b_a{\mathrm{d}y}\displaystyle\int^{\psi_2(y)}_{\psi_1(y)}{f(x,y)\mathrm{d}x}
    $$

  **二重积分严格要求 $\begin{cases}a<b \\ \phi_1(x)<\phi_2(x)或\psi_1(x)<\psi_2(x)\end{cases}$，即保证积分上下界为从小到大，否则必须换上下界**

  **对于不可积函数或难积分函数可以考虑交换积分顺序**

  $$
  \text{后积先定限，限内画条线}\\
  \text{先交写下限，后交写上限}
  $$

* 极坐标系

  与中心对称图像有关，**区域微元 $\mathrm{d}\sigma=\mathrm{d}r\cdot r\mathrm{d}\theta$**

  * 极点在区域外

    $$
    \iint_D{f(x,y)\mathrm{d}\sigma}=\displaystyle\int^{\beta}_{\alpha}{\mathrm{d}\theta}\displaystyle\int^{r_2(\theta)}_{r_1(\theta)}{f(r\cos{\theta},r\sin{\theta})r\mathrm{d}r}
    $$

  * 极点在区域边界上

    $$
    \iint_D{f(x,y)\mathrm{d}\sigma}=\displaystyle\int^{\beta}_{\alpha}{\mathrm{d}\theta}\displaystyle\int^{r(\theta)}_{0}{f(r\cos{\theta},r\sin{\theta})r\mathrm{d}r}
    $$

  * 极点在区域内

    $$
    \iint_D{f(x,y)\mathrm{d}\sigma}=\displaystyle\int^{2\pi}_{0}{\mathrm{d}\theta}\displaystyle\int^{r(\theta)}_{0}{f(r\cos{\theta},r\sin{\theta})r\mathrm{d}r}
    $$

  **若被积函数为 $f(x^2+y^2),f(\dfrac{x}{y}),f(\dfrac{y}{x})$ 等形式，或积分区域为圆或圆的一部分，则优先考虑使用极坐标系处理；否则优先考虑直角坐标系处理**

* 换元法

  若存在 $\begin{cases}x=x(u,v) \\ y=y(u,v)\end{cases}$ 是 $(x,y)$ 面到 $(u,v)$ 面的一对一映射，且 $x=x(u,v)\,,y=y(u,v)$ 存在一阶连续偏导，$\dfrac{\partial(x,y)}{\partial(u,v)}\neq0$ 时，有
  
  $$
  \iint_{D_{xy}}{f(x,y)\mathrm{d}x\mathrm{d}y}
  \xlongequal[y=y(u,v)]{x=x(u,v)}
  \iint_{D_{uv}}{f\left[x\left(u,v\right),y\left(u,v\right)\right]\cdot\left\lvert\det{J}\right\rvert\cdot\mathrm{d}u\mathrm{d}v}
  $$

  其中，公式中为 **雅可比行列式的绝对值**，雅可比行列式的计算方式如下：
  
  $$
  \det{J}=\dfrac{\partial(x,y)}{\partial(u,v)}=
  \begin{vmatrix}
    \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v}\\\\
    \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v}
  \end{vmatrix}
  $$

  **此外，新区域 $D_{uv}$ 需要将 $\begin{cases}x=x(u,v) \\ y=y(u,v)\end{cases}$ 代回旧区域 $D_{xy}$ 满足的约束式中，从中反解出 $u,v$ 满足的约束式，即为新区域 $D_{uv}$**

* **⚠️广义极坐标系**

  若积分区域 $D$ 为椭圆 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$，则可令 $\begin{cases}x=a\cdot r\cos{\theta} \\ y=b\cdot r\sin{\theta}\end{cases}$，则积分可写作
  
  $$
  \displaystyle\int^{\theta_2}_{\theta_1}{\mathrm{d}\theta}\displaystyle\int^{r_2}_{r_1}f(r,\theta)\cdot abr\cdot\mathrm{d}r
  $$

  ***特别注意，由于原区域 $D$ 为椭圆，新区域 $D^{'}$ 为圆，因此 $\theta,r$ 新的上下限均需带回原式重新计算 !!!；$abr$ 项为换元需要额外乘的雅可比行列式的快捷结果***
  
  **广义极坐标系由狭义极坐标结合换元法得到，极其适合在椭圆区域 $D$ 上使用。对于其他类型的区域可根据区域性质进行类似的换元操作**

## 2 进阶

### 2.1 计算二重积分 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

* 和式极限 $\textcolor{Cyan}{\text{D}_\text{22} (转换等价表述)}$

  常考 $[0,1]$ 区间，但也要留意特殊点额区间特殊分割方法(详见[一元函数积分学概念-知识点-定积分](./chapter8_%E4%B8%80%E5%85%83%E5%87%BD%E6%95%B0%E7%A7%AF%E5%88%86%E5%AD%A6%E6%A6%82%E5%BF%B5.md#12-定积分)、[一元函数积分学概念-进阶-其他分割取高型](./chapter8_%E4%B8%80%E5%85%83%E5%87%BD%E6%95%B0%E7%A7%AF%E5%88%86%E5%AD%A6%E6%A6%82%E5%BF%B5.md#2-进阶))。通过化简化成二重积分对应的极限形式即可

* 交换积分顺序 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作)}$

  常见的可积不可求积函数如下
  
  $$
  \begin{matrix}
    \displaystyle\int{\dfrac{\sin{x}}{x}\mathrm{d}x} & \displaystyle\int{\dfrac{\cos{x}}{x}\mathrm{d}x} & \displaystyle\int{\dfrac{\ln{(1+x)}}{x}\mathrm{d}x} & \displaystyle\int{\dfrac{1}{\ln{x}}\mathrm{d}x} \\\\
    \displaystyle\int{\sin{x^2}\mathrm{d}x} & \displaystyle\int{\cos{x^2}\mathrm{d}x} & \displaystyle\int{\sin{\dfrac{1}{x}}\mathrm{d}x} & \displaystyle\int{\cos{\dfrac{1}{x}}\mathrm{d}x} \\\\
    \displaystyle\int{\dfrac{\tan{x}}{x}\mathrm{d}x} & \displaystyle\int{\tan{x^2}\mathrm{d}x} & \displaystyle\int{\dfrac{e^x}{x}\mathrm{d}x} & \displaystyle\int{e^{ax^2+bx+c}\mathrm{d}x}(a\neq 0)
  \end{matrix}
  $$

  * 如果是可积不可求积或求积特别麻烦，考虑交换积分顺序再积
  * 变限积分求导时可考虑交换积分顺序以便于求导
  
* 积分保号性 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{22} (转换等价表述)}$

* 积分对称性 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{44} (善于发现对称)}$

  常用对称性和奇偶性消项简化计算

* 二重积分常用结论 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作)}$
  * 被积函数是圆和椭圆的
  * 二重积分中值定理极其扩展

* 二重积分计算法 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作)}$
  * 普通的直角坐标系、极坐标系
  * 换元平移坐标系、椭圆极坐标系、盲极坐标系

## 3 题目

* 基础30讲
  * 例14.1(二重积分正负、保号性)
  * ***例14.2(二元函数连续、二重积分导数、椭圆、中值定理)***
  * 例14.3(普通对称性)
  * 例14.4(轮换对称性)
  * 例14.5(交换上下限、超区间求 $\arcsin$)
  * ***例14.6(交换积分顺序、不可积函数)***
  * ***例14.7(交换积分顺序、基本积分法)***
  * 例14.8(轮换对称性、极坐标系)
  * ***例14.9(描点绘图、极坐标系、计算)***
  * ***例14.10(累次积分计算)***
  * ***例14.11($\Gamma$ 函数、积分与变量无关性)***
  * 例14.12($\Gamma$ 函数)
  * ***例14.13(同阶无穷小、$\Gamma$ 函数、洛必达法则)***
  * 例14.14(极坐标系)
  * ***例14.15(换元法)***
* 基础30讲课后习题
  * 14.3(极坐标系转直角坐标系)
  * 14.4(直角坐标系转极坐标系、凑微分)
  * 14.7(普通对称性)
  * 例14.8(计算、普通对称性)
  * ***例14.10($\sec$ 区域、极坐标系转直角坐标系、点火公式)***
  * ***例14.11($\Gamma$ 函数、反常积分)***
  * ***例14.12(二重积分最大值(被积函数 $\geq0$)、广义极坐标系)***
* 1000题基础
  * 01(区域围法)
  * ***02(二重积分中值定理、极限趋于点)***
  * 03(换元法、普通对称性)
  * 05(轮换对称性)
  * 10(极坐标定上下限、点火公式换元)
  * 11(极坐标定上下限、计算)
  * ***13(广义极坐标系)***
  * 14(轮换对称性)
  * ***15(拆项用普通对称性)***
  * 16(普通对称性、点火公式、$\sqrt{x^2}=\lvert x\rvert$)
  * 20(计算)
  * 21(计算)
  * ***22(圆平移换元)***
  * ***24(根式换元)***
* 强化36讲
  * 例14.1(和式极限)
  * 例14.2(可积不可求积交换积分顺序)
  * 例14.3(求积麻烦交换积分顺序)
  * ***例14.4(二重积分最大值)***
  
    > ***示例：求二重积分 $\displaystyle\iint{(1-x^2-y^2)\mathrm{d}\sigma}$ 取最大值的区域***
    >
    > 显然区域内应让 $1-x^2-y^2\geq 0$，则区域就是 $D=\set{(x,y)\,|\,x^2+y^2\leq 1}$

  * ***例14.5(轮换对称性)***
  * ⭐***例14.6(极坐标系转直角坐标系、积分计算 $\int{\sqrt{a^2-x^2}\mathrm{d}x}$)***
  
    > 极坐标系下 $D=\set{(r,\theta)\,|\,0\leq\theta\leq\dfrac{\pi}{4},0\leq r\leq\sec{\theta}}$，由 $\theta$ 显然看出边界是 $y=x$，起点是原点。当 $r=\sec{\theta}$ 时，即为 $r=\dfrac{1}{\cos{\theta}}\Rightarrow r\cos{\theta}=1\Rightarrow x=1$
    >
    > ***用 $\begin{cases}x=r\cos{\theta} \\ y=r\sin{\theta}\end{cases}$ 将极坐标系转成直角坐标系***

  * ⭐***例14.7(直角坐标系转极坐标系、二次型椭圆)***
  
    > ***示例：画出曲线 $x^2+y^2-xy=1$***
    >
    > 详见[番外-ep0二次型与椭圆](../_extra/ep0_%E4%BA%8C%E6%AC%A1%E5%9E%8B%E4%B8%8E%E6%A4%AD%E5%9C%86.md)

  * 例14.8(平移换元)
* 1000题强化
  * ⭐***04(平均值、二重积分换序、变限积分换元、二重积分的内积分当做原函数凑微分)***
  
    > $\displaystyle\int{\mathrm{d}x\int{f(x,y)\mathrm{d}y}}=\int{\left[\int{f(x,y)\mathrm{d}y}\right]\mathrm{d}x}$，即内层积分可以视作外层积分被积函数的一部分，就可以用单重积分的视角去尝试凑微分、换元操作

  * ***06(星形线、偶倍奇零)***
  
    > 遇见复杂的项先别急着算，必须先看看能不能用奇偶性化简

  * ⛔***07(可积不可求积交换积分顺序、极坐标交换积分顺序、凑微分、换元法求新区域)***
  
    > * 极坐标交换积分顺序与直角坐标系操作一样，都是后积先定限那个口诀。因此，当极坐标系二重积分的两个上下限都是常数时，交换积分顺序后各自上下限不变，类似直角坐标系中的矩形一样
    > * 二重积分凑微分仍然与一重的一样，但是要注意识别 $x,y$ 变量的关系。为了方便凑微分，必要时交换积分顺序或者换元统一变量，甚至像1000题强化04题那样把内层积分给凑了
    > * 直接凑微分凑不出来，尝试对复杂部分求导看看

  * ⭐***08(椭圆极坐标系换元成圆极坐标系)***
  * ***11(轮换对称性、偶倍奇零)***
  * ⭐***12(二次多项式在椭圆区域的积分、椭圆极坐标系换元成圆极坐标系)***
  
    > * 遇到被积函数为 $(x+a)^2+(y+b)^2$ 时，如果区域是圆或椭圆，直接展开，根据偶倍奇零把 $2ax,2by$ 这样的项直接消了，剩下的平方项用极坐标换元直接求就行(圆区域普通极坐标，椭圆区域用椭圆极坐标换元)
    > * **遇到一次项时一定先看看用偶倍奇零能不能消了，不然带着这玩意积起来很麻烦**

  * ***13(提公因式造 $\sin{(\alpha+\beta)}$、$\csc,\cot$ 的导数和积分)***
  
    > 看到 $\sin{\theta}+\cos{\theta}$ 可以尝试提公因式 $\sqrt{2},\,2$ 等，尝试配成 $\sin{(\alpha+\beta)}$

  * 14(交换积分顺序凑微分)
  * ⭐***16(高幂次三角函数降幂、三角函数拆平方)***
  
    > * **遇到高幂次的三角函数如 $\sin^4{(\theta+\dfrac{\pi}{4})}$，可能需要拆成 $\sin^2{(\theta+\dfrac{\pi}{4})}\cdot\sin^2{(\theta+\dfrac{\pi}{4})}$，用降幂公式，或凑微分，对两个平方分别处理；也可能整体换元用点火公式**
    > * **看到高次幂的三角函数的和，提公因式化成一个三角函数的高次幂。如**
    >
    > $$
    > (\sin{\theta}+\cos{\theta})^4=\left[\sqrt{2}(\sin{\theta}\cdot\dfrac{1}{\sqrt{2}}+\cos{\theta}\cdot\dfrac{1}{\sqrt{2}})\right]^4=4\sin^4{\left(\theta+\dfrac{\pi}{4}\right)}
    > $$

  * ⭐***17-18(去绝对值按被积函数正负分割区域、圆平移换元)***
  
    > * 分割区域时，只动区域，不动被积函数
    > * 圆心不在原点的圆可以平移换元，平移换元的 $\lvert\det{J}\rvert=1$

  * 21(带 $\max$ 的函数)
  
    > 把 $\max\{x,y\}$ 转化成 $\lvert x-y\rvert$，因为最大值本质是作差比大小(`jg`指令)，据此分割区域

  * ***22(圆面积)***
  
    > $\displaystyle\int^r_0{\sqrt{r^2-x^2}\mathrm{d}x}=\dfrac{1}{4}\pi r^2$

  * 29(形心)
  * ***33(极坐标系转直角坐标系)***
  
    > 过于复杂的极坐标要转直角坐标系做。因为出现不规则交集区域时，$\theta$ 不是跟圆区域一样切线几乎都是水平竖直的，可能出现斜着的切线，准确定界的风险太高

  * ⭐***36(极坐标盲定界)***
  
    > 区域表达式极其复杂难以绘制时，区域表达式如果带有 $x^2+y^2$ 之类的项，直接转极坐标，在数值上分析 $\theta,r$ 的定界范围

  * ***37(轮换对称性)***
  
    > 轮换对称性是看 **区域** 关于 $y=x$ 对称；而普通对称性是看 **被积函数** 关于 $y=x$ 对称 </br>
    > 轮换对称性是积分相加除二；普通对称性是积分整体是 $0$ 还是 $\times 2$

  * ⭐***39(定积分是数、求抽象函数、两边同时积分)***
  * ***40(二重极限、二重积分中值定理、夹逼准则)***
  * ⭐***41(平方开根号注意正负号、扩展的二重积分中值定理、积分绝对值缩放)***
