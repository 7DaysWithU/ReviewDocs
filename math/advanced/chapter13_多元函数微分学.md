# 多元函数微分学

## 1 知识点

### 1.1 基础概念

* 邻域
  * $\delta$ 邻域

    设 $P_0(x_0,y_0)$ 是 $xOy$ 平面上的一个点，$\delta$ 是某一正数，与 $P_0$ 的距离小于 $\delta$ 的点 $P(x,y)$ 的全体称为点 $P_0$ 的 $\delta$ 邻域，记为 $U(P_0,\delta)$，即
  
    $$
    U(P_0,\delta)
    =\left\{P\Big|\left\lvert PP_0\right\rvert<\delta\right\}
    =\left\{\left(x,y\right)\Big|\sqrt{\left(x-x_0\right)^2+\left(y-y_0\right)^2}<\delta\right\}
    $$

    $U(P_0,\delta)$ 的几何意义为以 $P_0$ 为圆心，$\delta>0$ 为半径的圆内的全体点 $P(x,y)$

  * 去心 $\delta$ 邻域

    点 $P_0$ 的去心 $\delta$ 邻域，记为 $\mathring{U}(P_0,\delta)$，即
  
    $$
    U(P_0,\delta)
    =\left\{P\Big|0<\left\lvert PP_0\right\rvert<\delta\right\}
    =\left\{\left(x,y\right)\Big|0<\sqrt{\left(x-x_0\right)^2+\left(y-y_0\right)^2}<\delta\right\}
    $$

* 极限

  设函数 $f(x,y)$ 在区域 $D$ 上有定义，点 $P_0(x_0,y_0)\in D$ 是区域内火边界上的一点。若对任意给定的 $\epsilon>0$，总存在 $\delta>0$，当点 $P(x,y)\in D$ 且满足 $\left\{P\Big|0<\left\lvert PP_0\right\rvert<\delta\right\}$ 时，恒有
  
  $$
  \left\lvert f(x,y)-A\right\rvert<\epsilon
  $$
  
  则称常数 $A$ 为 $(x,y)\to(x_0,y_0)$ 时 $f(x,y)$ 的极限，记作
  
  $$
  \lim_{(x,y)\to(x_0,y_0)}{f(x,y)}=A或\lim_{\substack{x\to x_0\\ y\to y_0}}{f(x, y)}=A
  $$

  * 证明极限不存在

    证明存在两条不同趋近路径得到的极限值不相同，或存在某一条趋近路劲极限不存在

  * 求极限

    除洛必达法则、单调有界准则外，其余方法仍然适用

* 连续

  若 $\lim\limits_{\substack{x\to x_0\\ y\to y_0}}{f(x, y)}=f(x_0,y_0)$ 则称函数 $f(x,y)$ 在点 $x_0,y_0$ 处连续。若 $f(x,y)$ 在区域 $D$ 上每一点都连续，则称 $f(x,y)$ 在区域 $D$ 上连续。间断点类型同一元函数，对应的邻域从线段变成区域

