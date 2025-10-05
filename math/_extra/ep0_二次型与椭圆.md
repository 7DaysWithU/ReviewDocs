# 二次型与椭圆

要利用**二次型与椭圆理论**来分析并画出二次型曲线如 $x^2 + y^2 - xy = 1$ 的形状，从而为**二重积分定界**提供帮助，我们可以按照以下系统性的步骤进行：

---

## 1 二次型转换成椭圆

### ✅ 第一步：识别为二次型

给定曲线：
$$
x^2 + y^2 - xy = 1
$$

这是一个**二次曲线**（圆锥曲线），可以写成矩阵形式（二次型）：
$$
\begin{bmatrix} x & y \end{bmatrix}
\begin{bmatrix}
1 & -\dfrac{1}{2} \\
-\dfrac{1}{2} & 1
\end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix} = 1
$$

记作：
$$
\mathbf{x}^T A \mathbf{x} = 1, \quad \text{其中 } A = \begin{bmatrix} 1 & -1/2 \\ -1/2 & 1 \end{bmatrix}
$$

---

### ✅ 第二步：判断是否为椭圆

我们检查矩阵 $ A $ 的特征值是否**全正**，以判断这是椭圆。

计算特征值：

$$
\det(A - \lambda I) =
\begin{vmatrix}
1 - \lambda & -1/2 \\
-1/2 & 1 - \lambda
\end{vmatrix}
= (1 - \lambda)^2 - \left(\dfrac{1}{2}\right)^2 = \lambda^2 - 2\lambda + 1 - \dfrac{1}{4} = \lambda^2 - 2\lambda + \dfrac{3}{4}
$$

解方程：
$$
\lambda^2 - 2\lambda + \dfrac{3}{4} = 0
\Rightarrow \lambda = \dfrac{2 \pm \sqrt{4 - 3}}{2} = \dfrac{2 \pm 1}{2}
\Rightarrow \lambda_1 = \dfrac{3}{2},\quad \lambda_2 = \dfrac{1}{2}
$$

✅ 两个特征值均为正 ⇒ 曲线是一个**椭圆**。

---

### ✅ 第三步：对角化矩阵，得到标准椭圆形式

我们需要通过**坐标旋转**（主轴变换）将椭圆化为标准形式：
$$
\dfrac{X^2}{a^2} + \dfrac{Y^2}{b^2} = 1
$$

🔹 求特征向量（确定旋转方向）

对 $\lambda_1 = \dfrac{3}{2}$：
$$
(A - \tfrac{3}{2}I)\mathbf{v} =
\begin{bmatrix}
-1/2 & -1/2 \\
-1/2 & -1/2
\end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix} = 0
\Rightarrow x + y = 0 \Rightarrow \mathbf{v}_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}
\Rightarrow \text{单位化：} \dfrac{1}{\sqrt{2}}\begin{bmatrix} 1 \\ -1 \end{bmatrix}
$$

对 $\lambda_2 = \dfrac{1}{2}$：
$$
(A - \tfrac{1}{2}I)\mathbf{v} =
\begin{bmatrix}
1/2 & -1/2 \\
-1/2 & 1/2
\end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix} = 0
\Rightarrow x - y = 0 \Rightarrow \mathbf{v}_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}
\Rightarrow \text{单位化：} \dfrac{1}{\sqrt{2}}\begin{bmatrix} 1 \\ 1 \end{bmatrix}
$$

所以正交变换矩阵为：
$$
P = \dfrac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 \\
-1 & 1
\end{bmatrix}
= \begin{bmatrix}
\cos\theta & \sin\theta \\
-\sin\theta & \cos\theta
\end{bmatrix},\quad \theta = 45^\circ
$$

这表示：**将坐标系逆时针旋转 $ 45^\circ $**，即可使椭圆主轴与新坐标轴对齐。

令：
$$
\begin{cases}
x = \dfrac{1}{\sqrt{2}}(X - Y) \\
y = \dfrac{1}{\sqrt{2}}(X + Y)
\end{cases}
\quad \text{或写作 } \begin{bmatrix} x \\ y \end{bmatrix} = P \begin{bmatrix} X \\ Y \end{bmatrix}
$$

