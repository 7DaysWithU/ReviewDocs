# 微分方程

## 1 知识点

### 1.1 概念

* 微分方程及其阶

  表示未知函数及其导数(或者微分)与自变量之间关系的方程称为微分方程，一般写成

  $$
  F[x,y,y',\cdots,y^{(n)}]=0\,或\,
  y^{(n)}=f[x,y,y',\cdots,y^{(n-1)}]
  $$

  其中，微分方程中未知函数的最高阶导数的阶数称为微分方程的阶

  **微分方程研究对象是函数 $y$，最终求出 $y=y(x)$。如 $y^{'''}-y^{''}+6y=0$ 就是三阶微分方程**

* 常微分方程

  未知函数是一元函数的微分方程称为常微分方程。如 $y^{'''}-y^{''}+6y=0\,,y\mathrm{d}x-(x+\sqrt{x^2+y^2})\mathrm{d}y=0$

* 线性微分方程

  形如 $a_n(x)y^{(n)}+a_{n-1}(x)y^{(n-1)}+\cdots+a_1(x)y^{'}+a_0(x)y=f(x)$ 的微分方程称为 **$n$ 阶线性微分方程**，其中 $a_k(x)(k=0,1,2,\cdots,n)$ 都是自变量 $x$ 的函数，$a_n(x)\neq0$。当 $a_k(x)(k=0,1,2,\cdots,n)$ 都是常数时，又称方程为 **$n$ 阶常系数线性微分方程**。若右端函数 $f(x)$ 恒为零，则称方程为 **$n$ 阶齐次线性微分方程**，否则称其为 **$n$ 阶非齐次线性微分方程**

* 微分方程的解

  若将函数代入微分方程，使方程成为恒等式，则该函数称为微分方程的解。微分方程解的图形称为积分曲线

* 微分方程的通解

  若微分方程的解中含有的独立常数的个数等于微分方程的阶数，则该解称为微分方程的通解

  * 此处的常数并非一定是任意常数，可能是在一定范围内取值的常数，如例15.4
  * 经任何恒等变换都不能使常数个数减少，如 $y=e^x(C_1+C_2x)$。但 $y=C_1\sin{x}+C_2\cdot2\sin{x}=(C_1+2C_2)\sin{x}=C\sin{x}$，这里的 $C_1,C_2$ 就不独立。

* 初始条件与特解

  确定通解中常数的条件就是初始条件。如 $y(x_0)=a_0\,,y^{'}(x_0)=a_1\,,\cdots\,,y^{(n-1)}(x_0)=a_{n-1}$，其中 $a_0\,,a_1\,,\cdots\,,a_{n-1}$ 为 $n$ 个给定的数。确定了通解中的常数后，解就成了特解。

### 1.2 一阶微分方程求解

* 可分离变量型微分方程
  * 直接分离

    $$
    \dfrac{\mathrm{d}y}{\mathrm{d}x}=f(x)g(y)\Rightarrow
    \int{\dfrac{\mathrm{d}y}{g(y)}}=\int{f(x)\mathrm{d}x}\,,g(y)\neq0
    $$

  * 换元分离

    $$
    \begin{align*}
      \dfrac{\mathrm{d}y}{\mathrm{d}x}=&f(ax+by+c)
      \xRightarrow{令u=ax+by+c}\dfrac{\mathrm{d}u}{\mathrm{d}x}=a+b\dfrac{\mathrm{d}y}{\mathrm{d}x}=a+bf(u)\\\\
      \Rightarrow&\int{\dfrac{\mathrm{d}u}{a+bf(u)}}=\int{1\cdot\mathrm{d}x}\,,a+bf(u)\neq0
    \end{align*}
    $$

  分离法均会导致损失一部分通解，可以去掉约束条件验证这一部分丢失的通解是否成立

* 齐次型微分方程
  * $y^{'}=f(\dfrac{y}{x})$ 型

    $$
    \begin{align*}
      \dfrac{\mathrm{d}y}{\mathrm{d}x}=&\phi(\dfrac{y}{x})
      \xRightarrow{令u=\dfrac{y}{x},则y=ux}\dfrac{\mathrm{d}y}{\mathrm{d}x}=\dfrac{\mathrm{d}u}{\mathrm{d}x}\cdot x+u=\phi(u)\\\\
      \Rightarrow&\int{\dfrac{\mathrm{d}u}{\phi(u)-u}}=\int{\dfrac{\mathrm{d}x}{x}}
    \end{align*}
    $$

  * $\dfrac{1}{y^{'}}=f(\dfrac{x}{y})$ 型

    $$
    \begin{align*}
      \dfrac{\mathrm{d}x}{\mathrm{d}y}=&\phi(\dfrac{x}{y})
      \xRightarrow{令u=\dfrac{x}{y},则x=uy}\dfrac{\mathrm{d}x}{\mathrm{d}y}=\dfrac{\mathrm{d}u}{\mathrm{d}y}\cdot y+u=\phi(u)\\\\
      \Rightarrow&\int{\dfrac{\mathrm{d}u}{\phi(u)-u}}=\int{\dfrac{\mathrm{d}y}{y}}
    \end{align*}
    $$

  * $y^{'}=f\left(\dfrac{ax+by+c}{a_1 x+b_1 y+c_1}\right)$ 型
    * 当 $c^2+c^2_1=0$ 时

      令 $y^{'}=f\left(\dfrac{ax+by}{a_1 x+b_1 y}\right)=g\left(\dfrac{y}{x}\right)$，分式上下 同时除 $x$，变成 $\dfrac{a+b\cdot\dfrac{y}{x}}{a_1+b_1\cdot\dfrac{y}{x}}=g\left(\dfrac{y}{x}\right)$

    * 当 $c^2+c^2_1\neq 0,\dfrac{a}{a_1}=\dfrac{b}{b_1}$ 时

      令 $y^{'}=f\left(\dfrac{ax+by+c}{a_1 x+b_1 y+c_1}\right)=g\left(ax+by\right)$，分式上下通过配出相同的比例系数，将分式拆成一个常数与一个简单分式

    * 当 $c^2+c^2_1\neq 0,\dfrac{a}{a_1}\neq\dfrac{b}{b_1}$ 时

      令 $y^{'}=f\left(\dfrac{ax+by}{a_1 x+b_1 y}\right)=f\left(\dfrac{aX+bY}{a_1 X+b_1 Y}\right)$，其中由 $\begin{cases}ax+by+c=0 \\ a_1 x+b_1 y+c_1=0\end{cases}$ 解得 $x_0,y_0$，再令 $\begin{cases}x=X+x_0 \\ y=Y+y_0\end{cases}$。相当于坐标系平移

    **通过这三种方法化简分式后再通过分离变量或换元进行求解**

* 一阶线性微分方程

  若 $p(x)\,,q(x)$ 连续，则一阶线性微分方程 $y^{'}+p(x)y=q(x)$ 的通解公式为
  
  $$
  y=e^{-\int{p(x)\mathrm{d}x}}\left[\int{e^{\int{p(x)\mathrm{d}x}}q(x)\mathrm{d}x}+C\right]
  $$

  **⚠️特别地，通解公式可以写作变限积分形式，便于进行有关函数分析的操作(极限、有界等)**
  
  $$
  y=e^{-\int^x_{x_0}{p(t)\mathrm{d}t}}\left[\int^x_{x_0}{e^{\int^t_{x_0}{p(u)\mathrm{d}u}}q(t)\mathrm{d}t}+C\right]
  $$

  * $e$ 的积分求的是**一个**原函数，而非**全体**原函数，不用加常数
  * 当 $\int{p(x)\mathrm{d}x}=\ln{\left\lvert\phi(x)\right\rvert}$ 时，通解公式中可以不带绝对值，因为两个 $e$ 的积分相乘必定是同号，正负无所谓了
  
* 二阶可降阶微分方程
  * 不带 $y$ 型： $y^{''}=f(x,y^{'})$

    令 $y^{'}=p(x)$，则 $y^{''}=p^{'}(x)$，原方程变为 $p$ 与 $x$ 的一阶方程 $\dfrac{\mathrm{d}p}{\mathrm{d}x}=f(x,p)$，作变量分离再同时积分得到 $y^{'}=p(x)$ 表达式，再根据初始条件获得常数并积分得到 $y$

    **既不带 $y$ 也不带 $x$ 按不带 $y$ 处理**

  * 不带 $x$ 型： $y^{''}=f(y,y^{'})$

    令 $y^{'}=p(y)$，则 $y^{''}=\dfrac{\mathrm{d}p}{\mathrm{d}x}=\dfrac{\mathrm{d}p}{\mathrm{d}y}\cdot\dfrac{\mathrm{d}y}{\mathrm{d}x}=\dfrac{\mathrm{d}p}{\mathrm{d}y}\cdot p$。则原方程变为 $p$ 与 $y$ 的一阶方程 $\dfrac{\mathrm{d}p}{\mathrm{d}y}\cdot p=f(y,p)$，作变量分离再同时积分得到 $\dfrac{\mathrm{d}y}{\mathrm{d}x}=p=\phi(y,C_1)$ 表达式，再根据初始条件获得常数并积分得到 $y$。**带值时按 $p[y(x)]$ 带，因为 $p$ 是关于 $y$ 的函数，$y$ 才是关于 $x$ 的函数**

### 1.3 高阶线性微分方程求解

* 二阶常系数齐次线性微分方程

  对于方程 $y^{''}+py^{'}+qy=0$，其中 $p,q$ 为常数，方程的特征方程为 $r^2+pr+q=0$。则方程的通解为
  
  $$
  \begin{align*}
    \Delta=p^2-4q
    \begin{cases}
      >0,&y=C_1e^{r_1x}+C_2e^{r_2x}\\
      =0,&y=e^{rx}(C_1+C_2x)\\
      <0,&y=e^{\alpha x}(C_1\cos{\beta x}+C_2\sin{\beta x})
    \end{cases}
  \end{align*}
  $$

  其中，$r_1,r_2$ 为特征方程的解；$r$ 为特征方程重根情况下的解；$\alpha,\beta$ 为特征方程解为复数 $\alpha\pm\beta i$ 时的实部和虚部

* 二阶常系数非齐次线性微分方程

  对于方程 $y^{''}+py^{'}+qy=f(x)\,,f(x)\not\equiv0$，其中 $p,q$ 为常数，方程的特征方程为 $r^2+pr+q=0$。则方程的通解为
  
  $$
  y(x)+y^*(x)
  $$
  
  其中，$y(x)$ 为方程 $y^{''}+py^{'}+qy=0$ 的通解，$y^*(x)$ 为二阶常系数非齐次方程的特解，特解可由两种方法得到。其中，待定系数法在设出 $y^*$ 后需要将特解带回方程求解系数，微分算子法直接求解设出的 $y^*$ 即可。特别地，有
  > 1.方程 $y^{''}+py^{'}+qy=f_1(x)+f_2(x)$ 的特解为 $y^{''}+py^{'}+qy=f_1(x)$ 的特解加 $y^{''}+py^{'}+qy=f_2(x)$ 的特解
  >
  > 2.方程 $y^{''}+py^{'}+qy=f(x)$ 的通解为 $y^{''}+py^{'}+qy=f_1(x)$ 的特解减 $y^{''}+py^{'}+qy=f_2(x)$ 的特解

  * 待定系数法
    * $f(x)=P_n(x)e^{\alpha x}$ 型
  
      应设特解为 $y^*=Q_n(x)e^{\alpha x}x^k$

        $$
        \begin{cases}
          e^{\alpha x}照抄\\\\
          Q_n(x)为x的n次多项式\\\\
          k
          \begin{cases}
            0,&\alpha不是特征根\\
            1,&\alpha是单特征根\\
            2,&\alpha是二重特征根
          \end{cases}
        \end{cases}
        $$

    * $f(x)=e^{\alpha x}(P_m(x)\cos{\beta x}+P_n(x)\sin{\beta x})$ 型

      应设特解为 $y^*=e^{\alpha x}\left[\phi_{l}(x)\cos{\beta x}+\psi_l(x)\sin{\beta x}\right]x^k$

        $$
        \begin{cases}
          e^{\alpha x}照抄\\\\
          \phi_l(x),\psi_l(x)分别为x的两个不同的l次多项式，l=\max{(m,n)}\\\\
          k
          \begin{cases}
            0,&\alpha\pm\beta i不是特征根\\
            1,&\alpha\pm\beta i是特征根
          \end{cases}
        \end{cases}
        $$

  * 微分算子法

    约定 $\mathrm{D}=\dfrac{\mathrm{d}}{\mathrm{d}x}\,,\mathrm{D}y=\dfrac{\mathrm{d}y}{\mathrm{d}x}\,,\mathrm{D}^2=\dfrac{\mathrm{d}^2}{\mathrm{d}x^2}\,,\mathrm{D}^2y=\dfrac{\mathrm{d}^2y}{\mathrm{d}x^2}$，则微分方程 $y^{''}+py^{'}+q=f(x)$ 可以写成 $y(\mathrm{D}^2+p\mathrm{D}+q)=f(x)$，进一步记作 $\mathrm{D}^2+pd+q=F(\mathrm{D})$，则微分方程的一个特解为 $y^*=\dfrac{1}{F(\mathrm{D})}f(x)$，根据以下不同类型进行相应处理得到特解。特别地，约定 $\dfrac{1}{\mathrm{D}}$ 为积分，$\mathrm{D}$ 表示求导

    * $\dfrac{1}{F(\mathrm{D})}e^{\alpha x}$ 型

      应设特解为

      $$
      y^*=
      \begin{cases}
        \dfrac{1}{\left.F(\mathrm{D})\right|_{\mathrm{D}=\alpha}}e^{\alpha x},&\left.F(\mathrm{D})\right|_{\mathrm{D}=\alpha}\neq0\\\\
        \dfrac{1}{\left.F^{'}(\mathrm{D})\right|_{\mathrm{D}=\alpha}}e^{\alpha x},&\left.F(\mathrm{D})\right|_{\mathrm{D}=\alpha}=0\,,\left.F^{'}(\mathrm{D})\right|_{\mathrm{D}=\alpha}\neq0\\\\
        \dfrac{1}{\left.F^{''}(\mathrm{D})\right|_{\mathrm{D}=\alpha}}e^{\alpha x},&\left.F(\mathrm{D})\right|_{\mathrm{D}=\alpha}=0\,,\left.F^{'}(\mathrm{D})\right|_{\mathrm{D}=\alpha}=0\,,\left.F^{''}(\mathrm{D})\right|_{\mathrm{D}=\alpha}\neq0
      \end{cases}
      $$

    * $\dfrac{1}{F(\mathrm{D})}e^{\alpha x}v(x)$ 型

      应设特解为

      $$
      y^*=e^{\alpha x}\dfrac{1}{F(\mathrm{D}+\alpha)}v(x)
      $$

    * $\dfrac{1}{\mathrm{D}^2+q}\cos{\beta x}$ 或 $\dfrac{1}{\mathrm{D}^2+q}\sin{\beta x}$ 型

      应设特解为

      $$
      y^*=
      \begin{cases}
        \dfrac{1}{\left(\left.\mathrm{D}^2+q\right)\right|_{\mathrm{D}=\beta i}}\cos{\beta x}&或&\dfrac{1}{\left(\left.\mathrm{D}^2+q\right)\right|_{\mathrm{D}=\beta i}}\sin{\beta x},&{\left(\left.\mathrm{D}^2+q\right)\right|_{\mathrm{D}=\beta i}}\neq0\\\\
        \dfrac{1}{\left(\left.\mathrm{D}^2+q\right)^{'}\right|_{\mathrm{D}=\beta i}}\cos{\beta x}&或&\dfrac{1}{\left(\left.\mathrm{D}^2+q\right)^{'}\right|_{\mathrm{D}=\beta i}}\sin{\beta x},&{\left(\left.\mathrm{D}^2+q\right)\right|_{\mathrm{D}=\beta i}}=0
      \end{cases}
      $$

    * $\dfrac{1}{F(\mathrm{D})}\cos{\beta x}$ 或 $\dfrac{1}{F(\mathrm{D})}\sin{\beta x}$ 型

      应设特解为

      $$
      y^*=\dfrac{1}{\left.F\left(\mathrm{D}\right)\right|_{\mathrm{D}^2=(\beta i)^2}}\cos{\beta x}
      \,\,\,或\,\,\,
      \dfrac{1}{\left.F\left(\mathrm{D}\right)\right|_{\mathrm{D}^2=(\beta i)^2}}\sin{\beta x}
      $$

      先消去 $\mathrm{D}^2$ 项，剩下的关于 $\mathrm{D}$ 在分母上的一次式用 **有理化** 方法消除，最后剩下的在分子上 $\mathrm{D}$ 的一次式用求导或积分的方式消除

    * $\dfrac{1}{F(\mathrm{D})}(x^k+a_1\,x^{k-1}+\cdots+a_{k-1}x+a_k)$ 型

      应设特解为

      $$
      y^*=Q_K(\mathrm{D})(x^k+a_1\,x^{k-1}+\cdots+a_{k-1}x+a_k)
      $$

      其中 $Q_K(\mathrm{D})$ 是 $\dfrac{1}{F(\mathrm{D})}$ 的 $k$ 次泰勒展开多项式

* 高阶 $(k>2)$ 常系数齐次线性微分方程
  1. 若 $r$ 为单实根，特解为 $Ce^{rx}$ </br>
     若解中含特解 $e^{rx}$，则 $r$ 至少为单实根
  2. 若 $r$ 为 $k$ 重实根，特解为 $(C_1+C_2x+C_3x^2+\cdots+C_kx^{k-1})e^{rx}$ </br>
     若解中含特解 $x^{k-1}e^{rx}$，则 $r$ 至少为 $k$ 重实根
  3. 若 $r$ 为单复根 $\alpha\pm\beta i$，特解为 $(C_1\cos{\beta x}+C_2\sin{\beta x})e^{\alpha x}$ </br>
     若解中含特解 $\cos{\beta x}\,或\,\sin{\beta x}$，则 $\alpha\pm\beta i$ 至少为单复根
  4. 若 $r$ 为二重复根 $\alpha\pm\beta i$，特解为 $(C_1\cos{\beta x}+C_2\sin{\beta x}+C_3x\cos{\beta x}+C_4x\sin{\beta x})e^{\alpha x}$ </br>
     若解中含特解 $x\cos{\beta x}\,或\,x\sin{\beta x}$，则 $\alpha\pm\beta i$ 至少为二重复根

  ⚠️**一对单复根 $\alpha\pm\beta i$ 算作两个根**
  
  **反解求方程时，给每个根安排一个为 $0$ 的项，所有项相乘即为方程的特征方程**

* 欧拉方程

  形如 $x^2\dfrac{\mathrm{d}^2y}{\mathrm{d}x^2}+px\dfrac{\mathrm{d}y}{\mathrm{d}x}+qy=f(x)$ 的方程称为欧拉方程，其中 $p,q$ 为常数，$f(x)$ 为已知的连续函数，则 $x>0$ 时，令 $x=e^t$；当 $x<0$ 时，令 $x=-e^t$。欧拉方程可换元为
  
  $$
  \begin{align*}
    \dfrac{\mathrm{d}y}{\mathrm{d}x}=&\dfrac{\mathrm{d}y}{\mathrm{d}t}\cdot\dfrac{\mathrm{d}t}{\mathrm{d}x}=\dfrac{\mathrm{d}y}{\mathrm{d}t}\cdot\dfrac{1}{x}\\\\

    \dfrac{\mathrm{d}^2y}{\mathrm{d}x^2}
    =&\dfrac{\mathrm{d}}{\mathrm{d}x}\left(\dfrac{\mathrm{d}y}{\mathrm{d}t}\cdot\dfrac{1}{x}\right)\\
    =&\dfrac{\mathrm{d}}{\mathrm{d}x}\left(\dfrac{\mathrm{d}y}{\mathrm{d}t}\right)\cdot\dfrac{1}{x}-\dfrac{\mathrm{d}y}{\mathrm{d}t}\cdot\dfrac{1}{x^2}\\
    =&\dfrac{\mathrm{d}\left(\dfrac{\mathrm{d}y}{\mathrm{d}t}\right)}{\mathrm{d}t}\cdot\dfrac{\mathrm{d}t}{\mathrm{d}x}\cdot\dfrac{1}{x}-\dfrac{\mathrm{d}y}{\mathrm{d}t}\cdot\dfrac{1}{x^2}\\
    =&\dfrac{\mathrm{d}^2y}{\mathrm{d}t^2}\cdot\dfrac{1}{x^2}-\dfrac{\mathrm{d}y}{\mathrm{d}t}\cdot\dfrac{1}{x^2}\\\\

    x^2\dfrac{\mathrm{d}^2y}{\mathrm{d}x^2}+px\dfrac{\mathrm{d}y}{\mathrm{d}x}+qy=&f(x)
    \Rightarrow \dfrac{\mathrm{d}^2y}{\mathrm{d}t^2}+(p-1)\dfrac{\mathrm{d}y}{\mathrm{d}t}+qy=f(e^t)
  \end{align*}
  $$

  换元后的欧拉方程即可按二阶常系数线性微分方程求解

* 解的理解

  以二阶常系数非齐次线性微分方程 $y^{''}-3y^{'}+2y=e^x$ 为例，说明各种解的含义

  | 名称 | 定义 | 是否含任意常数 | 是否满足原方程 | 示例 |
  |------|------|------------------|----------------|------|
  | 齐次通解 | 对应齐次方程的所有解 | ✅ 是（两个任意常数） | ✅ 是（满足齐次方程） | $y_h = C_1 e^x + C_2 e^{2x}$ |
  | 齐次特解 | 齐次通解中常数取具体值的结果 | ❌ 否 | ✅ 是（满足齐次方程） | $y = e^x\,,C_1=1, C_2=0$ |
  | 非齐次通解 | 整个方程的所有解，由齐次通解 + 一个非齐次特解组成 | ✅ 是（两个任意常数） | ✅ 是（满足非齐次方程） | $y = C_1 e^x + C_2 e^{2x} + x e^x$ |
  | 非齐次特解 | 满足非齐次方程的一个具体解 | ❌ 否 | ✅ 是（满足非齐次方程） | $y_p = x e^x$ |

  **齐次通解** 是齐次方程 $y'' - 3y' + 2y = 0$ 的所有解</br>
  **齐次特解** 是从齐次通解中取具体常数得到的一个具体解</br>
  **非齐次通解** 是整个非齐次方程的所有解，是齐次通解加上一个非齐次特解</br>
  **非齐次特解** 是我们通过待定系数法、常数变易法等方法找到的一个满足非齐次方程的具体解

### 1.4 微分方程应用

* 几何应用

  追及问题中，后轮轨迹上的切线一定与前轮所在点相交，且前后轮所在点之间的距离恒定

* 物理应用

  列微分方程求解，常用过渡求导，不直接求某个变量的导，而是写成两个微分式相乘，不用考虑微分式的物理意义

## 2 进阶

### 2.1 求微分方程 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

* 一阶微分方程 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式)}$

  分离变量型、齐次型、一阶线性型。特别注意分离变量型会默认丢失一些解，在默认条件下(常为分母式子不为 $0$)求不出来通解时，通解就应该是在默认条件的反情况下取到(如分母的式子为 $0$)

* 二阶可降阶微分方程 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式)}$

  缺 $y$ 型、缺 $x$ 型、全家福不缺型。全家福不缺型往往采用求导公式逆用法，根据导数往回配出多项式

* 高阶常系数线性微分方程 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式)}$

  通解、特解、解的关系、$2$ 阶以上高阶方程解的结构

* ⚠️换元法求解微分方程 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{23} (化归经典形式)}$

  如果看不出来是什么形式的微分方程，立即放弃识别类型，这种情况往往需要配合换元法、求导公式逆用来化归经典形式，不换元时什么也看不出来

### 2.2 建立微分方程 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

* 用极限、导数、积分表达式建立方程 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{22} (转换等价表述) + \text{D}_\text{3} (移花接木)}$
  * 如果是有关极限、导数、积分的等量关系，则令出等式即可
  * 如果是 $f(x),g(x)$ 或 $f^{'}(x),g^{'}(x)$ 的方程组，则消元或求导公式逆用建立方程组。如
  
    $$
    \begin{cases}
      f^{'}(x)+xf^{'}(-x)=x \\
      f^{'}(-x)-xf^{'}(x)=-x
    \end{cases}\xRightarrow{上下配系数消元}
    f^{'}=\dfrac{x+x^2}{1+x^2}
    $$

    如果只给了一个方程，则用换元法得到另一个方程。如第二个方程可由第一个方程令 $u=-x$ 得到

  * 如果是关于 $x,y$ 的恒等式，如 $f(xy)=yf(x)+xf(y)$，则需要带入特殊点求出某点的数值，再写 $f^{'}(x)$ 的导数定义。利用导数定义式得到微分方程

* 用几何量表达式建立方程 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{3} (移花接木)}$
  * 曲线的切线：斜率 $y^{'}=\tan{\theta}$、截距
  * 曲率：$k=\dfrac{\lvert y^{''}\rvert}{\left(1+y^{'}\right)^{\frac{3}{2}}}$。其中 $y^{'}$ 可用斜率 $\tan{\theta}$ 配合 $1+\tan^2{\theta}=\sec^2{\theta}$ 做变形
  * 弧长、侧面积、形心、旋转体体积、图形面积、平均值

* 用变化率表达式建立方程 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{3} (移花接木)}$
  * 注意变化率的正负号，如阻力、降温速度等应该是负的，一般令 $k>0$，手动添负号
  * 位移、速度、加速度：$\dfrac{\mathrm{d}^2 x}{\mathrm{d}t^2}=\dfrac{\mathrm{d}v}{\mathrm{d}t}=a$

## 3 题目

* 基础30讲
  * 例15.1(极值判别第二充分条件)
  * 例15.2(方程与导数关系、洛必达法则)
  * 例15.3(直接分离)
  * 例15.4(隐式解)
  * 例15.5(换元分离、损失通解)
  * 例15.6(齐次型微分方程)
  * ***例15.7(一阶线性微分方程通解公式、$e^{-x}\sin{x}$ 积分)***
  * ***例15.8(交换 $x,y$ 凑一阶线性微分方程)***
  * ***例15.9(一阶线性微分方程通解公式变限积分形式、极限)***
  * ***例15.10(一阶线性微分方程通解公式变限积分形式、证明有界)***
  * 例15.12(既不带y也不带x型二阶可降阶微分方程)
  * ***例15.13(不带x型二阶可降阶微分方程、补全非约束条件下的解)***
  * 例15.15($\Delta>0$ 的二阶常系数齐次线性微分方程)
  * 例15.16($\Delta<0$ 的二阶常系数齐次线性微分方程)
  * 例15.17(二阶常系数非齐次线性微分方程)
  * ***例15.18(二阶常系数非齐次线性微分方程反解)***
  * 例15.19(高阶常系数齐次线性微分方程反解)
  * 例15.20(欧拉方程通解)
  * 例15.21(自行车后轮曲线)
  * 例15.22(过渡求导)
  * 例15.23(分离变量)
* 基础30讲课后习题
  * ***15.1(二阶常系数非齐次线性微分方程解的结构)***
  * ***15.2(二阶常系数非齐次线性微分方程解的结构)***
  * 15.3(确定常数)
  * 15.5(y变形、一阶线性微分方程)
  * 15.6(二阶可降阶微分方程)
  * 15.7(解=齐次通解+非齐次特解)
  * 15.8(欧拉方程x分范围)
  * 15.9(齐次特解、齐次通解、非齐次特解、非齐次通解关系)
  * 15.10(求常数)
  * 15.11(高阶通解、k阶无穷小、泰勒展开)
  * 15.12(二阶可降阶微分方程)
  * 15.13(二阶可降阶微分方程)
* 1000题基础
  * 02($k_法\cdot k_切=-1$、加不加绝对值)
  * 03(积分换元、根据导数凑换元)
  * ***04(dy与dx交换位置)***
  * 06(斜渐近线)
  * 07($x(y)$ 化简回 $y(x)$、参数方程二阶导)
  * ***08(确定定义域)***
  * ***09($x\int^x_0{f(t)\mathrm{d}t}$ 求导是乘法公式)***
  * ***10(一阶线性微分方程变上限积分)***
  * ***16(高阶方程反解)***
  * ***18(高阶方程反解、二阶常系数非齐次线性微分方程解的结构)***
* 强化36讲
  * 例15.1(齐次型微分方程)
  * ***例15.2(齐次型微分方程、有理函数积分)***
  * 例15.3(积分周期性、一阶线性微分方程解的变限积分形式)

    > 变限积分是周期函数的充要条件是一个周期内的积分 $=0$

  * 例15.4(一阶线性微分方程、弧长)

    > $\sqrt{1+\left(\dfrac{1}{2}\Box-\dfrac{1}{2\Box}\right)^2}=\sqrt{\left(\dfrac{1}{2}\Box+\dfrac{1}{2\Box}\right)^2}$，本质就是配平方

  * ***例15.5(求奇点的解)***
  
    > 分离变量时，会默认部分变量 $\neq 0$，这会导致丢失一部分解，但如果通解存在，则可以不管这些丢失的特解；反之如果按照变量 $\neq 0$ 来求，结果通解不存在，就必须按 $=0$ 的情况求这些特解

  * ***例15.6(二阶可降阶微分方程缺 $x$)***
  * ***例15.7(二阶可降解微分方程全家福)***
  * ⭐***例15.8(二阶常系数非齐次线性微分方程、反常积分敛散性)***
  * ***例15.9(欧拉方程)***
  * ⭐***例15.10(高阶常系数齐次线性微分方程反解)***
  
    > **$k$ 重实根 $a$ 设为 $(r-a)^k$ </br> $k$ 重复根 $\alpha\pm\beta i$ 设为 $\Big[\big(r-(\alpha+\beta i)\big)\big(r-(\alpha-\beta i)\big)\Big]^k=\Big[(r-\alpha)^2+\beta^2\Big]^k$**

  * ⭐***例15.11-12(换元法、求导公式逆用)***
  * ⭐***例15.13(根据恒等式建立微分方程、导数 $\Delta$ 式定义、复合函数换元)***
  
    > 见到复合函数 $f[g(x,y)]$ 立马令 $u=g(x,y)$，换成 $f(u)$。注意区别 $f(xy)$ 与 $f(x,y)$，前者是一元函数，后者是二元函数

  * ***例15.14(根据切线斜率和截距建立微分方程)***
  * ***例15.15(根据曲率和三角函数建立微分方程)***
  * ⛔***例15.17(根据变化率建微分方程)***
  * ⭐***例15.18(同基础30讲例15.21)***
* 1000题强化
  * ⭐***01(一阶线性微分方程解的关系)***
  * ⛔***02(证明一阶线性微分方程有唯一周期解、一阶线性微分方程解的变限积分形式)***
  
    > * 证明 $f(x)$ 是以 $a$ 为周期的函数，则要证明 $f(x+a)-f(x)=0$
    > * 要证明某项应该是常数而不是函数时，可对其求导，如果导数为 $0$ 就是常数(常函数)，这时取最简单的变量带入(如 $x=0$)即可求得该常值

  * ***04(一阶线性微分方程解的变限积分形式、洛必达、含参讨论极限情况)***
  * ***05(二阶常系数齐次线性微分方程解的周期性)***
  * ***08(积分结果为 $\ln$ 时的常数项写法)***
  
    > 若某个积分结果为 $\ln{f(x)}$，在添加常数项时可以写作 $\ln{f(x)}+\ln{C_1}=\ln{[C_1 f(x)]}$，后续若需要抬 $e$ 就能写作 $C_1 f(x)$

  * ⭐***09-10(用 $\dfrac{\mathrm{d}x}{\mathrm{d}y}$ 求函数 $x(y)$)***
  
    > 原方程用 $\dfrac{\mathrm{d}y}{\mathrm{d}x}$ 求 $y(x)$ 不好做时，可以倒过来用 $\dfrac{\mathrm{d}x}{\mathrm{d}y}$ 求 $x(y)$

  * ***12(可导性判断)***
  
    > 若 $f(x)=\Box$，即使没说 $f(x)$ 可导，只要 $\Box$ 可导，那 $f(x)$ 就可导

  * ⭐13(求二阶常系数非齐次线性微分方程)
  * 14(积分曲线)
  
    > 微分方程的解 $y=y(x)$ 既是关于 $x$ 的函数，也称曲线 $y$

  * ***15(讨论二阶常系数齐次线性微分方程的解、微分方程的解求反常积分)***
  * ⭐***18(解的周期性)***
  * ***21(导数公式逆用)***
  * ⭐⭐⭐⭐⭐***23(二阶微分方程解的结构)***
  
    > 1.方程 $y^{''}+py^{'}+qy=f_1(x)+f_2(x)$ 的特解为 $y^{''}+py^{'}+qy=f_1(x)$ 的特解加 $y^{''}+py^{'}+qy=f_2(x)$ 的特解
    >
    > 2.方程 $y^{''}+py^{'}+qy=f(x)$ 的通解为 $y^{''}+py^{'}+qy=f_1(x)$ 的特解减 $y^{''}+py^{'}+qy=f_2(x)$ 的特解

  * ***28(方程反解)***
  
    > 若齐次方程的一个解为 $y_1$，则 $k y_1$ 也是齐次方程的解，$k$ 为任意实数； </br> 反过来说，若 $y_1$ 和 $k y_1$ 都是方程的解，则该方程是齐次方程

  * ⭐***33(换元法、反函数二阶导公式、微元错位相乘法)***
  * ⭐***34(换元法)***
  * ***37(微分方程的解是分段函数)***
  * ***39(含参讨论微分方程的解的拐点)***
  * ⭐***41(导数公式逆用)***
  
    > 有时候可能直接求不出来 $y(x)$，但通过导数公式逆用能求出来 $g[y(x)]$ 的表达式，这时就先求 $g(y)$ 的表达式，再根据 $g$ 的映射规则反求出 $y(x)$ 。如 $e^y y^{'}$ 就是 $g[y(x)]=e^y$ 对 $x$ 的导数，就可以先求关于 $e^y$ 的微分方程的解

  * ⚠️43(伯努利方程)
  * ⚠️44(欧拉方程)
  * ***45(排除解)***
  
    > 因带绝对值而产生多解时(如 $\ln\lvert y\rvert$)，一定要回看题目条件进行排除

  * 47(齐次型缺 $x$)
  * ⛔***48(齐次型缺 $x,y$、根式有理化联立、形心坐标)***
  
    > 想从 $y+\sqrt{1+y^2}=f(x)$ 中求 $y(x)$，先取倒数，再分母有理化形成方程组联立求解
    >
    > $$
    > \dfrac{1}{f(x)}=\dfrac{1}{y+\sqrt{1+y^2}}=\dfrac{\sqrt{1+y^2}-y}{\left[\sqrt{1+y^2}+y\right]\cdot\left[\sqrt{1+y^2}-y\right]}=\sqrt{1+y^2}-y
    > $$
    >
    > 联立方程组即可求出 $y(x)$
    >
    > $$
    > \begin{cases}
    >   y+\sqrt{1+y^2}=f(x)\\
    >   \sqrt{1+y^2}-y=f^{-1}(x)
    > \end{cases}
    > $$

  * 49(计算)
  * ⭐***50(双动点问题、凑微分把 $y^{'}$ 凑了、根式有理化联立)***

    > 双动点问题设一个点为 $(x_0,y_0)$，另一个点变量化为 $(x,y)$。否则都设为常数点会导致微分方程不能依靠变限积分进行求导变化，根本求不出来