* 偏导数

  设函数 $f(x,y)$ 在点 $(x_0,y_0)$ 的某邻域内有定义，若极限
  
  $$
  \lim\limits_{x\to x_0}{\dfrac{f(x,y_0)-f(x_0,y_0)}{x-x_0}}
  $$

  存在，则称该极限为函数 $z=f(x,y)$ 在点 $(x_0,y_0)$ 处对 $x$ 的偏导，记作下列中的任意一种
  
  $$
  \left.\dfrac{\partial f}{\partial x}\right|_{\substack{x=x_0\\ y=y_0}},
  \left.\dfrac{\partial z}{\partial x}\right|_{\substack{x=x_0\\ y=y_0}},
  \left.z^{'}_x\right|_{\substack{x=x_0\\ y=y_0}},
  f^{'}_x(x_0,y_0)
  $$
  
  类似的，对 $y$ 的偏导同理

  * 几何意义

    $f^{'}_x(x_0,y_0)$ 表示曲线
    $\begin{cases}
        z=f(x,y),\\
        y=y_0
    \end{cases}$ 在点 $(x_0,y_0,z_0)$ 处的切线对 $x$ 轴的斜率

    $f^{'}_y(x_0,y_0)$ 表示曲线
    $\begin{cases}
        z=f(x,y),\\
        x=x_0
    \end{cases}$ 在点 $(x_0,y_0,z_0)$ 处的切线对 $y$ 轴的斜率

  * 高阶偏导

    如果二元函数 $z=f(x,y)$ 的偏导 $f^{'}_x(x,y)$ 和 $f^{'}_y(x,y)$ 仍然具有偏导，则它们的偏导称为 $f$ 的二阶偏导，记作

    $$
    \begin{align*}
        \dfrac{\partial^2 f}{\partial x^2}=\dfrac{\partial}{\partial x}\left(\dfrac{\partial f}{\partial x}\right)=f^{''}_{xx}(x,y)=z^{''}_{xx},\\\\

        \dfrac{\partial^2 f}{\partial y^2}=\dfrac{\partial}{\partial y}\left(\dfrac{\partial f}{\partial y}\right)=f^{''}_{yy}(x,y)=z^{''}_{yy},\\\\

        \dfrac{\partial^2 f}{\partial x\partial y}=\dfrac{\partial}{\partial y}\left(\dfrac{\partial f}{\partial x}\right)=f^{''}_{xy}(x,y)=z^{''}_{xy},\\\\

        \dfrac{\partial^2 f}{\partial y\partial x}=\dfrac{\partial}{\partial x}\left(\dfrac{\partial f}{\partial y}\right)=f^{''}_{yx}(x,y)=z^{''}_{yx},
    \end{align*}
    $$

    若 $f^{''}_{xy}(x,y),f^{''}_{yx}(x,y)$ 都在区域 $D$ 内连续，则在区域 $D$ 中 $f^{''}_{xy}(x,y)=f^{''}_{yx}(x,y)$，且对 $f$ 的偏导数仍然成立

* 可微

  设函数 $z=f(x,y)$ 在点 $(x,y)$ 的某实心邻域内有定义，若函数在该点的全增量
  
  $$
  \Delta z=f(x+\Delta x,y+\Delta y)-f(x,y)
  $$
  
  可表示为
  
  $$
  \Delta z=A\Delta x+B\Delta y+o(\rho)
  $$
  
  且 $A,B$ 仅与点 $(x,y)$ 有关，与 $\Delta x,\Delta y$ 无关；$\rho=\sqrt{\Delta x^2+\Delta y^2}$；并且当 $\Delta x\to0,\Delta y\to0$ 时 $o(\rho)$ 是 $\sqrt{\Delta x^2+\Delta y^2}$ 的高阶无穷小，则称函数 $z=f(x,y)$ 在点 $(x,y)$ 处可微分，并称 $A\Delta x+B\Delta y$ 为函数 $z=f(x,y)$ 在点 $(x,y)$ 处的 **全微分**，记作
  
  $$
  \mathrm dz=A\Delta x+B\Delta y=A\mathrm dx+B\mathrm dy
  $$
  
  * 可微必要条件

    若函数 $z=f(x,y)$ 在点 $(x,y)$ 处可微分，则该点偏导必然存在，则

    $$
    \begin{align*}
        A=\dfrac{\partial z}{\partial x},B=\dfrac{\partial z}{\partial y}\\\\
        \mathrm dz=\dfrac{\partial z}{\partial x}\mathrm dx+\dfrac{\partial z}{\partial y}\mathrm dy
    \end{align*}
    $$

  * 可微充分条件

    若函数 $z=f(x,y)$ 在点 $(x_0,y_0)$ 处的偏导 **存在且连续**，则函数在该点可微

  * 判断可微

    判断函数 $z=f(x,y)$ 在点 $(x_0,y_0)$ 处是否可微

    * 求全增量 $\Delta z=f(x_0+\Delta x,y_0+\Delta y)-f(x_0,y_0)$
    * 求线性增量 $A\Delta x+B\Delta y$，其中 $A=f^{'}_x(x_0,y_0),B=f^{'}_y(x_0,y_0)$
    * 求极限 $\lim\limits_{\substack{\Delta x\to0\\ \Delta y\to0}}{\dfrac{\Delta z-(A\Delta x+B\Delta y)}{\sqrt{\Delta x^2+\Delta y^2}}}$。若极限为 $0$，则在点 $(x_0,y_0)$ 处可微，否则不可微

### 1.2 多元函数微分法则

* 链式求导法则
  * 多元复合函数
  
    设 $z=f(u,v)\,,u=\phi(x,y)\,,v=\psi(x,y)$，即 $z=f\left[\phi(x,y)\,,\psi(x,y)\right]$，则
  
    $$
    \begin{align*}
      \dfrac{\partial z}{\partial x}=\dfrac{\partial z}{\partial u}\cdot\dfrac{\partial u}{\partial x}+\dfrac{\partial z}{\partial v}\cdot\dfrac{\partial v}{\partial x}\\\\

      \dfrac{\partial z}{\partial y}=\dfrac{\partial z}{\partial u}\cdot\dfrac{\partial u}{\partial y}+\dfrac{\partial z}{\partial v}\cdot\dfrac{\partial v}{\partial y}
    \end{align*}
    $$

    ***无论求几阶导，$f^{(n)}_x(u,v)\,,f^{(n)}_y(u,v)$ 始终是 $u,v$ 的函数，对导数再求导依然遵守上边的公式***

  * 一元复合函数
  
    设 $z=f(u,v)\,,u=\phi(t)\,,v=\psi(t)$，即 $z=f\left[\phi(t)\,,\psi(t)\right]$，则
  
    $$
    \dfrac{\partial z}{\partial t}=\dfrac{\partial z}{\partial u}\cdot\dfrac{\partial u}{\partial t}+\dfrac{\partial z}{\partial v}\cdot\dfrac{\partial v}{\partial t}
    $$

* 全微分形式不变性

  设 $z=f(u,v)\,,u=u(x,y)\,,v=v(x,y)$，若三者分别有 **连续偏导**，则复合函数 $z=f(u,v)$ 在 $(x,y)$ 处的全微分可表示为
  
  $$
  \mathrm{d}z=\dfrac{\partial z}{\partial u}\mathrm{d}u+\dfrac{\partial z}{\partial v}\mathrm{d}v
  $$
  
* 隐函数存在定理
  * 二元隐函数存在定理

    设 $F(x,y)$ 在点 $(x_0,y_0)$ 的某邻域内有连续的偏导数，且
    $
    \begin{cases}
      F(x_0,y_0)=0\\
      F^{'}_y(x_0,y_0)\neq0
    \end{cases}
    $
    ，则存在确定的隐函数 $y=f(x)$。同时有

    $$
    \dfrac{\mathrm{d}y}{\mathrm{d}x}=-\dfrac{F^{'}_x(x,y)}{F^{'}_y(x,y)}\,,
    $$

    * 若 $F$ 对某个变量的一阶偏导不为 $0$，则该变量可以表示为另外一个变量的函数，且求导公式对应成立
    * 为充分非必要条件。即使 $F^{'}_y(x_0,y_0)=0$，若 $F^{'}_x(x,y)$ 是 $F^{'}_y(x_0,y_0)$ 的同阶或高阶无穷小，则 $\dfrac{\mathrm{d}y}{\mathrm{d}x}$ 仍然存在

  * 三元隐函数存在定理

    设 $F(x,y,z)$ 在点 $(x_0,y_0,z_0)$ 的某邻域内有连续的偏导数，且
    $
    \begin{cases}
      F(x_0,y_0,z_0)=0\\
      F^{'}_z(x_0,y_0,z_0)\neq0
    \end{cases}
    $
    ，则存在确定的隐函数 $z=f(x,y)$。同时有

    $$
    \dfrac{\partial z}{\partial x}=-\dfrac{F^{'}_x(x,y,z)}{F^{'}_z(x,y,z)}\,,
    \dfrac{\partial z}{\partial y}=-\dfrac{F^{'}_y(x,y,z)}{F^{'}_z(x,y,z)}
    $$

    * 若 $F$ 对某个变量的一阶偏导不为 $0$，则该变量可以表示为另外两个变量的函数，且求导公式对应成立
    * 为充分非必要条件。例如 $F^{'}_z(x_0,y_0)=0$，若 $F^{'}_x(x,y,z)$ 是 $F^{'}_z(x,y,z)$ 的同阶或高阶无穷小，则 $\dfrac{\partial z}{\partial x}$ 仍然存在

  * **⭐️⭐️⭐️经典题型**

    > 基础30讲课后习题13.9</br>
    > 设 $z=z(x,y)$ 由 $(z+y)^x=x^2$ 确定，求 $\left.\dfrac{\partial z}{\partial x}\right|_{(1,1)}$</br>
    > 即“设 $[隐函数]$ 由 $[方程]$ 给出，求 $[偏导]$”

    * 公式法

      令 $F(x,y,z)=(z+y)^x-x^2$。此时，***$x,y,z$ 是各自独立的三个变量***，根据隐函数存在定理求偏导时另外两个变量相当于 $C$

    * 两边求导法

      直接两边求全微分 $\left[(z+y)^x\right]^{'}=\left[x^2\right]^{'}$，即 $\left[\left(z\left(x,y\right)+y\right)^x\right]^{'}=\left[x^2\right]^{'}$。此时，自变量是 $x,y$，因变量是 $z$，因此等式左边是个幂指函数求导

    * 总结

      公式法是将隐函数嵌入回去，将两个变量变成三个变量，更方便求偏导。两边求导法是将隐函数作为因变量，对 $x$ 求偏导时如果遇到 $z$ 则会产生 $\dfrac{\partial z}{\partial x}$

* 二元拉格朗日定理

  设 $f(x,y)$ 定义在区域 $D$ 上，且 $\dfrac{\partial f}{\partial x}=0\,,\dfrac{\partial f}{\partial y}=0\,,(x,y)\in D$ ，则 $f(x,y)=C\,,(x,y)\in D$

### 1.3 多元函数极值与最值

* 定义
  * 极值

    若存在点 $(x_0,y_0)$ 的某个邻域，使邻域内任意一点 $(x,y)$ 均有
  
    $$
    f(x_0,y_0)\geq f(x,y)\,\left(或f(x_0,y_0)\leq f(x,y)\right)
    $$
  
    则称点 $(x_0,y_0)$ 为 $f(x,y)$ 的极大值点(或极小值点)

    **极值点不要求在该点连续或可微(尖锥)**

  * 最值

    设点 $(x_0,y_0)$ 为 $f(x,y)$ 定义域内的一个点，且对于定义域内任意一点 $(x,y)$ 均有
  
    $$
    f(x_0,y_0)\geq f(x,y)\,\left(或f(x_0,y_0)\leq f(x,y)\right)
    $$
  
    则称点 $(x_0,y_0)$ 为 $f(x,y)$ 的最大值点(或最小值点)

* 无条件极值
  * 二元函数求极值的必要条件

    设 $z=f(x,y)$ 在点 $(x_0,y_0)$ 处 $\begin{cases}一阶偏导存在\\取极值\end{cases}$，则 $\begin{cases}f^{'}_{x}(x_0,y_0)=0\\f^{'}_{y}(x_0,y_0)=0\end{cases}$

    若 $z=f(x,y)$ 在点 $(x_0,y_0)$ 处 $\begin{cases}二阶偏导存在\\取极大值\end{cases}$，则 $\begin{cases}f^{''}_{xx}(x_0,y_0)\leq0\\f^{''}_{yy}(x_0,y_0)\leq0\end{cases}$

  * 二元函数求极值的充分条件

    记

    $$
    \begin{cases}
      f^{''}_{xx}(x_0,y_0)=A\\
      f^{''}_{xy}(x_0,y_0)=B\\
      f^{''}_{yy}(x_0,y_0)=C
    \end{cases}
    $$

    则

    $$
    \Delta=AC-B^2
    \begin{cases}
      >0\Rightarrow\text{是极值}
      \begin{cases}
        A<0,C<0\Rightarrow\text{极大值}\\
        A>0,C>0\Rightarrow\text{极小值}
      \end{cases}\\
      <0\Rightarrow\text{不是极值}\\
      =0\Rightarrow\text{方法失效}
    \end{cases}
    $$

    **$\Delta>0$ 时可知 $A,C$ 同号，因此知道二者中一个的正负就可以了**

  * 判断极值点

    先找可疑点
    $
    \begin{cases}
      f^{'}_{x}(x_0,y_0)=0\,,f^{'}_{y}(x_0,y_0)=0\\
      不可导点
    \end{cases}
    $,
    再判别可疑点处的 $\Delta$ 确定具体极值点情况

    **大鼻子爷爷👴与小哑巴猪🐷，开不开心少年团😊😢**

    > **当 $\Delta=0$ 方法失效时，依据以下原理，通过选取单个方向降维来判断是否为多元函数的极值点**</br>
    > 若二元函数的极值点为 $(x_0,y_0)$，则 $x$ 方向上的 $(x,y_0)$ 、$y$ 方向上的 $(x_0,y)$ 都是极值点</br>
    > 若在 $x$ 方向上的 $(x,y_0)$ 、$y$ 方向上的 $(x_0,y)$ 均为极值点，则点 $(x_0,y_0)$ 不一定是二元函数的极值点</br>
    > 若 $x$ 方向上的 $(x,y_0)$ 、$y$ 方向上的 $(x_0,y)$ 其中一个不是极值点，则点 $(x_0,y_0)$ 不可能是二元函数的极值点

* 条件最值(拉格朗日乘数法)

  求目标函数 $u=f(x,y,z)$ 在约束条件
  $
  \begin{cases}
    \phi(x,y,z)=0\\
    \psi(x,y,z)=0
  \end{cases}
  $
  下的最值，需

  1. 构造辅助函数 $F(x,y,z,\lambda,\mu)=f(x,y,z)+\lambda\phi(x,y,z)+\mu\psi(x,y,z)$
  2. 令

      $$
      \begin{cases}
        F^{'}_x=f^{'}_x+\lambda\phi^{'}_x+\mu\psi^{'}_x=0\\
        F^{'}_y=f^{'}_y+\lambda\phi^{'}_y+\mu\psi^{'}_y=0\\
        F^{'}_z=f^{'}_z+\lambda\phi^{'}_z+\mu\psi^{'}_z=0\\
        F^{'}_\lambda=\phi(x,y,z)=0\\
        F^{'}_\mu=\psi(x,y,z)=0
      \end{cases}
      $$

  3. 解方程得到备选点，将备选点带入目标函数 $u=f(x,y,z)$ 求得最值

  **有几个约束就要再辅助函数后增加几项，每个约束使用不同的系数。二元函数同理**

  **若约束条件很简单，可以直接反解变量带入回目标函数，降维处理(如1000题25：二元约束求极值 $\to$ 一元二次函数求极值)**

* 最远(近)点垂线原理

  1. 若 $\Gamma$ 是光滑闭曲线，点 $Q$ 是 $\Gamma$ 外的一点，点 $P_1,P_2$ 分别是 $\Gamma$ 上与 $Q$ 的最远点、最近点。则直线 $P_1Q,P_2Q$ 分别在点 $P_1,P_2$ 处与 $\Gamma$ 垂直，即 $P_1Q,P_2Q$ 分别与点 $P_1,P_2$ 的切线垂直
  2. 若光滑闭曲线 $\Gamma_1,\Gamma_2$ 不相交，点 $P_1,P_2$ 分别是它们之间的最远(近)点。则直线 $P_1P_2$ 是 $\Gamma_1,\Gamma_2$ 的公垂线，即 $P_1P_2$ 同时垂直于 $\Gamma_1,\Gamma_2$ 在这两个点处的切线

  **部分情况下使用拉格朗日乘数法较为复杂，可简化为空间中的最远(近)问题，配合隐函数存在定理得到斜率，根据斜率求解坐标**

* 有界闭区间上的最值问题

  1. 根据
    $
    \begin{cases}
      f^{'}_x=0\\
      f^{'}_y=0
    \end{cases}
    $
    或二者都不存在，找到 **区域 $D$ 内** 的可疑点
  2. 使用拉格朗日乘数法或带入消元法找到 **区域 $D$ 边界上** 的可疑点
  3. 比较所有可疑点的函数值，确定最值

  **类比一元函数，需要求区间内与区间端点的函数值进行比较，二元函数的区间端点为区域边界**

## 2 进阶

### 2.1 计算二元函数极限 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

$$
\begin{align*}
  二重极限：&\lim\limits_{\substack{x\to x_0 \\ y\to y_0}}{f(x,y)} \\
  累次极限：&\lim\limits_{x\to x_0}{\lim\limits_{y\to y_0}{f(x,y)}},\quad\lim\limits_{x\to x_0}{\lim\limits_{y\to y_0}{f(x,y)}}
\end{align*}
$$

* 判别二重极限是否存在 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{22} (转换等价表述)}$
  * 同阶路径法：令 $y=kx$，常用于 $x,y$ 同阶的情况。如 $x+y\xlongequal{令y=kx}x(1+k)$
  * 变阶路径法：通过去掉一阶，补上另一阶凑齐，常用于 $x,y$ 不同阶的情况。如

    $$
    x+y
    \begin{cases}
      \xlongequal{令y=-x+x^2}x^2,&升阶 \\
      \xlongequal{令y=-x+\sqrt{x}}\sqrt{x},& 降阶 \\
    \end{cases}\\

    x^2+y\xlongequal{令y=x^2}2x^2,同阶
    $$

* 计算二重极限 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{22} (转换等价表述)}$
  * 夹逼准则：利用放缩法(套绝对值用绝对值不等式、裂项)、凑平方等手段直接夹逼出极限
  * 无穷小乘有界是无穷小：可以通过凑项把原本复杂的式子凑成一些无穷小乘有界，就能得到结果
  * 整体换元法：变成一元极限。如换元成极坐标，将 $\lim\limits_{\substack{x\to x_0 \\ y\to y_0}}{f(x,y)}\Rightarrow\lim\limits_{r\to r_0}{r(\theta)}$，不指定 $\theta$ 的趋向是为了确保所有路径的极限一致，即保证极限存在

* 判别累次极限是否存在 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作)}$

  里边的极限不存在，整体就不存在；必须两个极限都存在，累次极限才存在

* 二重极限和累次极限关系 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作)}$
  * 二重极限存在性与累次极限存在性没关系
  * 若二重极限和累次极限都存在，则二者必定相等
  * 两个累次极限都存在，但先 $x$ 后 $y$ 和先 $y$ 后 $x$ 不相等，则二重极限不存在

### 2.2 二元函数性质 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

* 连续、偏导数、全微分、连续 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作)}$
  * $f(x,y)$ 在 $(x_0,y_0)$ 处连续则在该点单变量也连续，反之未必
  * 关系

### 2.3 计算偏导和全微分 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

* 链式求导法则 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作)}$
  
  **遇到求二阶导时一定先求对应位置的导，再求该位置的对具体变量的导**

  * 一元复合函数 $f[g(x)]$ 求导
  * 二元多变量复合函数 $f(u,v)$ 求导，其中 $u=u(x,y),v=v(x,y)$
  * 二元单变量复合函数 $f(u,v)$ 求导，其中 $u=u(t),v=v(t)$

* 隐函数求导法 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作)}$
  * 单方程：隐函数存在定理
  
    $F(x,y,z)$ 在点 $(x_0,y_0,z_0)$ 的某邻域内有连续的偏导数，且
    $
    \begin{cases}
      F(x_0,y_0,z_0)=0\\
      F^{'}_z(x_0,y_0,z_0)\neq0
    \end{cases}
    $
    ，则

    $$
    \dfrac{\partial z}{\partial x}=-\dfrac{F^{'}_x(x,y,z)}{F^{'}_z(x,y,z)}\,,
    \dfrac{\partial z}{\partial y}=-\dfrac{F^{'}_y(x,y,z)}{F^{'}_z(x,y,z)}
    $$

  * 方程组：雅可比行列式

    设
    $
    \begin{cases}
      F(x, y, z) &= 0 \\
      G(x, y, z) &= 0
    \end{cases}$
    ，当满足
    $
    \dfrac{\partial(F,G)}{\partial(y,z)} =
    \begin{vmatrix}
      \dfrac{\partial F}{\partial y} & \dfrac{\partial F}{\partial z} \\\\
      \dfrac{\partial G}{\partial y} & \dfrac{\partial G}{\partial z}
    \end{vmatrix}
    \neq 0
    $时，可确定
    $
    \begin{cases}
      y &= y(x) \\
      z &= z(x)
    \end{cases}
    $

    且有

    $$
    \dfrac{dy}{dx} = -\dfrac{\dfrac{\partial(F,G)}{\partial(x,z)}}{\dfrac{\partial(F,G)}{\partial(y,z)}}
    = -\dfrac{
    \begin{vmatrix}
      \dfrac{\partial F}{\partial x} & \dfrac{\partial F}{\partial z} \\\\
      \dfrac{\partial G}{\partial x} & \dfrac{\partial G}{\partial z}
    \end{vmatrix}
    }{
    \begin{vmatrix}
      \dfrac{\partial F}{\partial y} & \dfrac{\partial F}{\partial z} \\\\
      \dfrac{\partial G}{\partial y} & \dfrac{\partial G}{\partial z}
    \end{vmatrix}
    },
    \quad
    \dfrac{dz}{dx} = -\dfrac{\dfrac{\partial(F,G)}{\partial(y,x)}}{\dfrac{\partial(F,G)}{\partial(y,z)}}
    = -\dfrac{
    \begin{vmatrix}
      \dfrac{\partial F}{\partial y} & \dfrac{\partial F}{\partial x} \\\\
      \dfrac{\partial G}{\partial y} & \dfrac{\partial G}{\partial x}
    \end{vmatrix}
    }{
    \begin{vmatrix}
      \dfrac{\partial F}{\partial y} & \dfrac{\partial F}{\partial z} \\\\
      \dfrac{\partial G}{\partial y} & \dfrac{\partial G}{\partial z}
    \end{vmatrix}
    }.
    $$

* 全微分不变性、全微分公式大观 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作)}$