代入原方程：
$$
\mathbf{x}^T A \mathbf{x} = \mathbf{X}^T P^T A P \mathbf{X} = \mathbf{X}^T D \mathbf{X} = \lambda_1 X^2 + \lambda_2 Y^2 = \dfrac{3}{2}X^2 + \dfrac{1}{2}Y^2 = 1
$$

整理得标准形式：
$$
\dfrac{3}{2}X^2 + \dfrac{1}{2}Y^2 = 1
\Rightarrow \dfrac{X^2}{( \sqrt{2/3} )^2} + \dfrac{Y^2}{( \sqrt{2} )^2} = 1
$$

即：
$$
\dfrac{X^2}{\dfrac{2}{3}} + \dfrac{Y^2}{2} = 1
$$

---

### ✅ 第四步：几何理解与作图

- 这是一个中心在原点的椭圆。
- 在**旋转后的坐标系 $(X,Y)$** 中（即原坐标系逆时针转 $45^\circ$）：
  - 半长轴：$b = \sqrt{2} \approx 1.414$，沿 $Y$ 方向（对应原 $y=x$ 方向）
  - 半短轴：$a = \sqrt{2/3} \approx 0.816$，沿 $X$ 方向（对应原 $y=-x$ 方向）

📌 所以这个椭圆的**长轴在直线 $ y = x $ 上**，短轴在 $ y = -x $ 上。

---

### ✅ 第五步：用于二重积分定界

现在你想在这个区域 $ D: x^2 + y^2 - xy \leq 1 $ 上计算二重积分。

- 方法一：使用**旋转坐标变换**

  令：
  $$
  \begin{cases}
  X = \dfrac{x + y}{\sqrt{2}} \\
  Y = \dfrac{-x + y}{\sqrt{2}}
  \end{cases}
  \quad \text{即 } \begin{bmatrix} X \\ Y \end{bmatrix} = P^T \begin{bmatrix} x \\ y \end{bmatrix}
  $$
  
  则区域变为：
  $$
  \dfrac{3}{2}X^2 + \dfrac{1}{2}Y^2 \leq 1 \Rightarrow \dfrac{X^2}{2/3} + \dfrac{Y^2}{2} \leq 1
  $$

  这是一个标准椭圆区域，可用**广义极坐标变换**：

  令：
  $$
  X = \sqrt{\dfrac{2}{3}}\, r \cos\theta, \quad Y = \sqrt{2}\, r \sin\theta, \quad r \in [0,1],\ \theta \in [0, 2\pi]
  $$

  再代回 $ x, y $ 表达式：
  $$
  \begin{bmatrix} x \\ y \end{bmatrix} = P \begin{bmatrix} X \\ Y \end{bmatrix} = \dfrac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} X \\ Y \end{bmatrix}
  $$

  最终得到：
  $$
  x = \dfrac{1}{\sqrt{2}} (X + Y), \quad y = \dfrac{1}{\sqrt{2}} (-X + Y)
  $$
  
  并计算雅可比行列式 $|\det J|$，注意两次变换的复合雅可比。
  
  但更高效的是直接写出从 $(r,\theta) \to (x,y)$ 的变换，并求雅可比。

- 方法二：直接画图辅助定界（适用于不换元的情况）

  如果你不想换元，只想画图辅助判断积分上下限：

  - **画出椭圆轮廓**：
    - 中心在原点。
    - 长轴沿 $y = x$，长度 $2\sqrt{2} \approx 2.828$
    - 短轴沿 $y = -x$，长度 $2\sqrt{2/3} \approx 1.633$

  - 可以取几个关键点估算：
    - 当 $x = 0$：$y^2 = 1 \Rightarrow y = \pm1$
    - 当 $y = 0$：$x^2 = 1 \Rightarrow x = \pm1$
    - 当 $x = y$：$x^2 + x^2 - x^2 = x^2 = 1 \Rightarrow x = \pm1 \Rightarrow (1,1), (-1,-1)$
    - 当 $x = -y$：$x^2 + x^2 + x^2 = 3x^2 = 1 \Rightarrow x = \pm1/\sqrt{3} \Rightarrow (\pm1/\sqrt{3}, \mp1/\sqrt{3})$

  这些点帮助你大致画出椭圆：它在 $(1,1)$ 和 $(-1,-1)$ 处最“宽”，在 $(1,-1)$ 方向较“窄”。

---