### 2.4 偏微分方程 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

* 已知偏导方程求原函数 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式) + \text{D}_\text{3} (移花接木)}$

  找到 $u,v$，令 $f=f(u,v)$，画结构图，求偏导并带入题目中的偏导方程进行化简，得到纯的一阶偏导或二阶混合偏导，再往回积分即可获得 $f$。特别注意，积分产生的"常数"实质上是另一个变量的函数，如 $\dfrac{\partial^2{f}}{\partial{x}\partial{y}}$ 对 $y$ 积分产生的是 $C(x)$

* 化简偏微分方程 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式) + \text{D}_\text{3} (移花接木)}$

  画结构图，求偏导并带入题目中的偏导方程进行化简，通过比对系数解出题目给的偏导方程中的未知数

* 已知关于偏导的复合函数求原函数 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式) + \text{D}_\text{3} (移花接木)}$

  如题目给出的是 $u=f[g(x)]$ 满足含 $u$ 的偏导方程，则令 $g(x)=t$，画结构图，求偏导并带入题目中的偏导方程进行化简，最后积分求原函数，仍然注意"常数"的问题

* 已知偏导与原函数关系求原函数 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式) + \text{D}_\text{3} (移花接木)}$

  如题目给出的是 $f^{'}(x,y)=-f(x,y)$，则可以化简成 $\dfrac{f^{'}(x,y)}{f(x,y)}=-1$，类似凑微分。两边同时对 $x$ 积分得 $\ln{\lvert f(x,y)\rvert}=-x+C(y)$。通过其他取值条件定下来 $C(y)$ 等"常数"

### 2.5 多元函数的极值最值 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

* 无条件极值 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{22} (转换等价表述) + \text{D}_\text{3} (移花接木)}$
  * 求解方法：一阶偏导为 $0$、二阶偏导判断 $\Delta$
  * $\Delta=0$ 时的否定极值方法
    * 沿 $x$ 方向是极小，沿 $y$ 方向是极大，即马鞍面
    * 沿 $y=kx$ 有极大也有极小
    * 邻域内有极大也有极小
  * 与一元函数区别
    * 多元函数唯一的极值点不一定是最值点；一元函数唯一极值点必是最值点
    * 多元函数可以有多个极值点，也可以只有多个极大值没有极小值；一元函数的两个极值点必定一个极大值一个极小值
  * 利用 $\Delta$ 判别极值点位置：若 $\Delta<0$，则区域内部一定没有极值点

* 条件极值、拉格朗日乘数法 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{22} (转换等价表述)}$
  * 可以利用 $k$ 次齐次函数优化乘数法方程组，方便求解
  * 在可微的条件下，条件极值点满足

    $$
    \left.\begin{vmatrix}
      f^{'}_x & f^{'}_y & f^{'}_z \\
      \phi^{'}_x & \phi^{'}_y & \phi^{'}_z \\
      \psi^{'}_x & \psi^{'}_y & \psi^{'}_z \\
    \end{vmatrix}\right|_{P_0}
    =0
    $$

* 闭区域上的最值 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作)}$

  区域内用无条件极值求候选点，区域边界上用拉格朗日乘数法或带入消元法求候选点，最后比较所有候选点的函数值大小

## 3 题目

* 基础30讲
  * 例13.1(极限存在)
  * 例13.2(求极限)
  * 例13.3(定义法求单点偏导)
  * 例13.4(公式法求区域偏导、高阶偏导)
  * ***例13.5(不可拆分变限积分求导、换元、最佳带值求导顺序、$\Gamma$ 函数)***
  * ***例13.6(偏导回积、恒等变形、微分方程)***
  * 例13.7(二阶混合偏导连续时相等)
  * 例13.8(判断可微)
  * ***例13.9(复合函数二阶混合偏导)***
  * 例13.10(链式求导法则)
  * 例13.11(链式求导法则)
  * 例13.12(全微分形式不变性、隐函数求导)
  * 例13.13(隐函数存在定理)
  * 例13.14(完整的隐函数存在定理)
  * 例13.15(隐函数存在定理)
  * ***例13.16(2元变3元、隐函数存在定理)***
  * 例13.17(二元极值与一元极值关系)
  * ***例13.18(极值点的二阶偏导)***
  * ***例13.19(求极值)***
  * ***例13.20(条件最值)***
  * 例13.21(最近距离)
  * ***例13.22(区域最值、全微分形式不变性、拉格朗日乘数法、椭圆)***
* 基础30讲课后习题
  * 13.1(极限存在)
  * 13.3(判断可微)
  * 13.4(链式求导法则)
  * ***13.9(隐函数公式法、两边求导法、自变量因变量)***
  * ***13.10(链式求导法则计算)***
  * ***13.11(单变量复合函数求导、两边求导法)***
  * ***13.13(多元函数积分、求极值)***
  * ***13.14(最值、计算化简)***
* 1000题基础
  * 06(换元法、积分法)
  * ***08(换元法)***
  * 09(分段函数求导)
  * 10(定义域)
  * ***13(多元复合函数求偏导计算)***
  * 16(变量代换)
  * 17(等式化简)
  * 19(二阶导、最值、极值)
  * 21(均值不等式、二元区域求最值、三元拉格朗日乘数法求最值)
  * ***27(偏导回积、极值判别第三充分条件)***
* 强化36讲
  * 例13.1(判断二重极限存在、同阶路径法)
  * 例13.2(判断二重极限存在、变阶路径法)
  * ***例13.3(计算二重极限、夹逼准则)***
  * 例13.4(计算二重极限、无穷小乘有界)
  * 例13.5(判断累次极限存在)
  * 例13.6(判断累次极限存在、二重极限和累次极限关系)
  * 例13.7(判断变量连续与函数连续)
  * ***例13.8(判断连续与偏导存在)***
  * 例13.9(判断连续与偏导存在)
  * ***例13.10(判断函数连续与可微)***
  * ⭐***例13.11(判断函数连续与微分、偏导数连续)***
  * ⭐***例13.12(判断可微与偏导连续)***
  * ***例13.13(带值求二阶混合偏导)***
  * 例13.14(连续函数的二阶混合偏导相等)
  * ⭐***例13.15(方程隐函数求全微分)***
  
    > 求快就两边同时求全微分再化简，求稳就公式法用隐函数存在定理

  * ⭐***例13.16(二元函数求混合二阶偏导)***
  
    > 对于 $f(u,v)$ 一定是先求对第一个位置的偏导，再求第一个位置相关变量的偏导，第二个位置也是一样
    >
    > **若一阶偏导是 $0$，则二阶偏导未必是 $0$**
  
  * ***例13.17(雅可比行列式、观察法解方程)***
  * 例13.18($k$ 次齐次函数充要条件证明)
  
    > **$f(x,y)$ 是 $k$ 次齐次函数 $f(tx,ty)=t^k f(x,y)\Leftrightarrow x\dfrac{\partial{f}}{\partial{x}}+y\dfrac{\partial{f}}{\partial{y}}=k f(x,y)$**

  * ***例13.19($k$ 次齐次函数)***
  * ⛔***例13.20($k$ 次齐次函数)***
  * ⭐***例13.21(已知偏导方程求原函数)***
  
    > 可以利用二阶混合偏导相等的性质交换积分先后。**特别注意对一个变量积分得到的"常数"是关于其他变量的表达式**，需要用题目中的表达式带值确认

  * ⭐***例13.22(化简偏微分方程)***
  * ⭐***例13.23(已知关于偏导的复合函数求原函数)***
  * ⭐***例13.24(已知偏导与原函数关系求原函数)***
  * 例13.25(无条件极值)
  * ***例13.26(无条件极值否定判断)***
  * 例13.27($\Delta$ 判别法判断最值在区域内还是边界上)
  * 例13.28($\Delta$ 判别法判断抽象函数取极值的充分条件)
  * ⛔***例13.29(条件极值点偏导行列式)***
  * ***例13.30(条件最值、$k$ 次齐次函数优化乘数法方程组、齐次线性方程组 $\det=0$ 是唯一零解)***
  * 例13.31(区域最值)
* 1000题强化
  * ⭐***02(求点的二阶复合偏导值、求分段函数的累次极限)***
  
    > 求点的二阶复合偏导值，则需要先固定一个变量($\neq 0$)并求出一阶偏导的表达式，再走导数定义求二阶偏导
    >
    > 若要求 $x\to 0$，则一定有 $x\neq 0$，据此选择分段函数符合 $x\neq 0$ 的部分

  * ***03(即使偏导都是0也要先证明可微才能求全微分、夹逼放缩证明可微)***
  * ***04(极限存在母为0子必为0)***
  * ⭐***05(极坐标换元求二重极限、判断二重极限存在)***