### ✅ 总结：如何用二次型理论画曲线并定界

| 步骤 | 内容 |
|------|------|
| 1️⃣ | 将二次曲线写成 $\mathbf{x}^T A \mathbf{x} = 1$ 形式 |
| 2️⃣ | 计算 $A$ 的特征值 → 判断是否为椭圆（全正） |
| 3️⃣ | 求特征向量 → 得到主轴方向（旋转角度） |
| 4️⃣ | 做正交变换（旋转坐标）消去交叉项，得标准椭圆 |
| 5️⃣ | 根据长短轴画图，确定区域范围 |
| 6️⃣ | 若用于积分，可进一步做伸缩变换转为圆域，或直接估计边界 |

---

### 📌 应用建议

- 在**二重积分**中，若被积函数也具有对称性，这种变换非常有用。
- 若只是定界（如直角坐标下积分），可通过画出主轴和关键点，判断 $x$ 的范围（如 $[-1.2, 1.2]$），再对每个 $x$ 解出 $y$ 的上下限（解二次方程）。
- 更高级做法：使用**广义极坐标**或**仿射变换 + 极坐标**简化积分。

## 2 二次方程对应图像的旋转角公式

对于一般的二次方程 $Ax^2+Bxy+Cy^2+Dx+Ey+F=0$，其对应图像的旋转角 $\theta=\dfrac{B}{A-C}$

> **特别地，该公式只能计算旋转角的大小，不能确定旋转方向。旋转方向可以快速带入几个具体点进行确认**

## 3 判断旋转的圆或椭圆

这是一个非常关键且实用的问题！在考试或解题中，我们经常遇到像 $Ax^2 + Bxy + Cy^2 = 1$ 这类带有交叉项 $xy$ 的二次曲线。虽然标准的圆和椭圆（如 $x^2 + y^2 = 1$ 或 $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$）我们很熟悉，但一旦出现 $xy$ 项，图像就“歪了”——即**发生了旋转**。

下面我将系统地教你如何**快速识别**这类旋转后的圆或椭圆，并判断其图像特征，无需复杂计算，适合考试使用。

---

### ✅ 3.1 先判断：这是圆？椭圆？还是别的？

给定一般二次曲线（无一次项）：
$$
Ax^2 + Bxy + Cy^2 = 1
$$

- 判别准则（基于判别式）

  定义判别量：
  $$
  \Delta = B^2 - 4AC
  $$
  
  | $\Delta$ 情况 | 曲线类型 | 说明 |
  |---------------|----------|------|
  | $\Delta < 0$ | **椭圆型**（可能是圆） | 封闭曲线，可用于二重积分定界 |
  | $\Delta = 0$ | 抛物型 | 非封闭 |
  | $\Delta > 0$ | 双曲型 | 开放曲线（两支） |
  
  📌 **我们只关心 $\Delta < 0$ 的情况**，即旋转后的椭圆或圆。

---

### ✅ 3.2 如何判断是否是“旋转的圆”？

圆在旋转后仍然是圆，但方程会多出 $xy$ 项。

> ***判断标准：***
>
> 若 $A = C$ 且 $B \neq 0 $，则该方程表示一个**旋转的圆**。

✅ 例子

$$
x^2 + xy + y^2 = 1
\quad\Rightarrow\quad A = 1,\ C = 1,\ B = 1
\Rightarrow A = C,\ B \ne 0
\Rightarrow \text{这是一个旋转了的圆！}
$$

- 半径可通过配方或变换求出，但关键是：**它仍然是圆，所有方向“胖瘦”一样**。
- 图像：一个被旋转 $45^\circ$ 的圆（看起来像“钻石”方向的椭圆，但其实是圆）。

---

### ✅ 3.3 如何判断是“旋转的椭圆”？长轴方向在哪？

当 $\Delta < 0$ 但 $A \neq C$，或 $A = C$ 但形状不对称（实际 $A \ne C$），则是**旋转的椭圆**。

- 步骤 1：用公式估算旋转角

  $$
  \tan(2\alpha) = \dfrac{B}{A - C}
  $$
  
  - 解出 $2\alpha$，再得 $\alpha$（主轴旋转角）
  - 注意：$\alpha$ 是将坐标系**逆时针旋转 $\alpha$** 后，可消去 $xy$ 项

  📌 特殊情况
  
  - 若 $A = C$，则分母为 0 ⇒ $\tan(2\alpha) \to \infty$ ⇒ $2\alpha = \pm \dfrac{\pi}{2}$ ⇒ $\alpha = \pm 45^\circ$
  - 若 $B = 0$，则 $\tan(2\alpha) = 0$ ⇒ $\alpha = 0^\circ$ 或 $90^\circ$，即无旋转

- 步骤 2：代入测试点，判断长轴方向

  | 方向 | 代入方式 | 判断依据 |
  |------|----------|----------|
  | $y = x$ | 令 $x = y$，代入方程 | 看解出的 $x$ 是否大（远） ⇒ 若远，则长轴在此方向 |
  | $y = -x$ | 令 $y = -x$ | 同上 |
  | $x = 0$ | 令 $x = 0$，看 $y$ 范围 | 判断上下跨度 |
  | $y = 0$ | 令 $y = 0$，看 $x$ 范围 | 判断左右跨度 |

  👉 **哪个方向能取到更大的 $|x|$ 或 $|y|$，哪个方向就是“长轴方向”**

---

### ✅ 3.4 经典例子对比分析

| 方程 | $A,C,B$ | $\Delta = B^2 - 4AC$ | 类型 | 旋转角 | 长轴方向 | 图像特点 |
|:---:|:-------:|:-----------------:|:------:|:--------:|:----------:|:----------:|
| $x^2 + y^2 = 1$ | $1,1,0$ | $0 - 4 = -4 < 0$ | 圆 | $0^\circ$ | 任意 | 标准圆 |
| $x^2 + xy + y^2 = 1$ | $1,1,1$ | $1 - 4 = -3 < 0$ | **旋转的圆** | $45^\circ$ | 所有方向等长 | 看似椭圆，实为圆 |
| $x^2 - xy + y^2 = 1$ | $1,1,-1$ | $1 - 4 = -3 < 0$ | **旋转的圆** | $-45^\circ$ | 同上 | 对称 |
| $2x^2 - 2xy + y^2 = 1$ | $2,1,-2$ | $4 - 8 = -4 < 0$ | **旋转椭圆** | $\tan 2\alpha = \dfrac{-2}{2-1} = -2$ ⇒ $2\alpha \approx -63.4^\circ$ ⇒ $\alpha \approx -31.7^\circ$ | 计算或代点验证 | “歪”的椭圆 |

---

### ✅ 3.5 图像识别口诀（考试速记）

> 🌟 **“一看判别式，负为椭圆；**  
> **二看 A 等 C，是圆就转 $45^\circ$；**  
> **三用 $\tan 2\alpha$，算角定方向；**  
> **四代关键点，谁远谁是长轴向。”**

---

### ✅ 3.6 如何用于二重积分定界？

一旦识别出是旋转椭圆：

- 方法 1：极坐标换元（最快）

  令 $x = r\cos\theta,\ y = r\sin\theta$，代入原方程，解出 $r(\theta)$：
  $$
  r^2 (A\cos^2\theta + B\cos\theta\sin\theta + C\sin^2\theta) = 1
  \Rightarrow r(\theta) = \dfrac{1}{\sqrt{A\cos^2\theta + B\cos\theta\sin\theta + C\sin^2\theta}}
  $$

✅ 积分区域：$0 \leq \theta \leq 2\pi$，$0 \leq r \leq r(\theta)$

- 方法 2：直角坐标定界（观察法）

  - $x$ 范围：从图像估计，如 $[-1.5, 1.5]$
  - 对每个 $x$，解关于 $y$ 的二次方程，得上下限

---

### ✅ 3.7 总结：旋转椭圆/圆的识别流程图

```Text
给定：Ax² + Bxy + Cy² = 1
        ↓
计算 Δ = B² - 4AC
        ↓
      Δ ≥ 0 ? ———是——→ 非封闭（双曲/抛物）
        ↓ 否
     是椭圆型！
        ↓
     A == C ? ——是——→ 是旋转的圆！旋转角 ±45°
        ↓ 否
   计算 tan(2α) = B/(A−C)
        ↓
    得旋转角 α（主轴方向）
        ↓
   代入 y=x, y=-x 等测试点
        ↓
   判断长轴方向（谁远谁长）
        ↓
    可画草图，用于定界
```
